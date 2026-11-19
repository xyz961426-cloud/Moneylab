import streamlit as st
import plotly.graph_objects as go
from lesson1 import lesson1
from lesson2 import lesson2
from lesson3 import lesson3
from lesson4 import show_lesson4
from lesson5 import show_lesson5
from lesson6 import show_lesson6

st.set_page_config(page_title="MoneyLab", page_icon="💰", layout="wide")

st.markdown("""
<style>
.stApp {
    background: #080d18;
    color: #e6edf7;
}
[data-testid="stSidebar"] {
    background: #101827;
}
[data-testid="stSidebar"] * {
    color: #e6edf7;
}
.block-container {
    padding-top: 2rem;
    padding-bottom: 2rem;
    max-width: 1200px;
}
div[data-testid="stMetric"] {
    background: #111b2c;
    border: 1px solid #23324a;
    padding: 20px;
    border-radius: 14px;
}
.stButton button {
    border-radius: 10px;
}
h1, h2, h3 {
    color: #f1f5f9;
}
</style>
""", unsafe_allow_html=True)

st.sidebar.markdown("# 💰 MoneyLab")
st.sidebar.caption("LEARN MONEY BY LIVING IT")
st.sidebar.markdown("---")

page = st.sidebar.radio(
    "NAVIGATION",
    ["Dashboard", "Money Basics", "Life Simulator", "Investment Lab", "Progress", "Lesson 1", "Lesson 2", "Lesson 3" , "Lesson 4" , "Lesson 5" , "Lesson 6"]
)

st.sidebar.markdown("---")
st.sidebar.caption("MoneyLab | Financial Education")

if page == "Dashboard":
    st.markdown("## Welcome to MoneyLab")
    st.markdown("### Understand money. Make decisions. Build your future.")
    st.markdown("---")

    a, b, c = st.columns(3)
    a.metric("Virtual Capital", "$10,000", "Practice money")
    b.metric("Lessons Completed", "0 / 35", "Start learning")
    c.metric("Current Level", "Beginner", "Level 1")

    st.markdown("### Your learning journey")
    st.progress(0)
    st.caption("0% complete — your financial journey begins here.")

    st.markdown("---")
    st.markdown("## Explore MoneyLab")

    x, y = st.columns(2)

    with x:
        st.markdown("### 🏦 Money Basics")
        st.write("Understand income, expenses, saving, inflation and how money works.")
        st.markdown("### 🌎 Life Simulator")
        st.write("Make real-life financial decisions using a virtual monthly salary.")

    with y:
        st.markdown("### 📈 Investment Lab")
        st.write("Experiment with compound growth, contributions and investment risk.")
        st.markdown("### 🧠 Decision Room")
        st.write("Explore financial choices and discover their consequences.")

    st.markdown("---")
    st.markdown("## Today's Challenge")

    st.info(
        "Why can someone earning $10,000 per month still be financially broke?"
    )

    st.markdown("### Start with a simple principle")
    st.write(
        "Income is how much money you earn. Wealth is what you build "
        "and retain over time. Spending, saving, investing and risk "
        "management influence your financial future."
    )

elif page == "Money Basics":
    st.title("🏦 Money Basics")
    st.markdown("### Lesson 1 — Purchasing Power")

    st.write("Inflation can reduce the amount of goods and services money buys.")

    money = st.slider("Starting money ($)", 100, 10000, 1000, 100)
    inflation = st.slider("Annual inflation (%)", 0.0, 20.0, 5.0)
    years = st.slider("Years", 1, 30, 10)

    future = money / (1 + inflation / 100) ** years

    st.metric("Future purchasing power", f"${future:,.2f}")
    st.caption("Illustration assuming constant inflation, not a forecast.")

elif page == "Life Simulator":
    st.title("🌎 Life Simulator")
    st.markdown("### Manage your virtual monthly salary")

    salary = st.number_input("Monthly income ($)", min_value=0, value=2500)
    housing = st.slider("Housing ($)", 0, 2000, 600, 50)
    food = st.slider("Food ($)", 0, 1000, 300, 25)
    transport = st.slider("Transport ($)", 0, 1000, 150, 25)
    entertainment = st.slider("Entertainment ($)", 0, 1000, 200, 25)
    other = st.slider("Other ($)", 0, 1000, 100, 25)

    expenses = housing + food + transport + entertainment + other
    remaining = salary - expenses

    a, b, c = st.columns(3)
    a.metric("Income", f"${salary:,.0f}")
    b.metric("Expenses", f"${expenses:,.0f}")
    c.metric("Remaining", f"${remaining:,.0f}")

    if remaining < 0:
        st.error("You are spending more than you earn.")
    elif remaining == 0:
        st.warning("You have no money left.")
    else:
        st.success("You have money remaining.")

    if salary > 0:
        st.metric("Savings rate", f"{remaining/salary*100:.1f}%")

    fig = go.Figure(data=[go.Pie(
        labels=["Housing", "Food", "Transport", "Entertainment", "Other", "Remaining"],
        values=[housing, food, transport, entertainment, other, max(remaining, 0)],
        hole=0.6
    )])

    fig.update_layout(template="plotly_dark", paper_bgcolor="#080d18")
    st.plotly_chart(fig, use_container_width=True)

elif page == "Investment Lab":
    st.title("📈 Investment Lab")
    st.markdown("### Explore hypothetical compound growth")

    initial = st.slider("Initial investment ($)", 100, 100000, 1000, 100)
    monthly = st.slider("Monthly contribution ($)", 0, 5000, 100, 50)
    rate = st.slider("Assumed annual return (%)", 0.0, 20.0, 8.0, 0.5)
    years = st.slider("Years", 1, 50, 20)

    balance = initial
    values = [balance]

    for _ in range(years * 12):
        balance *= (1 + rate / 100) ** (1 / 12)
        balance += monthly
        values.append(balance)

    contributed = initial + monthly * years * 12

    a, b, c = st.columns(3)
    a.metric("Simulated Value", f"${balance:,.2f}")
    b.metric("Total Contributed", f"${contributed:,.2f}")
    c.metric("Illustrative Growth", f"${balance-contributed:,.2f}")

    fig = go.Figure()
    fig.add_trace(go.Scatter(y=values, mode="lines", name="Portfolio"))

    fig.update_layout(
        template="plotly_dark",
        paper_bgcolor="#080d18",
        title="Portfolio Simulation",
        xaxis_title="Month",
        yaxis_title="Value ($)"
    )

    st.plotly_chart(fig, use_container_width=True)
    st.warning("Assumed returns are not guaranteed. Real investments can lose money.")

elif page == "Lesson 1":
    lesson1()

elif page == "Lesson 2":
    lesson2()

elif page == "Lesson 3":
    lesson3()
    
elif page == "Lesson 4":
    show_lesson4()
    
elif page == "Lesson 5":
    show_lesson5()

elif page == "Lesson 6":
    show_lesson6()
        
elif page == "Progress":
    st.title("🏆 Progress")

    a, b, c = st.columns(3)
    a.metric("Lessons", "0")
    b.metric("Challenges", "0")
    c.metric("Learning XP", "0")

    st.progress(0)
    st.info("Complete lessons and challenges to build your financial knowledge.")

st.markdown("---")
st.caption("MoneyLab • Learn. Experiment. Understand. Grow.")
