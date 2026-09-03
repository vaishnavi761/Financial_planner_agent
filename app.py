import streamlit as st
from graph.workflow import graph


# ============================================================
# PAGE CONFIG
# ============================================================

st.set_page_config(
    page_title="Financial Life Planner AI",
    page_icon="💰",
    layout="wide",
    initial_sidebar_state="expanded"
)


# ============================================================
# CUSTOM THEME / CSS
# ============================================================

st.markdown(
    """
    <style>

    /* ========================================================
       GLOBAL
       ======================================================== */

    html,
    body,
    [data-testid="stAppViewContainer"],
    [data-testid="stApp"] {
        background-color: #f8fafc !important;
    }

    [data-testid="stAppViewContainer"] {
        background-color: #f8fafc !important;
    }

    .main {
        background-color: #f8fafc !important;
    }

    .block-container {
        max-width: 1400px;
        padding-top: 2rem;
        padding-bottom: 3rem;
        padding-left: 3rem;
        padding-right: 3rem;
    }


    /* ========================================================
       ALL TEXT
       ======================================================== */

    h1 {
        color: #172554 !important;
        font-weight: 800 !important;
    }

    h2,
    h3,
    h4,
    h5,
    h6 {
        color: #1e293b !important;
        font-weight: 700 !important;
    }

    p {
        color: #334155 !important;
    }

    label {
        color: #172033 !important;
        font-weight: 600 !important;
    }

    small {
        color: #64748b !important;
    }


    /* ========================================================
       SIDEBAR
       ======================================================== */

    [data-testid="stSidebar"] {
        background-color: #172554 !important;
        border-right: 1px solid #1e3a8a !important;
    }

    [data-testid="stSidebar"] * {
        color: #ffffff !important;
    }

    [data-testid="stSidebar"] p {
        color: #dbeafe !important;
    }

    [data-testid="stSidebar"] h1,
    [data-testid="stSidebar"] h2,
    [data-testid="stSidebar"] h3 {
        color: #ffffff !important;
    }

    [data-testid="stSidebar"] hr {
        border-top: 1px solid rgba(255, 255, 255, 0.25) !important;
    }


    /* ========================================================
       TEXT INPUT
       ======================================================== */

    div[data-testid="stTextInput"] input {
        background-color: #ffffff !important;
        color: #172033 !important;
        border: 1px solid #94a3b8 !important;
        border-radius: 8px !important;
        caret-color: #2563eb !important;
    }

    div[data-testid="stTextInput"] input::placeholder {
        color: #64748b !important;
        opacity: 1 !important;
    }

    div[data-testid="stTextInput"] input:focus {
        background-color: #ffffff !important;
        color: #172033 !important;
        border: 2px solid #2563eb !important;
        box-shadow: 0 0 0 2px #dbeafe !important;
    }


    /* ========================================================
       NUMBER INPUT
       ======================================================== */

    div[data-testid="stNumberInput"] {
        background-color: transparent !important;
    }

    div[data-testid="stNumberInput"] input {
        background-color: #ffffff !important;
        color: #172033 !important;
        border: 1px solid #94a3b8 !important;
        caret-color: #2563eb !important;
    }

    div[data-testid="stNumberInput"] button {
        background-color: #f8fafc !important;
        color: #172033 !important;
        border-left: 1px solid #cbd5e1 !important;
    }

    div[data-testid="stNumberInput"] button:hover {
        background-color: #dbeafe !important;
        color: #1d4ed8 !important;
    }


    /* ========================================================
       TEXT AREA
       ======================================================== */

    div[data-testid="stTextArea"] textarea {
        background-color: #ffffff !important;
        color: #172033 !important;
        border: 1px solid #94a3b8 !important;
        border-radius: 8px !important;
        caret-color: #2563eb !important;
    }

    div[data-testid="stTextArea"] textarea::placeholder {
        color: #64748b !important;
        opacity: 1 !important;
    }

    div[data-testid="stTextArea"] textarea:focus {
        background-color: #ffffff !important;
        color: #172033 !important;
        border: 2px solid #2563eb !important;
        box-shadow: 0 0 0 2px #dbeafe !important;
    }


    /* ========================================================
       SELECTBOX
       ======================================================== */

    div[data-testid="stSelectbox"] div[data-baseweb="select"] > div {
        background-color: #ffffff !important;
        color: #172033 !important;
        border: 1px solid #94a3b8 !important;
        border-radius: 8px !important;
    }

    div[data-testid="stSelectbox"] div[data-baseweb="select"] span {
        color: #172033 !important;
    }

    div[data-testid="stSelectbox"] svg {
        fill: #172033 !important;
    }


    /* ========================================================
       SELECTBOX DROPDOWN
       ======================================================== */

    div[data-baseweb="popover"] {
        background-color: #ffffff !important;
    }

    div[data-baseweb="menu"] {
        background-color: #ffffff !important;
    }

    div[role="option"] {
        background-color: #ffffff !important;
        color: #172033 !important;
    }

    div[role="option"]:hover {
        background-color: #dbeafe !important;
        color: #172033 !important;
    }

    div[role="option"][aria-selected="true"] {
        background-color: #bfdbfe !important;
        color: #172033 !important;
    }


    /* ========================================================
       BUTTON
       ======================================================== */

    div.stButton > button {
        background-color: #2563eb !important;
        color: #ffffff !important;
        border: none !important;
        border-radius: 10px !important;
        height: 52px !important;
        font-size: 17px !important;
        font-weight: 700 !important;
        width: 100% !important;

        box-shadow:
            0 4px 10px rgba(37, 99, 235, 0.20) !important;
    }

    div.stButton > button p {
        color: #ffffff !important;
    }

    div.stButton > button:hover {
        background-color: #1d4ed8 !important;
        color: #ffffff !important;

        box-shadow:
            0 6px 15px rgba(37, 99, 235, 0.30) !important;
    }

    div.stButton > button:active {
        background-color: #1e40af !important;
    }


    /* ========================================================
       METRIC CARDS
       ======================================================== */

    div[data-testid="stMetric"] {
        background-color: #ffffff !important;

        border: 1px solid #cbd5e1 !important;

        border-radius: 12px !important;

        padding: 18px !important;

        box-shadow:
            0 3px 8px rgba(15, 23, 42, 0.06) !important;
    }

    div[data-testid="stMetric"]:hover {
        border-color: #93c5fd !important;

        box-shadow:
            0 5px 12px rgba(37, 99, 235, 0.10) !important;
    }

    div[data-testid="stMetric"] label {
        color: #475569 !important;
    }

    div[data-testid="stMetricValue"] {
        color: #172554 !important;
        font-weight: 800 !important;
    }

    div[data-testid="stMetricValue"] > div {
        color: #172554 !important;
    }

    div[data-testid="stMetricDelta"] {
        color: #334155 !important;
    }


    /* ========================================================
       TABS
       ======================================================== */

    button[data-baseweb="tab"] {
        background-color: #e2e8f0 !important;
        color: #475569 !important;
        font-weight: 600 !important;
    }

    button[data-baseweb="tab"] p {
        color: #475569 !important;
    }

    button[data-baseweb="tab"]:hover {
        background-color: #dbeafe !important;
    }

    button[data-baseweb="tab"][aria-selected="true"] {
        background-color: #2563eb !important;
        color: #ffffff !important;
    }

    button[data-baseweb="tab"][aria-selected="true"] p {
        color: #ffffff !important;
        font-weight: 700 !important;
    }


    /* ========================================================
       ALERT BOXES
       ======================================================== */

    div[data-testid="stAlert"] {
        border-radius: 10px !important;
    }

    div[data-testid="stAlert"] p {
        color: #1e293b !important;
    }


    /* ========================================================
       INFO BOX
       ======================================================== */

    div[data-testid="stAlert"][kind="info"] {
        background-color: #eff6ff !important;
        border: 1px solid #93c5fd !important;
    }


    /* ========================================================
       SUCCESS BOX
       ======================================================== */

    div[data-testid="stAlert"][kind="success"] {
        background-color: #f0fdf4 !important;
        border: 1px solid #86efac !important;
    }


    /* ========================================================
       WARNING BOX
       ======================================================== */

    div[data-testid="stAlert"][kind="warning"] {
        background-color: #fff7ed !important;
        border: 1px solid #fdba74 !important;
    }


    /* ========================================================
       CHART CONTAINER
       ======================================================== */

    [data-testid="stVegaLiteChart"] {
        background-color: #ffffff !important;
        border: 1px solid #cbd5e1 !important;
        border-radius: 12px !important;
        padding: 15px !important;

        box-shadow:
            0 3px 8px rgba(15, 23, 42, 0.05) !important;
    }


    /* ========================================================
       DIVIDERS
       ======================================================== */

    hr {
        border: none !important;
        border-top: 1px solid #cbd5e1 !important;
    }


    /* ========================================================
       CAPTION
       ======================================================== */

    [data-testid="stCaptionContainer"] {
        color: #64748b !important;
    }


    /* ========================================================
       EXPANDERS
       ======================================================== */

    [data-testid="stExpander"] {
        background-color: #ffffff !important;
        border: 1px solid #cbd5e1 !important;
        border-radius: 10px !important;
    }

    [data-testid="stExpander"] p {
        color: #334155 !important;
    }


    /* ========================================================
       SPINNER
       ======================================================== */

    [data-testid="stSpinner"] {
        color: #2563eb !important;
    }


    /* ========================================================
       REMOVE DARK BACKGROUNDS FROM COMMON CONTAINERS
       ======================================================== */

    div[data-testid="stVerticalBlock"],
    div[data-testid="stHorizontalBlock"] {
        background-color: transparent !important;
    }


    /* ========================================================
       SCROLLBAR
       ======================================================== */

    ::-webkit-scrollbar {
        width: 8px;
    }

    ::-webkit-scrollbar-track {
        background: #e2e8f0;
    }

    ::-webkit-scrollbar-thumb {
        background: #94a3b8;
        border-radius: 10px;
    }

    ::-webkit-scrollbar-thumb:hover {
        background: #64748b;
    }

    </style>
    """,
    unsafe_allow_html=True
)


