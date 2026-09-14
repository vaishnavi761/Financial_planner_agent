# 💰 Financial Life Planner AI

An **Agentic AI-powered financial planning assistant** that analyzes a user's financial profile, creates a budget, evaluates financial risk, plans goals, generates investment suggestions, and produces a final personalized financial plan.

The project uses **LangGraph** to orchestrate multiple specialized AI agents through a structured workflow. Each agent performs a specific financial-planning task and shares its results through a common state.

> **Disclaimer:** This project is intended for educational and demonstration purposes. It does not provide professional financial advice or guarantee financial outcomes. Users should consult a qualified financial advisor before making real financial decisions.

---

## 📌 Problem Statement

Personal financial planning often requires combining several activities:

- Understanding income and expenses
- Creating a realistic budget
- Setting short-term and long-term financial goals
- Assessing financial risk
- Considering investment options
- Prioritizing financial objectives
- Converting all of these factors into one actionable plan

Traditional financial-planning workflows can be difficult for beginners because these activities are interconnected.

A single LLM prompt may generate a financial response, but it does not provide a reliable way to divide the task into specialized stages, maintain structured information between stages, or create a transparent workflow.

### Proposed Solution

**Financial Life Planner AI** addresses this problem using a **multi-agent Agentic AI architecture**.

Instead of asking one AI model to perform everything, the system uses multiple specialized agents. Each agent focuses on one responsibility and passes its output to the next stage through a shared state managed by LangGraph.

---

# 🎯 Objectives

The main objectives of this project are:

1. Analyze the user's financial profile.
2. Understand income, expenses, savings, liabilities, and financial preferences.
3. Generate a personalized budget plan.
4. Identify and structure financial goals.
5. Assess the user's financial risk profile.
6. Generate investment planning suggestions based on the available profile information.
7. Combine outputs from different agents.
8. Produce a final personalized financial plan.
9. Demonstrate Agentic AI orchestration using LangGraph.
10. Maintain structured outputs using Pydantic schemas.
11. Build a modular architecture where individual agents can be improved independently.
12. Provide an easy-to-use Streamlit interface.

---

# 🤖 Why Agentic AI?

A traditional chatbot might process the entire request using one prompt:

```text
User → LLM → Financial Advice
```

This project follows a multi-agent workflow:

```text
User
  ↓
Profile Agent
  ↓
Budget Agent
  ↓
Goal Agent
  ↓
Risk Agent
  ↓
Investment Agent
  ↓
Recommendation Agent
  ↓
Final Financial Plan
```

Each agent has a clearly defined responsibility.

This demonstrates an important Agentic AI concept:

> **Complex tasks can be decomposed into smaller specialized tasks that are orchestrated to achieve a final objective.**

---

# 🏗️ System Architecture

```text
                         ┌──────────────────────┐
                         │      User Input      │
                         └──────────┬───────────┘
                                    │
                                    ▼
                         ┌──────────────────────┐
                         │    Profile Agent     │
                         │ Income / Expenses /  │
                         │ Financial Situation   │
                         └──────────┬───────────┘
                                    │
                                    ▼
                         ┌──────────────────────┐
                         │     Budget Agent     │
                         │ Budget & Cash Flow   │
                         └──────────┬───────────┘
                                    │
                                    ▼
                         ┌──────────────────────┐
                         │      Goal Agent      │
                         │ Financial Objectives │
                         └──────────┬───────────┘
                                    │
                                    ▼
                         ┌──────────────────────┐
                         │      Risk Agent      │
                         │ Risk Assessment      │
                         └──────────┬───────────┘
                                    │
                                    ▼
                         ┌──────────────────────┐
                         │  Investment Agent    │
                         │ Investment Planning  │
                         └──────────┬───────────┘
                                    │
                                    ▼
                         ┌──────────────────────┐
                         │ Recommendation Agent │
                         │ Final Plan & Report   │
                         └──────────┬───────────┘
                                    │
                                    ▼
                         ┌──────────────────────┐
                         │  Final Financial     │
                         │       Plan           │
                         └──────────────────────┘
```

---

# 🔄 Agent Workflow

## 1. Profile Analysis Agent

**File:**

```text
agents/profile.py
```

### Responsibility

Analyzes the user's financial information and creates a structured financial profile.

