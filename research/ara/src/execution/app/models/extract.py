# Grounding: transcribed from oshima/api/app/models/extract.py
from typing import Dict, List, Literal, Optional

from pydantic import BaseModel, Field
import dspy


class Claim(BaseModel):
    claim: str
    explanation: str
    claim_id: str = "C{number}"


class Claims(BaseModel):
    claims: List[Claim]
    acronyms: Optional[Dict[str, str]] = None


class Evidence(BaseModel):
    evidence: str
    explanation: str
    evidence_id: str = "E{number}"
    direction: Literal["support", "contradict", "contextual"]


class ClaimEvidenceGroup(BaseModel):
    claim_id: str
    evidence_list: List[Evidence]


class EvidenceList(BaseModel):
    evidence_groups: List[ClaimEvidenceGroup]
    acronyms: Optional[Dict[str, str]] = None

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
        description="Clear rephrasing with all pronouns resolved to their referents. Keep as close to verbatim as possible. Do not start with 'The authors'."
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
    A claim does not include empirical observations or statistical results.
    It can contain authoritative language, using terms like "demonstrates," "reveals," or "suggests,"
    indicating confidence in the originality or importance of the contribution.
    """

    document: str = dspy.InputField()
    claims: List[ClaimCore] = dspy.OutputField()