
import streamlit as st
import plotly.graph_objects as go

from lesson1 import lesson1
from lesson2 import lesson2
from lesson3 import lesson3
from lesson4 import show_lesson4
from lesson5 import show_lesson5
from lesson6 import show_lesson6
from lesson7 import lesson7
from lesson8 import lesson8

from chapter3 import show_chapter3
from chapter4 import show_chapter4
from chapter5 import show_chapter5
from chapter6 import show_chapter6
from chapter7 import show_chapter7
from chapter8 import show_chapter8
from chapter9 import show_chapter9
from chapter10 import show_chapter10
from chapter11 import show_chapter11

st.set_page_config(
    page_title="MoneyLab",
    page_icon="💰",
    layout="wide"
)

# NAVIGATION CALLBACK
def go_to_page(target):
    st.session_state.navigation = target


# DESIGN
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
    min-height: 45px;
}
h1, h2, h3 {
    color: #f1f5f9;
}
.learning-card {
    background: #111b2c;
    border: 1px solid #23324a;
    padding: 22px;
    border-radius: 16px;
}
</style>
""", unsafe_allow_html=True)


# SIDEBAR
st.sidebar.markdown("# 💰 MoneyLab")
st.sidebar.caption("LEARN MONEY BY LIVING IT")
st.sidebar.markdown("---")

pages = [
    "Dashboard",
    "Money Basics",
    "Life Simulator",
    "Investment Lab",
    "Progress",

    "Lesson 1",
    "Lesson 2",
    "Lesson 3",
    "Lesson 4",
    "Lesson 5",
    "Lesson 6",
    "Lesson 7",
    "Lesson 8",

    "Chapter 3 • Lessons 9–12",
    "Chapter 4 • Lessons 13–16",
    "Chapter 5 • Lessons 17–20",
    "Chapter 6 • Lessons 21–24",
    "Chapter 7 • Lessons 25–28",
    "Chapter 8 • Lessons 29–32",
    "Chapter 9 • Lessons 33–36",
    "Chapter 10 • Lessons 37–40",
    "Chapter 11 • Lessons 41–44"
]

if "navigation" not in st.session_state:
    st.session_state.navigation = "Dashboard"

page = st.sidebar.radio(
    "NAVIGATION",
    pages,
    key="navigation"
)

st.sidebar.markdown("---")
st.sidebar.caption("MoneyLab | Financial Education")


# DASHBOARD
if page == "Dashboard":

    st.markdown("""
    <div style="
    background:linear-gradient(135deg,#10233e,#1d4ed8);
    padding:35px;
    border-radius:25px;
    border:1px solid #29476d;
    ">
    <div style="font-size:20px;color:#86efac;font-weight:bold;">
    MONEYLAB
    </div>

    <h1 style="font-size:42px;">
    Learn Money by Living It.
    </h1>

    <p style="font-size:19px;">
    Make decisions. Learn financial skills.
    Build a better financial future.
    </p>

    <p style="font-size:16px;color:#cbd5e1;">
    No experience needed. Start from the beginning.
    </p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("## 🌱 Start Your Learning Journey")

    st.write("""
    MoneyLab teaches financial concepts through stories,
    interactive simulations, decisions and practical explanations.
    """)

    st.button(
        "🚀 Start Learning from Lesson 1",
        key="start_learning",
        on_click=go_to_page,
        args=("Lesson 1",),
        use_container_width=True
    )

    st.markdown("---")
    st.markdown("## 🗺️ Your Learning Path")

    chapters = [
        ("Lesson 1", "Start your financial journey."),
        ("Lesson 2", "Build your understanding of money."),
        ("Lesson 3", "Continue learning financial fundamentals."),
        ("Lesson 4", "Smart Spending."),
        ("Lesson 5", "The Emergency Trap."),
        ("Lesson 6", "The Investing Race."),
        ("Lesson 7", "Continue your financial education."),
        ("Lesson 8", "Continue your financial education."),
        ("Chapter 3 • Lessons 9–12", "Explore the next four lessons."),
        ("Chapter 4 • Lessons 13–16", "Understanding Debt."),
        ("Chapter 5 • Lessons 17–20", "The Investing World."),
        ("Chapter 6 • Lessons 21–24", "The World of Bonds."),
        ("Chapter 7 • Lessons 25–28", "Mutual Funds & ETFs."),
        ("Chapter 8 • Lessons 29–32", "The Power of Compounding & Wealth Building."),
        ("Chapter 9 • Lessons 33–36", "Banking, Central Banks & the Economy."),
        ("Chapter 10 • Lessons 37–40", "Taxes & Personal Finance."),
        ("Chapter 11 • Lessons 41–44", "Financial Markets & Trading.")
    ]

    for title, description in chapters:
        with st.container(border=True):
            st.markdown(f"### 📘 {title}")
            st.write(description)

            st.button(
                f"Open {title} →",
                key=f"dash_{title}",
                on_click=go_to_page,
                args=(title,)
            )

    st.markdown("---")

    # HOW MONEYLAB WORKS
    st.markdown("## 🎓 How MoneyLab Works")

    a, b = st.columns(2)

    with a:
        st.markdown("### 📖 Learn")
        st.write(
            "Understand financial concepts through "
            "stories and simple explanations."
        )

        st.markdown("### 🧠 Decide")
        st.write(
            "Make your own financial decisions "
            "in interactive situations."
        )

    with b:
        st.markdown("### 🎮 Experience")
        st.write(
            "Explore what happens when you make "
            "different financial choices."
        )

        st.markdown("### 💡 Understand")
        st.write(
            "Learn from consequences and apply "
            "your knowledge to real life."
        )

    st.markdown("---")

    # PRACTICE
    st.markdown("## 🎮 Practice Your Skills")

    a, b = st.columns(2)

    with a:
        with st.container(border=True):
            st.markdown("### 🌎 Life Simulator")
            st.write(
                "Practice managing income, expenses "
                "and monthly financial decisions."
            )
            st.button(
                "Enter Life Simulator →",
                key="dash_sim",
                on_click=go_to_page,
                args=("Life Simulator",),
                use_container_width=True
            )

    with b:
        with st.container(border=True):
            st.markdown("### 📈 Investment Lab")
            st.write(
                "Experiment with hypothetical growth, "
                "contributions and investment risk."
            )
            st.button(
                "Enter Investment Lab →",
                key="dash_inv",
                on_click=go_to_page,
                args=("Investment Lab",),
                use_container_width=True
            )

    st.markdown("---")

    st.markdown("## 💡 Today's Financial Question")

    st.info(
        "Why can someone earning a high income still "
        "struggle financially?"
    )

    st.write(
        "Think about spending, debt, saving, financial habits "
        "and the difference between income and wealth."
    )


# MONEY BASICS
elif page == "Money Basics":

    st.title("🏦 Money Basics")
    st.markdown("### Lesson 1 — Purchasing Power")

    st.write(
        "Inflation can reduce the amount of goods "
        "and services money buys."
    )

    money = st.slider(
        "Starting money ($)",
        100, 10000, 1000, 100
    )

    inflation = st.slider(
        "Annual inflation (%)",
        0.0, 20.0, 5.0
    )

    years = st.slider(
        "Years",
        1, 30, 10
    )

    future = money / (1 + inflation / 100) ** years

    st.metric(
        "Future purchasing power",
        f"${future:,.2f}"
    )

    st.caption(
        "Illustration assuming constant inflation, not a forecast."
    )


# LIFE SIMULATOR
elif page == "Life Simulator":

    st.title("🌎 Life Simulator")
    st.markdown("### Manage your virtual monthly salary")

    salary = st.number_input(
        "Monthly income ($)",
        min_value=0,
        value=2500
    )

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
        st.metric(
            "Savings rate",
            f"{remaining/salary*100:.1f}%"
        )

    fig = go.Figure(
        data=[go.Pie(
            labels=[
                "Housing",
                "Food",
                "Transport",
                "Entertainment",
                "Other",
                "Remaining"
            ],
            values=[
                housing,
                food,
                transport,
                entertainment,
                other,
                max(remaining, 0)
            ],
            hole=0.6
        )]
    )

    fig.update_layout(
        template="plotly_dark",
        paper_bgcolor="#080d18"
    )

    st.plotly_chart(fig, use_container_width=True)


# INVESTMENT LAB
elif page == "Investment Lab":

    st.title("📈 Investment Lab")
    st.markdown("### Explore hypothetical compound growth")

    initial = st.slider(
        "Initial investment ($)",
        100, 100000, 1000, 100
    )

    monthly = st.slider(
        "Monthly contribution ($)",
        0, 5000, 100, 50
    )

    rate = st.slider(
        "Assumed annual return (%)",
        0.0, 20.0, 8.0, 0.5
    )

    years = st.slider(
        "Years",
        1, 50, 20
    )

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

    fig.add_trace(
        go.Scatter(
            y=values,
            mode="lines",
            name="Portfolio"
        )
    )

    fig.update_layout(
        template="plotly_dark",
        paper_bgcolor="#080d18",
        title="Portfolio Simulation",
        xaxis_title="Month",
        yaxis_title="Value ($)"
    )

    st.plotly_chart(fig, use_container_width=True)

    st.warning(
        "Assumed returns are not guaranteed. Real investments can lose money."
    )


# LESSON 1
elif page == "Lesson 1":
    lesson1()


# LESSON 2
elif page == "Lesson 2":
    lesson2()


# LESSON 3
elif page == "Lesson 3":
    lesson3()


# LESSON 4
elif page == "Lesson 4":
    show_lesson4()


# LESSON 5
elif page == "Lesson 5":
    show_lesson5()


# LESSON 6
elif page == "Lesson 6":
    show_lesson6()


# LESSON 7
elif page == "Lesson 7":
    lesson7()


# LESSON 8
elif page == "Lesson 8":
    lesson8()


# CHAPTER 3
elif page == "Chapter 3 • Lessons 9–12":
    show_chapter3()


# CHAPTER 4
elif page == "Chapter 4 • Lessons 13–16":
    show_chapter4()


# CHAPTER 5
elif page == "Chapter 5 • Lessons 17–20":
    show_chapter5()


# CHAPTER 6
elif page == "Chapter 6 • Lessons 21–24":
    show_chapter6()


# CHAPTER 7
elif page == "Chapter 7 • Lessons 25–28":
    show_chapter7()


# CHAPTER 8
elif page == "Chapter 8 • Lessons 29–32":
    show_chapter8()


# CHAPTER 9
elif page == "Chapter 9 • Lessons 33–36":
    show_chapter9()


# CHAPTER 10
elif page == "Chapter 10 • Lessons 37–40":
    show_chapter10()


# CHAPTER 11
elif page == "Chapter 11 • Lessons 41–44":
    show_chapter11()


# PROGRESS
elif page == "Progress":

    st.title("📊 Progress")

    st.info(
        "Progress tracking will be developed as "
        "you continue through the MoneyLab learning journey."
    )

    st.write(
        "Explore the lessons to build your financial knowledge."
    )

    st.progress(0)


# FOOTER
st.markdown("---")
st.caption("MoneyLab • Learn. Experiment. Understand. Grow.")
