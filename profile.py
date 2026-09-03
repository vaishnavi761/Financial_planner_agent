from typing import List
from pydantic import BaseModel, Field


class ProfileOutput(BaseModel):
    financial_health_score: float = Field(
        description="Overall financial health score out of 10"
    )

    strengths: List[str] = Field(
        description="List of financial strengths"
    )

    weaknesses: List[str] = Field(
        description="List of financial weaknesses"
    )

    summary: str = Field(
        description="Overall financial profile summary"
    )