Typical information can include:

- Monthly income
- Monthly expenses
- Existing savings
- Loans/liabilities
- Age or life stage
- Financial priorities
- Existing investments
- Emergency savings

### Output

The agent creates a structured profile that becomes part of the shared workflow state.

---

## 2. Budget Planning Agent

**File:**

```text
agents/budget.py
```

### Responsibility

Uses the financial profile to develop a practical budget.

It can analyze:

- Essential expenses
- Discretionary expenses
- Savings capacity
- Debt obligations
- Potential areas for expense reduction

### Output

A structured budget plan is added to the shared state.

---

## 3. Goal Planning Agent

**File:**

```text
agents/goal.py
```

### Responsibility

Analyzes the user's financial objectives and organizes them into meaningful goals.

Examples include:

- Emergency fund
- Education
- Home purchase
- Retirement
- Travel
- Major purchases

The agent can prioritize goals based on factors such as urgency, importance, and available resources.

---

## 4. Risk Assessment Agent

**File:**

```text
agents/risk.py
```

### Responsibility

Evaluates the user's financial risk profile based on the information available to the workflow.

The agent can consider:

- Financial stability
- Existing liabilities
- Savings level
- Investment preferences
- Goal horizon
- Ability to tolerate financial losses

### Output

A structured risk assessment is passed to the next agent.

---

## 5. Investment Planning Agent

**File:**

```text
agents/investment.py
```

### Responsibility

Uses the profile, goals, budget, and risk assessment to generate an investment-planning perspective.

The agent can organize suggestions by:

- Risk level
- Time horizon
- Financial goal
- Available investment capacity
- Liquidity requirements

The output should be treated as educational planning guidance rather than personalized professional investment advice.

---

## 6. Recommendation Agent

**File:**

```text
agents/recommendation.py
```

### Responsibility

Acts as the final synthesis layer.

It receives the outputs generated by previous agents and combines them into a coherent financial plan.

The final report can contain:

- Financial profile summary
- Budget overview
- Goal priorities
- Risk assessment
- Investment planning considerations
- Savings recommendations
- Action plan
- Overall financial strategy

---

# 🧠 LangGraph Workflow

**File:**

```text
graph/workflow.py
```

LangGraph is responsible for orchestrating the agents.

Conceptually, the workflow is:

```text
START
  ↓
Profile
  ↓
Budget
  ↓
Goal
  ↓
Risk
  ↓
Investment
  ↓
Recommendation
  ↓
END
```

Each node represents an agent or processing step.

The shared state allows information generated by one agent to be accessed by subsequent agents.

This makes the workflow more structured than a single LLM call.

---

# 🗂️ Shared State

**File:**

```text
models/state.py
```

The shared state acts as the common information layer between agents.

Conceptually:

```text
FinancialState
│
├── user_input
├── profile
├── budget
├── goals
├── risk
├── investment
└── recommendation
```

When an agent completes its task, its result can be stored in the state.

The next agent can then use the accumulated information.

---

# 📦 Pydantic Schemas

The project uses structured schemas to make agent outputs more predictable.

Directory:

```text
schemas/
```

Files:

```text
schemas/
├── profile.py
├── budget.py
├── investment.py
├── goal.py
├── risk.py
└── recommendation.py
```

### Why use schemas?

Without structured output:

```text
LLM → Free-form text
```

With schemas:

```text
LLM
 ↓
Structured Output
 ↓
Pydantic Validation
 ↓
Agent State
```

Benefits include:

- Consistent output structure
- Easier validation
- Easier downstream processing
- Reduced ambiguity
- Better maintainability
- Easier integration between agents

---

# ✍️ Prompt Management

**File:**

```text
prompts/prompt.py
```

The project keeps agent instructions and prompt templates separately from the application logic.

This provides:

- Cleaner code
- Easier prompt modification
- Reusable prompts
- Better separation of concerns
- Easier experimentation with prompt engineering

Each agent can use a task-specific prompt.

---

# 🔌 LLM Integration

**File:**

```text
utils/llm.py
```

This module is responsible for initializing and managing the LLM connection.

The project uses Google's Gemini API through the configured Google API key.

Keeping LLM initialization in one place makes it easier to:

