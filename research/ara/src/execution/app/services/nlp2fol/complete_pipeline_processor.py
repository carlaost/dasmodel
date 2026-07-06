# Grounding: transcribed from oshima/api/app/services/nlp2fol/complete_pipeline_processor.py
#!/usr/bin/env python3
"""
Complete NLP2FOL Pipeline Processor

Integrates all logical pipeline steps to generate complete logical AST from claims/evidence.
This replaces the incomplete ExtractAdapter.process_extract_output() in the storage pipeline.

Usage:
    processor = CompletePipelineProcessor()
    complete_results = processor.process_claims_and_evidence(nlp2fol_input)
"""

import json
import logging
from datetime import datetime
from pathlib import Path
from typing import Any, Dict, List, Optional

from app.services.nlp2fol.composer import compose_formula

# Import the logical pipeline components
from app.services.nlp2fol.logic_feature_detector import detect_features
from app.services.nlp2fol.logic_mapper import map_to_logic

# SUMO pipeline components
from app.services.nlp2fol.ontologies.sumo.s0_resources import load_resources
from app.services.nlp2fol.ontologies.sumo.s1_mention_extractor import extract_mentions
from app.services.nlp2fol.ontologies.sumo.s2_normalizer import normalize_mentions
from app.services.nlp2fol.ontologies.sumo.s3_wn_candidates import find_wn_candidates
from app.services.nlp2fol.ontologies.sumo.s4_sumo_join import join_sumo
from app.services.nlp2fol.ontologies.sumo.s5_ranker import rank_sumo
from app.services.nlp2fol.ontologies.sumo.s6_typing_hints import build_typing_hints
from app.services.nlp2fol.parser import extract_triples
from app.services.nlp2fol.splitter import split
from app.services.nlp2fol.triple_wrapper import add_ids_and_fallback
from app.services.nlp2fol.variable_binder import bind_variables

logger = logging.getLogger(__name__)


