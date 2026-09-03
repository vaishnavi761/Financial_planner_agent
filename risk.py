from typing import List
from pydantic import BaseModel, Field


class RiskOutput(BaseModel):
    risk_level: str = Field(
        description="Low, Moderate, or High"
    )

    explanation: str = Field(
        description="Reason for assigned risk level"
    )

    precautions: List[str] = Field(
        description="Investment precautions"
    )