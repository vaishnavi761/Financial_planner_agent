from typing import List
from pydantic import BaseModel, Field


class RecommendationOutput(BaseModel):
    financial_score: float = Field(
        description="Overall financial score out of 10"
    )

    top_priorities: List[str] = Field(
        description="Top financial priorities"
    )

    investment_advice: List[str] = Field(
        description="Investment recommendations"
    )

    budget_advice: List[str] = Field(
        description="Budget recommendations"
    )

    five_year_roadmap: List[str] = Field(
        description="Five-year financial roadmap"
    )

    final_message: str = Field(
        description="Motivational message"
    )