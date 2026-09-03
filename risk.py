from utils.llm import llm

from prompts.prompts import RISK_PROMPT
from schemas.risk import RiskOutput


def risk_agent(state):

    structured_llm = llm.with_structured_output(RiskOutput)

    prompt = RISK_PROMPT.format(
        age=state["age"],
        monthly_income=state["monthly_income"],
        savings=state["savings"],
        debt=state["debt"],
        risk=state["risk"]
    )

    response = structured_llm.invoke(prompt)

    state["risk_analysis"] = response

    return state