class CompletePipelineProcessor:
    """
    Processes claims and evidence through the complete NLP2FOL logical pipeline.
    """

    def __init__(self):
        """Initialize the complete pipeline processor."""
        self.sumo_resources = None
        self.pipeline_stats = {
            "total_processed": 0,
            "successful": 0,
            "failed": 0,
            "fallback_used": 0,
        }
        self._load_sumo_resources()
        logger.info("CompletePipelineProcessor initialized")

    def _load_sumo_resources(self):
        """Load SUMO resources with fallback to stub resources."""
        try:
            self.sumo_resources, is_real = load_resources()
            resource_type = "REAL" if is_real else "STUB"
            logger.info(f"Loaded SUMO resources: {resource_type}")
        except Exception as e:
            logger.warning(f"Failed to load SUMO resources: {e}")
            # Create minimal stub resources
            self.sumo_resources = {
                "ALIASES": {},
                "WN.index": {},
                "SUMO.map": {},
                "meta": {"source": "minimal_stub"},
            }

    def process_claims_and_evidence(
        self, nlp2fol_input: Dict[str, Any]
    ) -> Dict[str, Any]:
        """
        Process claims and evidence through complete logical pipeline.

        Args:
            nlp2fol_input: Output from ExtractAdapter with claims and evidence

        Returns:
            Complete results with logical AST components for all claims/evidence
        """
        logger.info("Starting complete NLP2FOL pipeline processing")

        # Initialize results structure
        results = {
            "document_info": nlp2fol_input.get("document_info", {}),
            "processing_stats": nlp2fol_input.get("processing_stats", {}),
            "acronyms": nlp2fol_input.get("acronyms", {}),
            "nlp2fol_results": [],
            "pipeline_completion_summary": {},
        }

        # Process claims
        claims = nlp2fol_input.get("claims", [])
        for claim in claims:
            try:
                claim_result = self._process_single_item(
                    item_id=claim.get("id", "unknown"),
                    item_type="claim",
                    original_text=claim.get("text", ""),
                    expanded_text=self._expand_acronyms(
                        claim.get("text", ""), nlp2fol_input.get("acronyms", {})
                    ),
                )
                results["nlp2fol_results"].append(claim_result)
                self.pipeline_stats["successful"] += 1
            except Exception as e:
                logger.error(
                    f"Failed to process claim {claim.get('id', 'unknown')}: {e}"
                )
                # Add failed item with error info
                failed_result = {
                    "id": claim.get("id", "unknown"),
                    "type": "claim",
                    "original_text": claim.get("text", ""),
                    "pipeline_error": str(e),
                    "status": "failed",
                }
                results["nlp2fol_results"].append(failed_result)
                self.pipeline_stats["failed"] += 1

            self.pipeline_stats["total_processed"] += 1

        # Process evidence
        evidence = nlp2fol_input.get("evidence", [])
        for evidence_item in evidence:
            try:
                evidence_result = self._process_single_item(
                    item_id=evidence_item.get("id", "unknown"),
                    item_type="evidence",
                    original_text=evidence_item.get("text", ""),
                    expanded_text=self._expand_acronyms(
                        evidence_item.get("text", ""), nlp2fol_input.get("acronyms", {})
                    ),
                )
                results["nlp2fol_results"].append(evidence_result)
                self.pipeline_stats["successful"] += 1
            except Exception as e:
                logger.error(
                    f"Failed to process evidence {evidence_item.get('id', 'unknown')}: {e}"
                )
                # Add failed item with error info
                failed_result = {
                    "id": evidence_item.get("id", "unknown"),
                    "type": "evidence",
                    "original_text": evidence_item.get("text", ""),
                    "pipeline_error": str(e),
                    "status": "failed",
                }
                results["nlp2fol_results"].append(failed_result)
                self.pipeline_stats["failed"] += 1

            self.pipeline_stats["total_processed"] += 1

        # Update summary statistics
        self._update_completion_summary(results)

        logger.info(
            f"Complete pipeline processing finished: {self.pipeline_stats['successful']}/{self.pipeline_stats['total_processed']} successful"
        )

        return results

    def _process_single_item(
        self, item_id: str, item_type: str, original_text: str, expanded_text: str
    ) -> Dict[str, Any]:
        """
        Process a single claim or evidence item through the complete logical pipeline.

        Args:
            item_id: Unique identifier
            item_type: "claim" or "evidence"
            original_text: Original text
            expanded_text: Text with acronyms expanded

        Returns:
            Complete logical processing results
        """
        processing_text = expanded_text

        try:
            # Step 1: Triple extraction (CoreNLP/OpenIE)
            logger.debug(f"Step 1: Extracting triples for {item_id}")
            raw_triples, deps = extract_triples(processing_text)

            # Step 2: ID assignment and fallback
            logger.debug(f"Step 2: ID assignment for {item_id}")
            triples_with_ids = add_ids_and_fallback(raw_triples, deps, processing_text)

            # Step 3: Coordination splitting
            logger.debug(f"Step 3: Coordination splitting for {item_id}")
            atomic_triples = split(triples_with_ids)

            # Add IDs to triples if not present
            for i, triple in enumerate(atomic_triples):
                if "id" not in triple:
                    triple["id"] = f"T{i+1}"
                    triple["sentence"] = processing_text

            # Step 4: Logical feature detection
            logger.debug(f"Step 4: Logical feature detection for {item_id}")
            try:
                features = detect_features(
                    sentence=processing_text, triples=atomic_triples, deps=deps
                )
            except Exception as e:
                logger.warning(
                    f"Feature detection failed for {item_id}, using minimal features: {e}"
                )
                features = {
                    "sentence": processing_text,
                    "triples": atomic_triples,
                    "operator_cues": [],
                    "implication_cues": [],
                    "quantifier_cues": [],
                }
                self.pipeline_stats["fallback_used"] += 1

            # Step 5: Logic mapping
            logger.debug(f"Step 5: Logic mapping for {item_id}")
            try:
                logic_plan = map_to_logic(features)
            except Exception as e:
                logger.warning(
                    f"Logic mapping failed for {item_id}, using minimal plan: {e}"
                )
                logic_plan = {
                    "ops": [],
                    "quant": [],
                    "scopes": {t["id"]: "null" for t in atomic_triples},
                }
                self.pipeline_stats["fallback_used"] += 1

            # Step 6: SUMO pipeline
            logger.debug(f"Step 6: SUMO pipeline for {item_id}")
            sumo_results = self._run_sumo_pipeline(features)

            # Step 7: Variable binding
            logger.debug(f"Step 7: Variable binding for {item_id}")
            binding_input = {
                "sentence": processing_text,
                "triples": atomic_triples,
                "dependencies": deps,
                "logic": logic_plan,
                "sumo": sumo_results,
            }

            try:
                variable_binding = bind_variables(binding_input)
            except Exception as e:
                logger.warning(
                    f"Variable binding failed for {item_id}, using minimal binding: {e}"
                )
                variable_binding = {
                    "vars": {},
                    "triples_ir": [],
                    "ops": logic_plan.get("ops", []),
                    "quant": logic_plan.get("quant", []),
                    "scopes": logic_plan.get("scopes", {}),
                    "notes": [f"Variable binding failed: {e}"],
                    "stats": {
                        "sumo_mapped": 0,
                        "raw_fallback": len(atomic_triples),
                        "generic_roles_used": False,
                    },
                }
                self.pipeline_stats["fallback_used"] += 1

            # Step 8: Logical AST composition
            logger.debug(f"Step 8: AST composition for {item_id}")
            try:
                logical_ast = compose_formula(variable_binding)
            except Exception as e:
                logger.warning(
                    f"AST composition failed for {item_id}, using minimal AST: {e}"
                )
                logical_ast = {
                    "ast": {"type": "true"},
                    "free_vars": [],
                    "var_table": {},
                    "debug": {
                        "warnings": [f"Composition failed: {e}"],
                        "type_placements": {},
                    },
                }
                self.pipeline_stats["fallback_used"] += 1

            # Compile complete result
            result = {
                "id": item_id,
                "type": item_type,
                "original_text": original_text,
                "expanded_text": expanded_text,
                "processing_text": processing_text,
                "raw_triples": raw_triples,
                "dependencies": deps,
                "triples_with_ids": triples_with_ids,
                "atomic_triples": atomic_triples,
                "logical_features": features,
                "logic_plan": logic_plan,
                "sumo_mappings": sumo_results,
                "variable_binding": variable_binding,
                "logical_ast": logical_ast,
                "pipeline_stats": {
                    "raw_triples_count": len(raw_triples),
                    "final_triples_count": len(atomic_triples),
                    "dependencies_count": len(deps) if deps else 0,
                    "features_detected": len(features.get("operator_cues", []))
                    + len(features.get("implication_cues", []))
                    + len(features.get("quantifier_cues", [])),
                    "logic_operations": len(logic_plan.get("ops", [])),
                    "quantifiers": len(logic_plan.get("quant", [])),
                    "sumo_mappings": len(sumo_results.get("sumo_tags", [])),
                    "bound_variables": len(variable_binding.get("vars", {})),
                    "ast_complexity": self._calculate_ast_complexity(
                        logical_ast.get("ast", {})
                    ),
                },
                "status": "completed",
            }

            return result

        except Exception as e:
            logger.error(f"Complete pipeline failed for {item_id}: {e}")
            # Return minimal result with error
            return {
                "id": item_id,
                "type": item_type,
                "original_text": original_text,
                "expanded_text": expanded_text,
                "pipeline_error": str(e),
                "status": "failed",
                "raw_triples": [],
                "dependencies": [],
                "pipeline_stats": {
                    "raw_triples_count": 0,
                    "final_triples_count": 0,
                    "dependencies_count": 0,
                },
            }

    def _run_sumo_pipeline(self, features: Dict[str, Any]) -> Dict[str, Any]:
        """Run the complete SUMO pipeline."""
        try:
            # S1: Extract mentions
            s1_result = extract_mentions(features)

            # S2: Normalize mentions
            s2_input = {
                "mentions": s1_result["mentions"],
                "ALIASES": self.sumo_resources.get("ALIASES", {}),
            }
            s2_result = normalize_mentions(s2_input)

            # S3: Find WordNet candidates
            s3_input = {
                "norm_mentions": s2_result["norm_mentions"],
                "WN.index": self.sumo_resources.get("WN.index", {}),
            }
            s3_result = find_wn_candidates(s3_input)

            # S4: Join SUMO
            s4_input = {
                "wn_candidates": s3_result["wn_candidates"],
                "SUMO.map": self.sumo_resources.get("SUMO.map", {}),
            }
            s4_result = join_sumo(s4_input)

            # S5: Rank SUMO
            s5_input = {
                "sumo_candidates": s4_result["sumo_candidates"],
                "mentions": s1_result["mentions"],
                "norm_mentions": s2_result["norm_mentions"],
                "thresholds": {"min_score": 0.0, "top_k": 3},
            }
            s5_result = rank_sumo(s5_input)

            # S6: Build typing hints
            s6_result = build_typing_hints(s5_result)

            return {
                "sumo_tags": s5_result.get("sumo_tags", []),
                "typing_hints": s6_result.get("typing_hints", []),
                "mentions": s1_result.get("mentions", []),
                "norm_mentions": s2_result.get("norm_mentions", []),
                "pipeline_stats": {
                    "mentions_extracted": len(s1_result.get("mentions", [])),
                    "normalized": len(s2_result.get("norm_mentions", [])),
                    "wn_candidates": len(s3_result.get("wn_candidates", [])),
                    "sumo_candidates": len(s4_result.get("sumo_candidates", [])),
                    "final_tags": len(s5_result.get("sumo_tags", [])),
                    "typing_hints": len(s6_result.get("typing_hints", [])),
                },
            }

        except Exception as e:
            logger.warning(f"SUMO pipeline failed: {e}")
            self.pipeline_stats["fallback_used"] += 1
            return {
                "sumo_tags": [],
                "typing_hints": [],
                "mentions": [],
                "norm_mentions": [],
                "pipeline_stats": {"error": str(e)},
            }

    def _expand_acronyms(self, text: str, acronyms: Dict[str, str]) -> str:
        """Expand acronyms in text using the acronym dictionary."""
        expanded_text = text

        for acronym, expansion in acronyms.items():
            import re

            pattern = r"\b" + re.escape(acronym) + r"\b"
            replacement = f"{acronym} ({expansion})"
            expanded_text = re.sub(pattern, replacement, expanded_text)

        return expanded_text

    def _calculate_ast_complexity(self, ast: Dict[str, Any]) -> int:
        """Calculate a simple complexity metric for the AST."""
        if not isinstance(ast, dict):
            return 0

        complexity = 1  # Base complexity

        # Add complexity for different node types
        node_type = ast.get("type", "")
        if node_type in ["and", "or"]:
            complexity += len(ast.get("args", []))
            for arg in ast.get("args", []):
                complexity += self._calculate_ast_complexity(arg)
        elif node_type in ["forall", "exists"]:
            complexity += len(ast.get("vars", []))
            complexity += self._calculate_ast_complexity(ast.get("body", {}))
        elif node_type in ["not", "impl"]:
            complexity += self._calculate_ast_complexity(
                ast.get("arg", ast.get("lhs", {}))
            )
            complexity += self._calculate_ast_complexity(ast.get("rhs", {}))
        elif node_type == "atom":
            complexity += len(ast.get("args", []))

        return complexity

    def _update_completion_summary(self, results: Dict[str, Any]):
        """Update the pipeline completion summary."""
        nlp2fol_results = results.get("nlp2fol_results", [])

        completed_count = sum(
            1 for item in nlp2fol_results if item.get("status") == "completed"
        )
        failed_count = sum(
            1 for item in nlp2fol_results if item.get("status") == "failed"
        )

        total_features = sum(
            item.get("pipeline_stats", {}).get("features_detected", 0)
            for item in nlp2fol_results
            if item.get("status") == "completed"
        )

        total_operations = sum(
            item.get("pipeline_stats", {}).get("logic_operations", 0)
            for item in nlp2fol_results
            if item.get("status") == "completed"
        )

        total_variables = sum(
            item.get("pipeline_stats", {}).get("bound_variables", 0)
            for item in nlp2fol_results
            if item.get("status") == "completed"
        )

        # Add completion statistics
        results["pipeline_completion_summary"] = {
            "total_items": len(nlp2fol_results),
            "successfully_completed": completed_count,
            "failed": failed_count,
            "completion_rate": (
                completed_count / len(nlp2fol_results) if nlp2fol_results else 0
            ),
            "total_logical_features": total_features,
            "total_logic_operations": total_operations,
            "total_bound_variables": total_variables,
            "fallback_usage": self.pipeline_stats["fallback_used"],
            "pipeline_components_added": [
                "logical_features",
                "logic_plan",
                "sumo_mappings",
                "variable_binding",
                "logical_ast",
            ],
        }

    def get_pipeline_stats(self) -> Dict[str, Any]:
        """Get current pipeline processing statistics."""
        return self.pipeline_stats.copy()
