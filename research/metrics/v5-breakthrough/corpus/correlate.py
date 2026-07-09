#!/usr/bin/env python3
"""Join the metric's significance score with the blind expert-panel breakthrough scores and
measure how well the metric tracks expert judgement on recent papers. No LLM calls — reads the
completed expert-panel workflow result + corpus_scored.json. Papers missing either side are
listed, not silently dropped.
"""
import json
import os

HERE = os.path.dirname(os.path.abspath(__file__))
PANEL = "/private/tmp/claude-501/-Users-carlaostmann-code-dasmodel/5417ea35-0ea7-4fac-96ea-536bdcb259ba/tasks/wvi1w1ro5.output"


def median(xs):
    xs = sorted(xs)
    n = len(xs)
    if not n:
        return None
    return xs[n // 2] if n % 2 else (xs[n // 2 - 1] + xs[n // 2]) / 2


def spearman(pairs):
    # rank-transform each side, then Pearson on ranks
    def ranks(vals):
        order = sorted(range(len(vals)), key=lambda i: vals[i])
        r = [0.0] * len(vals)
        i = 0
        while i < len(vals):
            j = i
            while j + 1 < len(vals) and vals[order[j + 1]] == vals[order[i]]:
                j += 1
            avg = (i + j) / 2.0 + 1
            for k in range(i, j + 1):
                r[order[k]] = avg
            i = j + 1
        return r
    xs = [p[0] for p in pairs]
    ys = [p[1] for p in pairs]
    rx, ry = ranks(xs), ranks(ys)
    n = len(pairs)
    mx, my = sum(rx) / n, sum(ry) / n
    cov = sum((rx[i] - mx) * (ry[i] - my) for i in range(n))
    sx = sum((rx[i] - mx) ** 2 for i in range(n)) ** 0.5
    sy = sum((ry[i] - my) ** 2 for i in range(n)) ** 0.5
    return cov / (sx * sy) if sx and sy else 0.0


def main():
    stable = os.path.join(HERE, "expert_scores.json")
    if os.path.exists(stable):
        expert = {k: {"expert_median": float(v), "n_judges": 3, "spread": 0}
                  for k, v in json.load(open(stable)).items()}
    else:
        raw = json.load(open(PANEL))
        res = raw.get("result", raw)
        if isinstance(res, str):
            res = json.loads(res)
        panel = res["expert"]
        expert = {}
        for row in panel:
            scores = [v["breakthrough_score"] for v in row.get("votes", []) if "breakthrough_score" in v]
            if scores:
                expert[row["slug"]] = {"expert_median": median(scores), "n_judges": len(scores),
                                       "spread": max(scores) - min(scores)}

    metric = {r["slug"]: r for r in json.load(open(os.path.join(HERE, "corpus_scored.json")))}

    joined = []
    for slug, m in metric.items():
        if slug in expert:
            joined.append({"slug": slug, "significance": m["significance"],
                           "expert": expert[slug]["expert_median"],
                           "spread": expert[slug]["spread"]})
    joined.sort(key=lambda x: -x["expert"])

    missing_expert = sorted(set(metric) - set(expert))
    pairs = [(j["significance"], j["expert"]) for j in joined]
    rho = spearman(pairs)

    print(f"papers with BOTH metric + expert score: {len(joined)}  "
          f"(missing expert: {len(missing_expert)} tail papers not yet judged)")
    print(f"\nSpearman rank correlation (significance vs expert breakthrough): {rho:.3f}\n")
    print("%-52s %5s %7s %s" % ("paper", "SIG", "expert", "spread"))
    print("-" * 74)
    for j in joined:
        print("%-52s %5.3f %7.1f  %d" % (j["slug"][:52], j["significance"], j["expert"], j["spread"]))
    if missing_expert:
        print("\nnot yet judged (panel hit session limit):", ", ".join(s[:18] for s in missing_expert))

    out = {"n_joined": len(joined), "spearman": round(rho, 4),
           "rows": joined, "missing_expert": missing_expert}
    with open(os.path.join(HERE, "metric_vs_expert.json"), "w") as f:
        json.dump(out, f, indent=2)


if __name__ == "__main__":
    main()
