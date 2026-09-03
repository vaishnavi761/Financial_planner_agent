from utils.llm import llm
from schemas.profile import ProfileOutput
from prompts.prompts import PROFILE_PROMPT


def profile_agent(state):

    structured_llm = llm.with_structured_output(ProfileOutput)

    prompt = PROFILE_PROMPT.format(
        age=state["age"],
        occupation=state["occupation"],
        monthly_income=state["monthly_income"],
        monthly_expenses=state["monthly_expenses"],
        savings=state["savings"],
        debt=state["debt"],
        investment=state["investment"],
    )

    response = structured_llm.invoke(prompt)

    state["profile_analysis"] = response

    return state