# ============================================================
# SIDEBAR
# ============================================================

with st.sidebar:

    st.title("💰 Financial Planner")

    st.markdown("---")

    st.markdown("### About")

    st.write(
        """
        This AI Financial Planner helps you:

        - 📊 Analyze your finances
        - 💰 Plan your budget
        - 📈 Suggest investments
        - 🎯 Achieve your financial goals
        """
    )


# ============================================================
# MAIN HEADER
# ============================================================

st.title("💰 Financial Life Planner AI")

st.caption(
    "Plan smarter. Invest better. Achieve your financial goals with AI."
)

st.markdown("---")


# ============================================================
# PERSONAL INFORMATION
# ============================================================

st.subheader("👤 Personal Information")

col1, col2 = st.columns(2)

with col1:

    name = st.text_input(
        "Full Name"
    )

    age = st.number_input(
        "Age",
        min_value=18,
        max_value=100,
        value=25
    )

    occupation = st.text_input(
        "Occupation"
    )


with col2:

    risk = st.selectbox(
        "Risk Preference",
        [
            "Low",
            "Moderate",
            "High"
        ]
    )

    goal = st.selectbox(
        "Primary Financial Goal",
        [
            "Emergency Fund",
            "Buy House",
            "Retirement",
            "Wealth Creation",
            "Child Education",
            "Vacation"
        ]
    )


