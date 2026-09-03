from utils.llm import llm

from prompts.prompts import INVESTMENT_PROMPT
from schemas.investment import InvestmentOutput


def investment_agent(state):

    structured_llm = llm.with_structured_output(InvestmentOutput)

    prompt = INVESTMENT_PROMPT.format(
        age=state["age"],
        monthly_income=state["monthly_income"],
        savings=state["savings"],
        debt=state["debt"],
        goal=state["goal"],
        risk_level=state["risk_analysis"].risk_level
    )

    response = structured_llm.invoke(prompt)

    state["investment_plan"] = response

    return state