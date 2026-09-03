from typing import List
from pydantic import BaseModel, Field


class GoalOutput(BaseModel):
    goal_name: str = Field(
        description="Financial goal"
    )

    estimated_years: float = Field(
        description="Estimated years to achieve the goal"
    )

    monthly_saving_required: float = Field(
        description="Monthly savings required"
    )

    action_steps: List[str] = Field(
        description="Action steps to achieve the goal"
    )