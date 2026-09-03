PROFILE_PROMPT = """
You are a certified financial analyst.

Analyze the user's financial profile.

Age: {age}
Occupation: {occupation}

Monthly Income: ₹{monthly_income}
Monthly Expenses: ₹{monthly_expenses}

Savings: ₹{savings}
Debt: ₹{debt}
Investments: ₹{investment}

Return the response according to the ProfileOutput schema.
"""

BUDGET_PROMPT = """
You are a Personal Budget Planner.

Create a realistic monthly budget for the user.

User Details:
---------------
Monthly Income: ₹{monthly_income}
Monthly Expenses: ₹{monthly_expenses}
Current Savings: ₹{savings}

Instructions:
1. Calculate recommended monthly savings.
2. Suggest an emergency fund target.
3. Provide practical recommendations to improve budgeting.
4. Keep recommendations realistic.

Return the response according to the BudgetOutput schema only.
"""

GOAL_PROMPT = """
You are a Financial Goal Planning Expert.

Create a roadmap for achieving the user's financial goal.

User Details:
---------------
Age: {age}
Monthly Income: ₹{monthly_income}
Current Savings: ₹{savings}

Goal:
{goal}

Goal Description:
{financial_goal}

Instructions:
1. Identify the financial goal.
2. Estimate the timeline.
3. Estimate monthly savings required.
4. Generate clear action steps.

Return the response according to the GoalOutput schema only.
"""

RISK_PROMPT = """
You are an Investment Risk Assessment Expert.

Evaluate the user's investment risk profile.

User Details:
---------------
Age: {age}
Monthly Income: ₹{monthly_income}
Current Savings: ₹{savings}
Outstanding Debt: ₹{debt}
Selected Risk Preference: {risk}

Instructions:
1. Determine the risk level.
2. Explain why.
3. List investment precautions.

Return the response according to the RiskOutput schema only.
"""

INVESTMENT_PROMPT = """
You are a Certified Investment Advisor.

Suggest an ideal investment allocation.

User Details:
---------------
Age: {age}
Monthly Income: ₹{monthly_income}
Current Savings: ₹{savings}
Outstanding Debt: ₹{debt}

Financial Goal:
{goal}

Risk Level:
{risk_level}

Instructions:
1. Recommend percentage allocation for:
   - Emergency Fund
   - Equity
   - Mutual Funds
   - Fixed Deposits
   - Gold
   - Cash
2. The total allocation must equal exactly 100%.
3. Explain why this allocation is suitable.

Return the response according to the InvestmentOutput schema only.
"""

RECOMMENDATION_PROMPT = """
You are a Senior Certified Financial Advisor.

Prepare a final personalized financial plan by combining all previous analyses.

Profile Summary:
----------------
Health Score: {financial_health_score}
Strengths: {strengths}
Weaknesses: {weaknesses}

Budget Recommendations:
-----------------------
{budget_recommendations}

Goal:
------
Goal Name: {goal_name}
Timeline: {goal_timeline}
Monthly Saving Required: ₹{monthly_saving_required}

Risk Assessment:
----------------
Risk Level: {risk_level}
Explanation: {risk_explanation}

Investment Allocation:
----------------------
Emergency Fund: {emergency_fund}%
Equity: {equity}%
Mutual Funds: {mutual_funds}%
Fixed Deposits: {fixed_deposits}%
Gold: {gold}%
Cash: {cash}%

Instructions:
1. Give an overall financial score.
2. List top financial priorities.
3. Provide investment advice.
4. Provide budgeting advice.
5. Create a practical five-year roadmap.
6. End with an encouraging message.

Return the response according to the RecommendationOutput schema only.
"""