- Change the model
- Modify model parameters
- Reuse the LLM across agents
- Avoid duplicating configuration code

---

# 🖥️ Streamlit Application

**File:**

```text
app.py
```

Streamlit provides the user interface.

The application can collect financial information from the user and trigger the LangGraph workflow.

The final results can be displayed in sections such as:

```text
Financial Profile
       ↓
Budget Plan
       ↓
Financial Goals
       ↓
Risk Assessment
       ↓
Investment Planning
       ↓
Final Recommendation
```

---

# 📁 Project Structure

```text
Financial-Life-Planner-AI/
│
├── agents/
│   ├── profile.py
│   ├── budget.py
│   ├── investment.py
│   ├── goal.py
│   ├── risk.py
│   └── recommendation.py
│
├── graph/
│   └── workflow.py
│
├── models/
│   └── state.py
│
├── prompts/
│   └── prompt.py
│
├── schemas/
│   ├── profile.py
│   ├── budget.py
│   ├── investment.py
│   ├── goal.py
│   ├── risk.py
│   └── recommendation.py
│
├── utils/
│   └── llm.py
│
├── app.py
├── requirements.txt
├── .env
└── README.md
```

---

# ⚙️ Technologies Used

| Technology | Purpose |
|---|---|
| Python | Core programming language |
| LangGraph | Agent orchestration and workflow management |
| LangChain | LLM application framework |
| Google Gemini | Large Language Model |
| Pydantic | Structured output validation |
| Streamlit | Web application interface |
| python-dotenv | Environment variable management |

---

# 🔑 Environment Variables

Create a `.env` file in the project root:

```text
GOOGLE_API_KEY=your_api_key
```

Do not commit your actual API key to GitHub.

Add `.env` to `.gitignore`:

```text
.env
__pycache__/
*.pyc
```

For GitHub, you can provide an example file such as:

```text
.env.example
```

with:

```text
GOOGLE_API_KEY=your_api_key_here
```

---

# 🚀 Installation

## Step 1: Clone the Repository

```bash
git clone <your-github-repository-url>
```

Move into the project directory:

```bash
cd Financial-Life-Planner-AI
```

---

## Step 2: Create a Virtual Environment

Windows:

```bash
python -m venv venv
```

Activate it:

```bash
venv\Scripts\activate
```

Linux/macOS:

```bash
python3 -m venv venv
source venv/bin/activate
```

---

## Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Step 4: Configure API Key

Create:

```text
.env
```

Add:

```text
GOOGLE_API_KEY=your_api_key
```

---

## Step 5: Run the Application

```bash
streamlit run app.py
```

The Streamlit application will open in your browser.

---

# 🔄 End-to-End Execution Flow

The application follows this sequence:

### Step 1 — User Input

The user provides financial information through the Streamlit interface.

### Step 2 — Profile Analysis

The Profile Agent analyzes the information and creates a structured profile.

### Step 3 — Budget Planning

The Budget Agent uses the profile to create a budget strategy.

### Step 4 — Goal Planning

The Goal Agent identifies and prioritizes financial objectives.

### Step 5 — Risk Assessment

The Risk Agent evaluates the user's financial risk characteristics.

### Step 6 — Investment Planning

The Investment Agent generates investment-planning considerations using the accumulated context.

### Step 7 — Final Recommendation

The Recommendation Agent synthesizes all previous results.

### Step 8 — Display

Streamlit presents the final financial plan to the user.

---

# ⭐ Key Features

### Multi-Agent Architecture

Multiple specialized agents collaborate instead of relying on one general-purpose prompt.

### Sequential Agentic Workflow

LangGraph controls the order in which agents execute.

### Shared State

Information generated by earlier agents can be used by later agents.

### Structured Outputs

Pydantic schemas provide predictable data structures.

### Modular Design

Each agent is separated into its own Python module.

### Prompt Separation

Prompts are maintained separately from agent implementation.

### Interactive UI

Streamlit provides a simple interface for interacting with the system.

### Final Report Generation

All agent outputs are combined into a single financial-planning report.

---

# 🧩 Agent Responsibilities at a Glance

