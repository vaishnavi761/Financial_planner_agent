from pydantic import BaseModel, Field


class InvestmentOutput(BaseModel):
    emergency_fund: int = Field(
        description="Percentage allocation"
    )

    equity: int = Field(
        description="Percentage allocation"
    )

    mutual_funds: int = Field(
        description="Percentage allocation"
    )

    fixed_deposits: int = Field(
        description="Percentage allocation"
    )

    gold: int = Field(
        description="Percentage allocation"
    )

    cash: int = Field(
        description="Percentage allocation"
    )

    explanation: str = Field(
        description="Reason for this allocation"
    )