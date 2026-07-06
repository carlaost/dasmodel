# Grounding: transcribed from oshima/api/app/services/extract/dspy_claims_extractor.py
"""
DSPy-based Claims Extraction Module

This module extracts original scientific claims from research papers using DSPy signatures
and structured LLM outputs. It provides a clean, modular interface for claim extraction
that can replace the OpenAI-based extraction in extract_paper.py.

INPUT:
    - document: str (full paper text content)
    - Optional: paper metadata (title, field, topic) for context

OUTPUT:
    {
        "claims": [
            {
                "verbatim_statement": str,      # Word-for-word extracted claim
                "rephrased_statement": str,     # Clarified version with pronouns resolved
                "original": bool,               # True if original to this paper, False if citing others
                "confidence": float,            # 0-1: How confident the claim is original
                "centrality_percentage": float  # 0-100: How central to paper's main thesis
            }
        ]
    }

DEPENDENCIES:
    - dspy: For signatures and structured prediction
    - Caller must configure dspy.settings.configure() before using this module

USAGE:
    import dspy
    dspy.settings.configure(lm=your_language_model)

    extractor = DspyClaimsExtractor()
    result = extractor.extract_claims(document_text)
"""

from typing import List, Optional

import dspy

# ------------------------------------------------------------
# TYPE DEFINITIONS
# ------------------------------------------------------------


class ClaimOutput:
    """Type definition for a single extracted claim."""

    verbatim_statement: str
    rephrased_statement: str
    original: bool
    confidence: float
    centrality_percentage: float


class ClaimsExtractionResult:
    """Type definition for the complete extraction result."""

    claims: List[ClaimOutput]


# ------------------------------------------------------------
# DSPY SIGNATURES
# ------------------------------------------------------------


class ExtractCore(dspy.Signature):
    """
    Base extraction for verbatim and rephrased content and originality analysis.
    Statements are only original if this paper is the first time they are made.
    Statements are not original if they are derived out of previous literature or studies,
    or if they include some form of citation or reference to other work
    (the citation format depends on the field but you'll understand from context).
    """

    verbatim_statement: str = dspy.OutputField(
        description="The word-for-word statement extracted from the document."
    )
    rephrased_statement: str = dspy.OutputField(
        description="""
            Clear rephrasing of the claim with all pronouns resolved to their referents.
            This statement can be taken out of context and understood independently, 
            while still accurately representing the word-for-word claim being made by the authors in the source text.
            Words like 'this' and 'it' are replaced with what the auhtors mean by them.
            If the paper introduces something, use the name they have for it instead of general terms like 'system' when talking about it specifically.
            Never say 'the authors' or 'this paper' or 'these findings' -- state the claim being made on a general level.
            Be careful not to overstate confidence in a claim: Match exactly the confidence the authors have.
            """
    )
    original: bool = dspy.OutputField(
        description="True if this is an original statement by the authors' in this paper, False if citing others or restating previous literature or studies."
    )


class ClaimCore(ExtractCore):
    """Original scientific claim or hypothesis from the authors."""

    confidence: float = dspy.OutputField(
        description="Confidence that the authors would agree that this is an original claim of their paper at hand (0-1)."
    )
    centrality_percentage: float = dspy.OutputField(
        description="How central this claim is to the paper's main thesis (0-100). Higher if claim's content is mentioned in title or abstract of the paper."
    )