# ============================================================
# FINANCIAL INFORMATION
# ============================================================

st.markdown("---")

st.subheader("💵 Financial Information")

col3, col4 = st.columns(2)

with col3:

    monthly_income = st.number_input(
        "Monthly Income (₹)",
        min_value=0.0,
        value=0.0
    )

    savings = st.number_input(
        "Current Savings (₹)",
        min_value=0.0,
        value=0.0
    )

    investment = st.number_input(
        "Current Investments (₹)",
        min_value=0.0,
        value=0.0
    )


with col4:

    monthly_expenses = st.number_input(
        "Monthly Expenses (₹)",
        min_value=0.0,
        value=0.0
    )

    debt = st.number_input(
        "Outstanding Debt (₹)",
        min_value=0.0,
        value=0.0
    )


# ============================================================
# FINANCIAL GOAL
# ============================================================

st.markdown("---")

financial_goal = st.text_area(
    "📝 Describe your Financial Goal",
    height=120,
    placeholder=(
        "Example: I want to buy a house in the next 5 years "
        "while building an emergency fund..."
    )
)

st.markdown("")


# ============================================================
# GENERATE BUTTON
# ============================================================

generate = st.button(
    "🚀 Generate Financial Plan",
    use_container_width=True
)


# ============================================================
# RUN LANGGRAPH
# ============================================================

if generate:

    state = {

        "name": name,

        "age": age,

        "occupation": occupation,

        "monthly_income": monthly_income,

        "monthly_expenses": monthly_expenses,

        "savings": savings,

        "debt": debt,

        "investment": investment,

        "risk": risk,

        "goal": goal,

        "financial_goal": financial_goal

    }

    with st.spinner(
        "🧠 AI is analyzing your financial profile..."
    ):

        st.session_state["result"] = graph.invoke(state)

    st.success(
        "✅ Financial Plan Generated Successfully!"
    )

    st.markdown("---")


# ============================================================
# GET RESULT FROM SESSION
# ============================================================

result = st.session_state.get("result")


# ============================================================
# FINANCIAL DASHBOARD
# ============================================================

st.subheader("📊 Financial Dashboard")

m1, m2, m3, m4 = st.columns(4)

