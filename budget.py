from typing import List
from pydantic import BaseModel, Field


class BudgetOutput(BaseModel):
    monthly_income: float = Field(
        description="Monthly income"
    )

    monthly_expenses: float = Field(
        description="Monthly expenses"
    )

    recommended_monthly_savings: float = Field(
        description="Recommended monthly savings amount"
    )

    emergency_fund_target: float = Field(
        description="Target emergency fund amount"
    )

    recommendations: List[str] = Field(
        description="Budget improvement recommendations"
    )