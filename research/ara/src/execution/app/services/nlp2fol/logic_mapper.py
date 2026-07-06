# Grounding: transcribed from oshima/api/app/services/nlp2fol/logic_mapper.py
"""
LogicMapper
===========

Purpose
-------
Map neutral cues from the Logical Feature Detector to a domain-agnostic
"logic plan" that the Composer can realize into FOL later.

Expected Input
--------------
features: dict with this shape (from detector):
{
  "sentence": str,
  "triples": [                       # atomic, ID-assigned triples
    { "id":"T#","subject":str,"relation":str,"object":str,"sentence":str }
  ],
  "operator_cues": [                 # NEG / COORD, neutral only
    {
      "kind":"COORD|NEG",
      "span":[char_start,char_end],
      "attaches_to":"SUBJ|REL|OBJ|SENT",
      "triple_ids":["T1","T2"],      # optional if resolved
      "cue_text":"string (optional)"
    }
  ],
  "implication_cues": [              # if / then / when / unless
    {
      "cue_span":[c_start,c_end],
      "antecedent_span":[a_start,a_end] | null,
      "consequent_span":[b_start,b_end] | null,
      "antecedent_triple_ids":["T#"...],
      "consequent_triple_ids":["T#"...],
      "cue_text":"if|then|when|unless|..."
    }
  ],
  "quantifier_cues": [
    {
      "cue_span":[q_start,q_end],
      "target_span":[n_start,n_end],
      "target_head_token": int | null,
      "polarity":"POS|NEG|UNKNOWN",
      "cue_text":"all|every|some|no|most|few|at least one|..."
    }
  ]
}

Returned Output
---------------
logic_plan: dict
{
  "ops": [                           # boolean/implication operators
    # Unary:
    {"op":"NEG","triples":["T2"],"reason":"not|no|..."},
    # N-ary boolean:
    {"op":"AND","triples":["T1","T3"]},
    {"op":"OR","triples":["T1","T2"]},
    {"op":"NOR","triples":["T1","T2"]},       # lowered later to ¬(A ∨ B)
    {"op":"NAND","triples":["T1","T2"]},      # lowered later to ¬(A ∧ B)
    {"op":"XOR","triples":["T1","T2"]},       # lowered later to (A∨B)∧¬(A∧B)
    {"op":"XNOR","triples":["T1","T2"]},      # lowered later to equivalence
    {"op":"EQUIV","triples":["T1","T2"]},     # ↔ (if and only if / equivalent)
    # Implication family:
    {"op":"IMPL","lhs":["T1"],"rhs":["T2"]},         # A → B
    {"op":"NONIMPL","lhs":["T1"],"rhs":["T2"]},      # A ↛ B  (Composer lowers to A ∧ ¬B)
    {"op":"CONVERSE_IMPL","lhs":["T2"],"rhs":["T1"]},# B → A  (“only if”)
    {"op":"CONVERSE_NONIMPL","lhs":["T2"],"rhs":["T1"]} # B ↛ A
  ],
  "quant": [                         # quantifiers + scope
    {"type":"FORALL","var_hint":"NP@[a,b]","scope":["T1","T2","T3"]},
    {"type":"EXISTS","var_hint":"NP@[c,d]","scope":["T2"]},
    {"type":"NOT_EXISTS","var_hint":"NP@[e,f]","scope":["T4"]}  # Composer lowers to ¬∃ or ∀¬
  ],
  "scopes": { "T1":"antecedent|consequent|null", "T2":"..." }
}

Notes
-----
- This module DOES NOT render symbols (¬ ∧ ∨ → ↔ ∀ ∃). The Composer decides
  pretty-printing and lowering rules, e.g.:
    NOR(A,B)   ⇒ ¬(A ∨ B)
    NAND(A,B)  ⇒ ¬(A ∧ B)
    XOR(A,B)   ⇒ (A ∨ B) ∧ ¬(A ∧ B)
    XNOR(A,B)  ⇒ (A ∧ B) ∨ (¬A ∧ ¬B) or EQUIV(A,B)
    NONIMPL(A,B) ⇒ A ∧ ¬B
- If a coordinator lacks explicit triple_ids, the mapper groups triples by
  (subject, relation) as a pragmatic default.
- Quantifiers carry a var_hint (usually an NP span). The VariableBinder will
  assign variable names and types and bind them across triples.
"""

from __future__ import annotations

from typing import Any, Dict, List

# --------- helpers


def _cue_text(c: dict) -> str:
    return (c.get("cue_text") or "").lower().strip()


def _unique(seq):
    seen = set()
    out = []
    for x in seq:
        if x not in seen:
            seen.add(x)
            out.append(x)
    return out


import re


def _span_of_substring(text: str, fragment: str):
    if not fragment:
        return None
    i = text.lower().find(fragment.lower())
    return None if i == -1 else (i, i + len(fragment))


def _overlaps(a, b):
    return a and b and not (a[1] <= b[0] or b[1] <= a[0])


