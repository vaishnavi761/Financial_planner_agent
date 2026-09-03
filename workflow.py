from langgraph.graph import StateGraph, START, END

from models.state import FinancialState

from agents.profile import profile_agent
from agents.budget import budget_agent
from agents.goal import goal_agent
from agents.risk import risk_agent
from agents.investment import investment_agent
from agents.recommendation import recommendation_agent


# Create the workflow
builder = StateGraph(FinancialState)

builder.add_node("profile_agent", profile_agent)

builder.add_node("budget_agent", budget_agent)

builder.add_node("goal_agent", goal_agent)

builder.add_node("risk_agent", risk_agent)

builder.add_node("investment_agent", investment_agent)

builder.add_node("recommendation_agent", recommendation_agent)

# Connect Nodes
builder.add_edge(START, "profile_agent")

builder.add_edge("profile_agent", "budget_agent")

builder.add_edge("budget_agent", "goal_agent")

builder.add_edge("goal_agent", "risk_agent")

builder.add_edge("risk_agent", "investment_agent")

builder.add_edge("investment_agent", "recommendation_agent")

builder.add_edge("recommendation_agent", END)


graph = builder.compile()