with m1:

    st.metric(
        "💵 Income",
        f"₹{monthly_income:,.0f}"
    )

with m2:

    st.metric(
        "💸 Expenses",
        f"₹{monthly_expenses:,.0f}"
    )

with m3:

    st.metric(
        "💰 Savings",
        f"₹{savings:,.0f}"
    )

with m4:

    st.metric(
        "📉 Debt",
        f"₹{debt:,.0f}"
    )


st.markdown("")


# ============================================================
# BEFORE GENERATION
# ============================================================

if result is None:

    st.info(
        """
        Fill in your financial information above and click
        **🚀 Generate Financial Plan** to receive your
        personalized financial analysis.
        """
    )


# ============================================================
# AFTER GENERATION
# ============================================================

else:

    # --------------------------------------------------------
    # FINANCIAL HEALTH SCORE
    # --------------------------------------------------------

    st.metric(
        "⭐ Financial Health Score",
        f'{result["final_recommendation"].financial_score}/10'
    )

    st.markdown("---")


    # --------------------------------------------------------
    # TABS
    # --------------------------------------------------------

    tab1, tab2, tab3, tab4, tab5 = st.tabs(
        [
            "👤 Profile",
            "💰 Budget",
            "🎯 Goal",
            "📈 Investment",
            "🏆 Recommendation"
        ]
    )


    # ========================================================
    # PROFILE TAB
    # ========================================================

    with tab1:

        st.subheader("Financial Summary")

        st.info(
            result["profile_analysis"].summary
        )

        col1, col2 = st.columns(2)

        with col1:

            st.markdown("### ✅ Strengths")

            for strength in result["profile_analysis"].strengths:

                st.success(
                    strength
                )

        with col2:

            st.markdown("### ⚠️ Weaknesses")

            for weakness in result["profile_analysis"].weaknesses:

                st.warning(
                    weakness
                )


    # ========================================================
    # BUDGET TAB
    # ========================================================

    with tab2:

        st.subheader("Monthly Budget")

        c1, c2 = st.columns(2)

        with c1:

            st.metric(
                "Recommended Monthly Savings",
                f"₹{result['budget_plan'].recommended_monthly_savings:,.0f}"
            )

        with c2:

            st.metric(
                "Emergency Fund Target",
                f"₹{result['budget_plan'].emergency_fund_target:,.0f}"
            )

        st.markdown("### 💡 Budget Recommendations")

        for recommendation in result["budget_plan"].recommendations:

            st.info(
                recommendation
            )


    # ========================================================
    # GOAL TAB
    # ========================================================

    with tab3:

        st.subheader("Goal Planning")

        st.metric(
            "🎯 Goal",
            result["goal_plan"].goal_name
        )

        col1, col2 = st.columns(2)

        with col1:

            st.metric(
                "Timeline",
                f"{result['goal_plan'].estimated_years} Years"
            )

        with col2:

            st.metric(
                "Monthly Savings Required",
                f"₹{result['goal_plan'].monthly_saving_required:,.0f}"
            )

        st.markdown("### 📌 Action Steps")

        for step in result["goal_plan"].action_steps:

            st.success(
                f"✅ {step}"
            )


    # ========================================================
    # INVESTMENT TAB
    # ========================================================

    with tab4:

        st.subheader("Investment Allocation")

        allocation = {

            "Emergency Fund":
                result["investment_plan"].emergency_fund,

            "Equity":
                result["investment_plan"].equity,

            "Mutual Funds":
                result["investment_plan"].mutual_funds,

            "Fixed Deposits":
                result["investment_plan"].fixed_deposits,

            "Gold":
                result["investment_plan"].gold,

            "Cash":
                result["investment_plan"].cash,

        }

        st.bar_chart(
            allocation
        )

        st.markdown("### 💬 AI Explanation")

        st.info(
            result["investment_plan"].explanation
        )

        st.markdown("### 📊 Allocation")

        for key, value in allocation.items():

            st.write(
                f"**{key}:** {value}%"
            )


    # ========================================================
    # RECOMMENDATION TAB
    # ========================================================

    with tab5:

        st.subheader(
            "🏆 Personalized Financial Plan"
        )

        st.markdown("### 🎯 Top Priorities")

        for priority in result["final_recommendation"].top_priorities:

            st.success(
                priority
            )

        st.markdown("### 📈 Investment Advice")

        for advice in result["final_recommendation"].investment_advice:

            st.info(
                advice
            )

        st.markdown("### 💰 Budget Advice")

        for advice in result["final_recommendation"].budget_advice:

            st.info(
                advice
            )


# ============================================================
# FOOTER
# ============================================================

st.markdown("---")