def _center_distance(a, b):
    if not a or not b:
        return float("inf")
    ca = (a[0] + a[1]) / 2.0
    cb = (b[0] + b[1]) / 2.0
    return abs(ca - cb)


def _ensure_arg_spans(sentence: str, triples: list):
    """
    Attach quick subject/object char spans to each triple in-place as:
      t["_subj_span"], t["_obj_span"]
    """
    for t in triples:
        t["_subj_span"] = _span_of_substring(sentence, t.get("subject", ""))
        t["_obj_span"] = _span_of_substring(sentence, t.get("object", ""))


# --------- public API


def map_to_logic(features: Dict[str, Any]) -> Dict[str, Any]:
    """
    Input (from detector):
      {
        "sentence": str,
        "triples": [{"id": "T1", "subject": "...", "relation": "...", "object": "...", "sentence": "..."}],
        "operator_cues": [{"kind":"COORD|NEG","span":[...],"attaches_to":"SUBJ|REL|OBJ|SENT","triple_ids":[...],"cue_text": "..."}],
        "implication_cues": [{"cue_span":[...],"antecedent_span":[...],"consequent_span":[...],
                              "antecedent_triple_ids":[...],"consequent_triple_ids":[...],"cue_text":"if|then|..."}],
        "quantifier_cues": [{"cue_span":[...], "target_span":[...], "polarity":"POS|NEG|UNKNOWN", "cue_text":"all|no|some|..."}]
      }

    Output (logic plan):
      {
        "ops": [ {"op":"AND|OR|NOR|XOR|NEG|IMPL|EQUIV", ... } ],
        "quant": [ {"type":"FORALL|EXISTS|NOT_EXISTS","var_hint": "np_head_or_span", "scope": ["T#"...]} ],
        "scopes": {"T#":"antecedent|consequent|null"}
      }
    """
    triples = features.get("triples", [])
    t_ids = [t["id"] for t in triples]

    _ensure_arg_spans(features.get("sentence", ""), triples)

    ops: List[Dict[str, Any]] = []
    scopes: Dict[str, str] = {tid: "null" for tid in t_ids}
    quant: List[Dict[str, Any]] = []

    # ---------- implication (→) / biconditional (↔) if needed later
    # Merge multiple implication cues; prefer the widest clause split.
    impls = features.get("implication_cues", []) or []
    if impls:
        # pick first 'if' cue; attach triples from ids provided
        best = None
        for c in impls:
            if _cue_text(c) in {"if", "unless", "when", "whenever", "provided that"}:
                best = c
                break
        if not best:
            best = impls[0]

        lhs = _unique(best.get("antecedent_triple_ids", []))
        rhs = _unique(best.get("consequent_triple_ids", []))
        if lhs and rhs:
            ops.append({"op": "IMPL", "lhs": lhs, "rhs": rhs})
            for tid in lhs:
                scopes[tid] = "antecedent"
            for tid in rhs:
                scopes[tid] = "consequent"

    # ---------- coordination / negation
    # Group cues by text to infer OR/NOR/XOR hints; default AND when multiple
    # independent triples share same subj/rel and cue is 'and'.
    coord = [c for c in features.get("operator_cues", []) if c.get("kind") == "COORD"]
    negs = [c for c in features.get("operator_cues", []) if c.get("kind") == "NEG"]

    # Negations -> mark as unary ops on provided triple_ids
    for n in negs:
        tids = n.get("triple_ids") or []
        for tid in tids:
            ops.append({"op": "NEG", "triples": [tid], "reason": _cue_text(n)})

    # Coordination mapping:
    # - 'or'  → OR over its attached triples (fallback: all)
    # - 'nor' / 'neither'...'nor' → NOR (Composer can lower to ¬(A∨B))
    # - 'xor' / 'exactly one' → XOR (Composer can lower to (A∨B) ∧ ¬(A∧B))
    # - 'and' / 'both' → AND
    # If no triple_ids provided, apply over all with same (subject, relation).
    def triples_for_coord(c):
        tids = c.get("triple_ids") or []
        if tids:
            return tids

        # Proximity fallback: choose the two triples whose NP spans are closest to the cue
        cue_span = tuple(c.get("span") or [])
        if len(cue_span) == 2:
            scored = []
            for t in triples:
                d = min(
                    _center_distance(cue_span, t.get("_subj_span")),
                    _center_distance(cue_span, t.get("_obj_span")),
                )
                scored.append((d, t["id"]))
            scored.sort(key=lambda x: x[0])
            # usually 2 is right for “X and/or Y”
            picked = [tid for _, tid in scored[:2] if _ != float("inf")]
            if len(picked) >= 2:
                return picked

        # Legacy fallback: largest group by (subject, relation)
        groups = {}
        for t in triples:
            key = (t["subject"].lower(), t["relation"].lower())
            groups.setdefault(key, []).append(t["id"])
        if groups:
            return max(groups.values(), key=len)

        return t_ids

    for c in coord:
        text = _cue_text(c)
        tids = _unique(triples_for_coord(c))
        if len(tids) < 2:
            continue

        if text in {"or"}:
            sent_low = (features.get("sentence") or "").lower()
            if (
                "exactly one" in sent_low
                or re.search(r"\beither\b.*\bor\b.*\bbut not both\b", sent_low)
                or re.search(r"\bbut not both\b", sent_low)
                or re.search(r"\bonly one of\b.*\bor\b", sent_low)
                or re.search(r"\bone but not both\b", sent_low)
            ):  # TODO: expand this regex to detect "either ... or ... but not both" cases
                ops.append({"op": "XOR", "triples": tids})
            else:
                ops.append({"op": "OR", "triples": tids})
        elif text in {"nor"}:
            ops.append({"op": "NOR", "triples": tids})
        elif text in {"neither"}:
            # 'neither ... nor ...' often surfaces as two cues; let Composer lower to NOR
            ops.append({"op": "NOR", "triples": tids})
        elif text in {"xor"} or "exactly one" in text:
            ops.append({"op": "XOR", "triples": tids})
        elif text in {"and", "both", "as well as"}:
            ops.append({"op": "AND", "triples": tids})
        elif text in {"but"}:
            # treat as AND; actual negation usually captured by a nearby NEG cue
            ops.append({"op": "AND", "triples": tids})
        else:
            # default to AND for unknown coordinators
            ops.append({"op": "AND", "triples": tids})

    # ---------- simple equivalence (↔) if explicit cues appear
    # Rare in prose, but support “equivalent”, “if and only if”
    # (detector could add a dedicated cue later)
    if " iff " in (" " + features.get("sentence", "").lower() + " "):
        # naive: all triples participate symmetrically
        ops.append({"op": "EQUIV", "triples": t_ids})

    # ---------- quantifiers (∀ / ∃ / ¬∃)  — with target_role inference
    for q in features.get("quantifier_cues") or []:
        cue = _cue_text(q)
        pol = (q.get("polarity") or "POS").upper()

        if cue in {"all", "every", "each", "any"} and pol != "NEG":
            qtype = "FORALL"
        elif cue in {"some", "at least one", "there exists"} and pol != "NEG":
            qtype = "EXISTS"
        elif cue == "no" or pol == "NEG":
            qtype = "NOT_EXISTS"
        else:
            continue

        target_span = tuple(q.get("target_span") or [])
        scope_ids = []
        target_role = None  # "SUBJ" | "OBJ" | None

        # Collect overlaps against SUBJ/OBJ spans (you already set _subj_span/_obj_span earlier)
        if len(target_span) == 2:
            for t in triples:
                subj_sp, obj_sp = t.get("_subj_span"), t.get("_obj_span")
                hit_subj = _overlaps(target_span, subj_sp)
                hit_obj = _overlaps(target_span, obj_sp)
                if hit_subj or hit_obj:
                    scope_ids.append(t["id"])

            # Role preference by quantifier type:
            if qtype == "FORALL":
                # Universals typically bind the SUBJECT NP
                for t in triples:
                    if t["id"] in scope_ids and _overlaps(
                        target_span, t.get("_subj_span")
                    ):
                        target_role = "SUBJ"
                        break
                if target_role is None:
                    for t in triples:
                        if t["id"] in scope_ids and _overlaps(
                            target_span, t.get("_obj_span")
                        ):
                            target_role = "OBJ"
                            break
                if target_role is None:
                    target_role = "SUBJ"  # default when spans are ambiguous/missing
            else:
                # EXISTS / NOT_EXISTS: default preference to the OBJECT NP
                for t in triples:
                    if t["id"] in scope_ids and _overlaps(
                        target_span, t.get("_obj_span")
                    ):
                        target_role = "OBJ"
                        break
                if target_role is None:
                    for t in triples:
                        if t["id"] in scope_ids and _overlaps(
                            target_span, t.get("_subj_span")
                        ):
                            target_role = "SUBJ"
                            break

        # Fallback: if nothing overlapped, keep previous behavior (all triples in scope)
        if not scope_ids:
            scope_ids = t_ids
            # Sensible defaults if we have no spans at all:
            if target_role is None:
                target_role = "SUBJ" if qtype == "FORALL" else "OBJ"

        # logic_mapper.py  (inside map_to_logic, when building quant.append)
        quant.append(
            {
                "type": qtype,
                "var_hint": "NP@" + str(q.get("target_span")),
                "scope": _unique(scope_ids),
                "target_role": target_role,  # existing
                "cue_span": q.get("cue_span"),  # NEW: preserve cue span
                "target_span": q.get("target_span"),  # NEW: preserve NP span
            }
        )

    # normalize & coalesce simple duplicates (same op+set)
    normalized = []
    seen = set()
    for op in ops:
        key = (
            op["op"],
            tuple(sorted(op.get("triples", []))),
            tuple(sorted(op.get("lhs", []))),
            tuple(sorted(op.get("rhs", []))),
        )
        if key not in seen:
            seen.add(key)
            normalized.append(op)

    return {"ops": normalized, "quant": quant, "scopes": scopes}