| Agent | Main Responsibility | Uses |
|---|---|---|
| Profile Agent | Understand financial situation | User input |
| Budget Agent | Create spending/saving plan | Profile |
| Goal Agent | Identify and prioritize goals | Profile + Budget |
| Risk Agent | Assess financial risk | Profile + Goals |
| Investment Agent | Create investment-planning perspective | Profile + Budget + Goals + Risk |
| Recommendation Agent | Generate final plan | All previous outputs |

---

# 💡 Example Use Case

Consider a user who provides:

```text
Monthly Income: ₹80,000
Monthly Expenses: ₹45,000
Savings: ₹2,00,000
Loan: ₹5,00,000
Goal: Buy a house
Investment Preference: Moderate Risk
```

The workflow can process this information as:

```text
User Input
    ↓
Profile Analysis
    ↓
Income / Expense / Liability Analysis
    ↓
Budget Planning
    ↓
House-Purchase Goal Analysis
    ↓
Risk Assessment
    ↓
Investment Planning
    ↓
Final Financial Strategy
```

The important point is that the final agent does not need to independently solve every problem. It receives structured outputs from specialized agents.

---

# 🔐 Security Considerations

Financial information can be sensitive. Therefore:

- Do not hard-code API keys.
- Do not commit `.env` files.
- Avoid storing unnecessary personal financial information.
- Do not expose API keys in application logs.
- Use environment variables for secrets.
- Treat generated recommendations as informational.
- Avoid presenting AI-generated output as guaranteed financial advice.

---

# ⚠️ Limitations

This project has several limitations:

1. LLM-generated recommendations can contain inaccuracies.
2. Financial markets and products change over time.
3. The system may not have access to real-time market data unless an external data source is integrated.
4. Investment suggestions are not a substitute for professional financial advice.
5. The quality of recommendations depends on the accuracy and completeness of user-provided information.
6. The current workflow is primarily a sequential multi-agent architecture.

---

# 🔮 Future Enhancements

The project can be extended with:

## 1. Real-Time Financial Data

Integrate reliable financial APIs to retrieve current market information.

## 2. RAG

Add a financial knowledge base containing trusted financial documents and educational resources.

```text
User Query
    ↓
Retriever
    ↓
Financial Knowledge
    ↓
Agent
    ↓
Recommendation
```

## 3. Agent Memory

Add persistent memory to remember relevant user preferences across sessions, with appropriate privacy controls.

## 4. Human-in-the-Loop

Add an approval step before generating or executing sensitive recommendations.

```text
Agents
  ↓
Recommendation
  ↓
Human Review
  ↓
Final Plan
```

## 5. LangSmith / Observability

Add tracing and monitoring to inspect:

- Agent execution
- Latency
- LLM calls
- Errors
- Token usage
- Workflow behavior

## 6. Evaluation

Create a golden dataset and evaluate:

- Output correctness
- Consistency
- Relevance
- Structured-output validity
- Recommendation quality

## 7. Advanced Agent Routing

Instead of always using a fixed sequence, LangGraph can be extended with conditional routing.

For example:

```text
Profile
   ↓
Risk Assessment
   ↓
 ┌───────────────┐
 │ Risk Level?   │
 └───────┬───────┘
     Low │ High
         │
         ▼
 Different planning paths
```

## 8. Report Export

Allow users to export the final financial plan as PDF or other formats.

---

# 🧪 Testing Strategy

Each agent can be tested independently before testing the complete workflow.

### Unit Testing

Test:

- Input validation
- Schema validation
- Individual agent outputs
- State updates
- Prompt behavior

### Integration Testing

Verify that:

```text
Profile → Budget → Goal → Risk → Investment → Recommendation
```

works correctly as a complete workflow.

### Evaluation Testing

Use predefined financial scenarios to check whether the system produces consistent and relevant structured outputs.

---

# 📊 What This Project Demonstrates

This project demonstrates practical knowledge of:

- Python
- Generative AI
- LLM applications
- Agentic AI
- Multi-agent architecture
- LangChain
- LangGraph
- Prompt engineering
- Pydantic structured outputs
- State management
- Workflow orchestration
- Streamlit
- Environment-variable management
- Modular software architecture

---

# 🧠 Agentic AI Concepts Demonstrated

The project can be explained using the following concepts:

### 1. Agent

An AI component responsible for a specific task.

### 2. Tool/Capability

The functionality available to an agent to perform its assigned task.

