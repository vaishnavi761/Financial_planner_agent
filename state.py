from schemas.profile import ProfileOutput
from schemas.budget import BudgetOutput
from schemas.goal import GoalOutput
from schemas.investment import  InvestmentOutput
from schemas.recommendation import RecommendationOutput
from schemas.risk import RiskOutput


from typing import TypedDict


class FinancialState(TypedDict):
    # User Inputs
    name: str
    age: int
    occupation: str

    monthly_income: float
    monthly_expenses: float
    savings: float

    debt: float
    investment: float

    risk: str
    goal: str
    financial_goal: str

    # Agent Outputs
    profile_analysis: ProfileOutput
    budget_plan: BudgetOutput
    goal_plan: GoalOutput
    investment_plan: InvestmentOutput
    risk_analysis: RiskOutput
    final_recommendation: RecommendationOutput
    
   