from utils.llm import llm

from prompts.prompts import BUDGET_PROMPT
from schemas.budget import BudgetOutput


def budget_agent(state):

    structured_llm = llm.with_structured_output(BudgetOutput)

    prompt = BUDGET_PROMPT.format(
        monthly_income=state["monthly_income"],
        monthly_expenses=state["monthly_expenses"],
        savings=state["savings"]
    )

    response = structured_llm.invoke(prompt)

    state["budget_plan"] = response

    return state