### 3. State

Shared information maintained throughout the workflow.

### 4. Workflow

The sequence or graph controlling agent execution.

### 5. Orchestration

Coordinating multiple agents to accomplish a larger task.

### 6. Structured Output

Converting LLM responses into predictable schemas.

### 7. Multi-Agent Collaboration

Multiple specialized agents contribute to one final result.

---

# 🎤 Interview Explanation

A concise way to explain the project in an interview:

> **"Financial Life Planner AI is an Agentic AI application that uses LangGraph to orchestrate multiple specialized financial-planning agents. The workflow starts by analyzing the user's financial profile, then creates a budget, identifies financial goals, assesses risk, generates investment-planning considerations, and finally combines all outputs into a personalized financial plan. I used a shared state to pass information between agents and Pydantic schemas to maintain structured outputs. Streamlit provides the user interface, while Google Gemini acts as the LLM."**

---

# ❓ Why LangGraph Instead of a Single LLM Call?

A single LLM call would make the system simpler, but it would combine multiple responsibilities into one prompt.

LangGraph provides:

- Explicit workflow control
- Separate agent responsibilities
- Shared state
- Easier debugging
- Conditional routing capability
- Extensibility
- Better demonstration of agentic workflows

Therefore, LangGraph is useful when the application contains multiple dependent steps or agents.

---

# 🆚 Traditional Chatbot vs This Project

| Traditional Chatbot | Financial Life Planner AI |
|---|---|
| One general prompt | Multiple specialized agents |
| Mostly linear response | Explicit workflow |
| Limited task separation | Clear agent responsibilities |
| Unstructured output possible | Pydantic schemas |
| Little state management | Shared workflow state |
| Difficult to extend | Modular architecture |
| General response | Financial planning workflow |

---

# 📈 Project Impact

The project demonstrates how a complex domain problem can be decomposed into smaller AI tasks and orchestrated through an agentic workflow.

Instead of:

```text
One Large Prompt
       ↓
One Large Response
```

the system uses:

```text
Complex Problem
       ↓
Task Decomposition
       ↓
Specialized Agents
       ↓
Shared State
       ↓
Workflow Orchestration
       ↓
Structured Final Recommendation
```

---

# 🛠️ Possible Production Architecture

A production-ready version could be extended to:

```text
                    ┌─────────────────┐
                    │   Streamlit/UI  │
                    └────────┬────────┘
                             │
                             ▼
                    ┌─────────────────┐
                    │   LangGraph     │
                    │   Orchestrator  │
                    └────────┬────────┘
                             │
          ┌──────────────────┼──────────────────┐
          ▼                  ▼                  ▼
     Profile Agent      Budget Agent       Goal Agent
          │                  │                  │
          └──────────────────┼──────────────────┘
                             ▼
                       Risk Agent
                             │
                             ▼
                    Investment Agent
                             │
                             ▼
                  Recommendation Agent
                             │
              ┌──────────────┴──────────────┐
              ▼                             ▼
       Financial APIs                  Knowledge Base
              │                             │
              └──────────────┬──────────────┘
                             ▼
                      Final Financial Plan
```

---

# 📋 Project Checklist

- [x] Multi-agent architecture
- [x] Specialized financial agents
- [x] LangGraph orchestration
- [x] Shared state
- [x] Pydantic schemas
- [x] Prompt management
- [x] LLM utility module
- [x] Streamlit interface
- [x] Environment variable configuration
- [ ] Real-time financial data
- [ ] RAG knowledge base
- [ ] Agent evaluation
- [ ] Observability/tracing
- [ ] Human-in-the-loop
- [ ] Production deployment

---

# 👩‍💻 Author

**Vaishnavi Ansapure**

AI/ML & Generative AI Project

---

# ⭐ Conclusion

**Financial Life Planner AI** demonstrates how Agentic AI can be applied to a real-world planning problem by decomposing a complex task into specialized agents.

The combination of **LangGraph + LLMs + Pydantic + Streamlit** creates a modular foundation that can be extended with real-time data, RAG, memory, evaluation, observability, and human-in-the-loop controls.

The project is primarily designed to demonstrate **Agentic AI architecture, workflow orchestration, structured LLM outputs, and modular AI application development**.