class ExtractClaims(dspy.Signature):
    """
    Extract all original scientific claims from the document.
    A claim is an original, novel insight presented in a paper that contributes new knowledge,
    perspective, or understanding to the field. Claims are conclusive and interpretive.
    Claims are falsifiable. Hypotheses are subsets of claims, they are just unproven so far.
    A claim does not include empirical observations or statistical results.
    It can contain authoritative language, using terms like "demonstrates," "reveals," or "suggests,"
    indicating confidence in the originality or importance of the contribution.

    A paper will often make the same claim multiple times in different section (often abstract and conclusion will say similar things).
    Keep only the most comprehensive statement of the claim, and drop any duplicates. Return only the main claims of the papers.

    A given paper will usually have one core claim and perhaps 1-2 more adjacent ones, 5 if it’s a really big study.
    If you end up with more than 5 claims for your response, think again, and see which ones you could drop.
    Only keep a claim if without it, the list of claims would not be representative of what people will view as
    the contributions this paper makes to the literature.

    Note that we will extract evidence for these claims later on, so you can ignore anything that would be more evidence than claim,
    meaning anything that reports an empirical observation that can be used to substantiate a claim made in this paper.

    A good claim would be:
    - "Insomnia is a significant problem among euthymic patients with bipolar disorder."
        -> Makes an assertion about the nature of a phenomenon. Does not report any specific observation; is a general statement of proposed truth.
    - "Sleep has a critical mood regulatory function, and sleep deprivation involves the loss of top-down inhibitory control usually exerted by medial prefrontal cortex on amygdala."
        -> Makes an assertion about how something works, is a general statement of proposed truth. Requires proof to be believed but is falsifiable and thus scientific.



    These are not claims:
    - "Seventy percent of euthymic patients with bipolar disorder exhibited a clinically significant sleep disturbance."
        -> Reports a finding but makes no assertion/conclusion/interpretation. This is evidence.
    - "Among individuals with bipolar disorder treated with best practice mood stabilizers in the STEP-BD study, 66% still experienced significant sleep disturbance."
        -> Reports a finding but makes no assertion/conclusion/interpretation. This is evidence.
    """

    document: str = dspy.InputField()
    claims: List[ClaimCore] = dspy.OutputField()


# ------------------------------------------------------------
# EXTRACTOR CLASS
# ------------------------------------------------------------


class DspyClaimsExtractor:
    """
    Clean claims extraction using DSPy signatures.

    This extractor uses structured DSPy signatures to extract original scientific claims
    from research paper text. It does not handle model configuration - the caller must
    configure dspy.settings before instantiating this class.
    """

    def __init__(self):
        """
        Initialize the claims extractor.

        Note: Caller must configure dspy.settings.configure() before instantiation.
        """
        self.predictor = dspy.Predict(ExtractClaims)

    def extract_claims(self, document: str) -> dict:
        """
        Extract claims from document text.

        Args:
            document: Full paper text content

        Returns:
            Dictionary with structure:
            {
                "claims": [
                    {
                        "verbatim_statement": str,
                        "rephrased_statement": str,
                        "original": bool,
                        "confidence": float,
                        "centrality_percentage": float
                    }
                ]
            }
        """
        result = self.predictor(document=document)

        # Convert DSPy result to dict format
        claims_list = []
        if hasattr(result, "claims"):
            for claim in result.claims:
                claim_dict = {
                    "verbatim_statement": getattr(claim, "verbatim_statement", ""),
                    "rephrased_statement": getattr(claim, "rephrased_statement", ""),
                    "original": getattr(claim, "original", False),
                    "confidence": getattr(claim, "confidence", 0.0),
                    "centrality_percentage": getattr(
                        claim, "centrality_percentage", 0.0
                    ),
                }
                claims_list.append(claim_dict)

        return {"claims": claims_list}

    def extract_claims_with_context(
        self,
        document: str,
        title: Optional[str] = None,
        field: Optional[str] = None,
        topic: Optional[str] = None,
    ) -> dict:
        """
        Extract claims with additional paper context.

        Args:
            document: Full paper text content
            title: Paper title (optional, added to document context)
            field: Research field (optional, e.g., "machine learning")
            topic: Specific topic (optional, e.g., "neural networks")

        Returns:
            Same format as extract_claims()
        """
        # Build enhanced document with context
        context_parts = []

        if title:
            context_parts.append(f"Title: {title}")
        if field:
            context_parts.append(f"Research Field: {field}")
        if topic:
            context_parts.append(f"Topic: {topic}")

        if context_parts:
            context_header = "\n".join(context_parts)
            enhanced_document = f"{context_header}\n\n{document}"
        else:
            enhanced_document = document

        return self.extract_claims(enhanced_document)


# ------------------------------------------------------------
# UTILITY FUNCTIONS
# ------------------------------------------------------------


def parse_document_from_json(parsed_data: dict) -> str:
    """
    Parse document text from JSON structure (Adobe Extract API format).

    Args:
        parsed_data: Dictionary with "elements" key containing text elements

    Returns:
        Concatenated document text
    """
    document_text = ""
    if "elements" in parsed_data:
        for element in parsed_data["elements"]:
            if element.get("Text"):
                document_text += element["Text"] + "\n"
    return document_text
