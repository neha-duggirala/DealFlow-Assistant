from typing import List
from pydantic import BaseModel, Field

class DealAnalysis(BaseModel):
    summary: str = Field(description="A concise summary of the latest communications.")
    fingerprints: List[str] = Field(description="Semantic tags representing deal state (e.g., 'CurrencyRisk', 'RegulatoryHold').")
    risk_level: str = Field(description="Low, Medium, or High risk assessment.")
    recommended_action: str = Field(description="The immediate next step to resolve the bottleneck.")