from utils.llm import llm

from prompts.prompts import RECOMMENDATION_PROMPT
from schemas.recommendation import RecommendationOutput


def recommendation_agent(state):

    structured_llm = llm.with_structured_output(RecommendationOutput)

    prompt = RECOMMENDATION_PROMPT.format(

        financial_health_score=state["profile_analysis"].financial_health_score,

        strengths=", ".join(state["profile_analysis"].strengths),

        weaknesses=", ".join(state["profile_analysis"].weaknesses),

        budget_recommendations=", ".join(
            state["budget_plan"].recommendations
        ),

        goal_name=state["goal_plan"].goal_name,

        goal_timeline=state["goal_plan"].estimated_years,

        monthly_saving_required=state["goal_plan"].monthly_saving_required,

        risk_level=state["risk_analysis"].risk_level,

        risk_explanation=state["risk_analysis"].explanation,

        emergency_fund=state["investment_plan"].emergency_fund,

        equity=state["investment_plan"].equity,

        mutual_funds=state["investment_plan"].mutual_funds,

        fixed_deposits=state["investment_plan"].fixed_deposits,

        gold=state["investment_plan"].gold,

        cash=state["investment_plan"].cash
    )

    response = structured_llm.invoke(prompt)

    state["final_recommendation"] = response

    return state