from utils.llm import llm

from prompts.prompts import GOAL_PROMPT
from schemas.goal import GoalOutput


def goal_agent(state):

    structured_llm = llm.with_structured_output(GoalOutput)

    prompt = GOAL_PROMPT.format(
        age=state["age"],
        monthly_income=state["monthly_income"],
        savings=state["savings"],
        goal=state["goal"],
        financial_goal=state["financial_goal"]
    )

    response = structured_llm.invoke(prompt)

    state["goal_plan"] = response

    return state