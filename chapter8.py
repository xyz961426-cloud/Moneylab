
import streamlit as st
import plotly.graph_objects as go


def wealth_quiz(key, questions):
    if key not in st.session_state:
        st.session_state[key] = {}

    for i, q in enumerate(questions):
        st.markdown(f"### Question {i+1}")
        st.write(q["question"])

        choice = st.radio(
            "Choose your answer:",
            q["options"],
            index=None,
            key=f"{key}_q{i}"
        )

        if st.button("Check Answer", key=f"{key}_check{i}"):
            st.session_state[key][i] = choice

        if i in st.session_state[key]:
            answer = st.session_state[key][i]

            if answer == q["answer"]:
                st.success("Correct! " + q["explanation"])
            else:
                st.error(f"Your answer: {answer}")
                st.info(
                    f"Correct answer: {q['answer']}\n\n"
                    f"Explanation: {q['explanation']}"
                )


def show_chapter8():

    st.title("🌱 Chapter 8: The Power of Compounding & Wealth Building")
    st.caption("MoneyLab • Learn Money by Living It")

    st.markdown("""
    <div style="padding:20px;background:#153448;
    border-radius:12px;color:white;">

    <h3>Alex's Long-Term Journey</h3>

    <p>Alex has learned about stocks, bonds and investment funds.</p>

    <p>Now Alex wants to understand how money can grow over
    years, why inflation matters, and how to create a
    realistic plan for the future.</p>

    </div>
    """, unsafe_allow_html=True)

    lesson = st.selectbox(
        "Choose your lesson",
        [
            "Lesson 29 — The Magic of Compounding",
            "Lesson 30 — Time vs Money",
            "Lesson 31 — Inflation & Purchasing Power",
            "Lesson 32 — Building a Wealth Plan"
        ]
    )

    # --------------------------------------------------
    # LESSON 29
    # --------------------------------------------------

    if lesson == "Lesson 29 — The Magic of Compounding":

        st.header("📘 Lesson 29 — The Magic of Compounding")

        st.markdown("""
        ### Alex invests ₹10,000

        Alex invests ₹10,000 and earns an illustrative
        10% annual return.

        At the end of the first year, Alex earns ₹1,000.

        In the second year, returns can be earned on the
        original ₹10,000 and on the previous year's growth.

        This is called compounding.
        """)

        st.markdown("""
        <div style="padding:20px;background:#102B3F;
        border-radius:15px;color:white;text-align:center;">

        <h3>💰 Initial investment</h3>

        <p>₹10,000</p>

        <p>⬇️</p>

        <h3>📈 Returns</h3>

        <p>⬇️</p>

        <h3>💰 Returns can generate further returns</h3>

        <p>⬇️</p>

        <h3>🌱 Compounding</h3>

        </div>
        """, unsafe_allow_html=True)

        st.markdown("### 🎮 Compound growth simulator")

        principal = st.number_input(
            "Initial investment (₹)",
            min_value=1000,
            value=10000,
            step=1000
        )

        rate = st.slider(
            "Illustrative annual return (%)",
            1.0, 30.0, 10.0, 0.5
        )

        years = st.slider(
            "Investment duration",
            1, 50, 20
        )

        simple = principal * (1 + (rate / 100) * years)

        compound = principal * (1 + rate / 100) ** years

        st.metric("Simple growth illustration", f"₹{simple:,.2f}")
        st.metric("Compound growth illustration", f"₹{compound:,.2f}")

        st.metric(
            "Difference",
            f"₹{compound - simple:,.2f}"
        )

        simple_values = []
        compound_values = []

        for year in range(years + 1):
            simple_values.append(
                principal * (1 + rate / 100 * year)
            )

            compound_values.append(
                principal * (1 + rate / 100) ** year
            )

        fig = go.Figure()

        fig.add_trace(go.Scatter(
            x=list(range(years + 1)),
            y=simple_values,
            mode="lines",
            name="Simple growth"
        ))

        fig.add_trace(go.Scatter(
            x=list(range(years + 1)),
            y=compound_values,
            mode="lines",
            name="Compound growth"
        ))

        fig.update_layout(
            title="Simple vs compound growth",
            xaxis_title="Years",
            yaxis_title="Portfolio value (₹)"
        )

        st.plotly_chart(fig, use_container_width=True)

        st.markdown("""
        ### Why does compounding happen?

        - Your initial investment can generate returns.
        - Previous gains may also generate returns.
        - More time can allow this process to continue.
        - Compounding can also work against you with debt.

        **Important:** Returns are not guaranteed. Real investments
        can have negative years, fees and taxes.
        """)

        st.markdown("### 📝 Quick quiz")

        wealth_quiz("chapter8_l29", [
            {
                "question": "What is compounding?",
                "options": [
                    "Returns generating additional returns over time",
                    "A guaranteed profit",
                    "A bank fee",
                    "A method of avoiding all losses"
                ],
                "answer": "Returns generating additional returns over time",
                "explanation": "Compounding occurs when returns build on previous investment growth."
            },
            {
                "question": "What can increase the effect of compounding?",
                "options": [
                    "More time, assuming positive growth",
                    "Always withdrawing the gains",
                    "Never investing",
                    "Increasing every expense"
                ],
                "answer": "More time, assuming positive growth",
                "explanation": "A longer period can allow growth to compound, although actual returns are uncertain."
            }
        ])

    # --------------------------------------------------
    # LESSON 30
    # --------------------------------------------------

    elif lesson == "Lesson 30 — Time vs Money":

        st.header("📗 Lesson 30 — Time vs Money")

        st.markdown("""
        ### Two people, two starting dates

        Alex starts investing at age 20.

        Another person starts investing at age 30.

        Both invest the same monthly amount and earn
        the same hypothetical return.

        Let's compare their outcomes.
        """)

        st.markdown("### 🎮 Early vs late investing")

        monthly = st.number_input(
            "Monthly investment (₹)",
            min_value=500,
            value=2000,
            step=500
        )

        rate = st.slider(
            "Illustrative annual return (%)",
            1.0, 20.0, 10.0, 0.5,
            key="l30_rate"
        )

        early_years = st.slider(
            "Years the early investor invests",
            5, 50, 30
        )

        late_years = st.slider(
            "Years the late investor invests",
            5, 50, 20
        )

        r = rate / 100 / 12

        early_months = early_years * 12
        late_months = late_years * 12

        if r > 0:
            early_value = monthly * (
                ((1 + r) ** early_months - 1) / r
            )

            late_value = monthly * (
                ((1 + r) ** late_months - 1) / r
            )
        else:
            early_value = monthly * early_months
            late_value = monthly * late_months

        early_invested = monthly * early_months
        late_invested = monthly * late_months

        st.metric("Early investor final value", f"₹{early_value:,.2f}")
        st.metric("Late investor final value", f"₹{late_value:,.2f}")

        st.metric(
            "Early investor total contributions",
            f"₹{early_invested:,.2f}"
        )

        st.metric(
            "Late investor total contributions",
            f"₹{late_invested:,.2f}"
        )

        fig = go.Figure()

        fig.add_trace(go.Bar(
            x=["Early investor", "Late investor"],
            y=[early_value, late_value],
            text=[
                f"₹{early_value:,.0f}",
                f"₹{late_value:,.0f}"
            ],
            textposition="auto"
        ))

        fig.update_layout(
            title="Illustrative final portfolio comparison",
            yaxis_title="Portfolio value (₹)"
        )

        st.plotly_chart(fig, use_container_width=True)

        st.markdown("""
        ### What did we discover?

        The early investor had more time for growth.

        However, this is not a guaranteed outcome.
        Actual returns, contribution amounts, fees,
        taxes and market conditions can change the result.

        Starting early is helpful, but investing consistently
        and choosing an appropriate level of risk also matter.
        """)

        st.markdown("### 📝 Quick quiz")

        wealth_quiz("chapter8_l30", [
            {
                "question": "Why can starting earlier help an investor?",
                "options": [
                    "It gives investments more time to potentially compound",
                    "It guarantees profit",
                    "It eliminates market risk",
                    "It guarantees a fixed return"
                ],
                "answer": "It gives investments more time to potentially compound",
                "explanation": "A longer investment horizon can give positive returns more time to compound."
            },
            {
                "question": "Does investing earlier guarantee a higher final value?",
                "options": [
                    "Yes, in every situation",
                    "No, actual returns and contributions matter",
                    "Only for bonds",
                    "Only for mutual funds"
                ],
                "answer": "No, actual returns and contributions matter",
                "explanation": "Investment outcomes depend on returns, contributions, timing, costs and other factors."
            }
        ])

    # --------------------------------------------------
    # LESSON 31
    # --------------------------------------------------

    elif lesson == "Lesson 31 — Inflation & Purchasing Power":

        st.header("📙 Lesson 31 — Inflation & Purchasing Power")

        st.markdown("""
        ### Alex notices that prices change

        Alex remembers that a snack once cost ₹20.

        Years later, the same snack costs ₹30.

        Money still exists, but it buys fewer goods
        than before.

        This is one example of inflation.
        """)

        st.markdown("""
        <div style="padding:20px;background:#153448;
        border-radius:12px;color:white;">

        <h3>💰 ₹1,000 today</h3>

        <p>⬇️ Inflation over time ⬇️</p>

        <h3>🛒 Less purchasing power</h3>

        </div>
        """, unsafe_allow_html=True)

        st.markdown("### 🎮 Inflation calculator")

        money = st.number_input(
            "Current money (₹)",
            min_value=1000,
            value=100000,
            step=10000
        )

        inflation = st.slider(
            "Annual inflation (%)",
            1.0, 15.0, 6.0, 0.5
        )

        years = st.slider(
            "Years",
            1, 40, 10,
            key="l31_years"
        )

        future_cost = money * (
            1 + inflation / 100
        ) ** years

        purchasing_power = money / (
            1 + inflation / 100
        ) ** years

        st.metric(
            "Equivalent future cost",
            f"₹{future_cost:,.2f}"
        )

        st.metric(
            "Purchasing power of today's money in future rupees",
            f"₹{purchasing_power:,.2f}"
        )

        st.markdown("""
        ### What does this mean?

        If inflation averages 6% for 10 years,
        a product that costs ₹1,00,000 today
        would cost approximately ₹1,79,085 in 10 years.

        This is an illustration, not a forecast.

        Inflation affects different products and households
        differently. Actual inflation can vary considerably.
        """)

        fig = go.Figure()

        fig.add_trace(go.Scatter(
            x=list(range(years + 1)),
            y=[
                money / (1 + inflation / 100) ** year
                for year in range(years + 1)
            ],
            mode="lines",
            name="Purchasing power"
        ))

        fig.update_layout(
            title="Illustrative purchasing power over time",
            xaxis_title="Years",
            yaxis_title="Value in today's purchasing power (₹)"
        )

        st.plotly_chart(fig, use_container_width=True)

        st.markdown("""
        ### Why inflation matters to investors

        - Saving money alone may not preserve purchasing power.
        - Investment returns should be evaluated relative to inflation.
        - Higher returns often involve additional risks.
        - No investment guarantees beating inflation.
        """)

        st.markdown("### 📝 Quick quiz")

        wealth_quiz("chapter8_l31", [
            {
                "question": "What happens to purchasing power when prices rise?",
                "options": [
                    "It generally declines",
                    "It always increases",
                    "It stays exactly the same",
                    "It becomes guaranteed"
                ],
                "answer": "It generally declines",
                "explanation": "When prices rise, the same amount of money generally buys fewer goods and services."
            },
            {
                "question": "Why should investors consider inflation?",
                "options": [
                    "It can reduce the real value of future money",
                    "It guarantees investment returns",
                    "It prevents market losses",
                    "It eliminates taxes"
                ],
                "answer": "It can reduce the real value of future money",
                "explanation": "Inflation reduces purchasing power, so nominal returns may not represent real growth."
            }
        ])

    # --------------------------------------------------
    # LESSON 32
    # --------------------------------------------------

    elif lesson == "Lesson 32 — Building a Wealth Plan":

        st.header("📕 Lesson 32 — Building a Wealth Plan")

        st.markdown("""
        ### Alex creates a plan

        Alex now understands:

        - Stocks.
        - Bonds.
        - Mutual funds.
        - ETFs.
        - Diversification.
        - Compounding.
        - Inflation.

        But knowledge alone is not enough.

        Alex needs a practical plan.
        """)

        st.markdown("### 🧭 Step 1 — Define a goal")

        goal = st.number_input(
            "Your target amount (₹)",
            min_value=10000,
            value=1000000,
            step=50000
        )

        current = st.number_input(
            "Current savings for this goal (₹)",
            min_value=0,
            value=100000,
            step=10000
        )

        years = st.slider(
            "Years to reach the goal",
            1, 40, 10
        )

        rate = st.slider(
            "Illustrative annual return (%)",
            0.0, 20.0, 8.0, 0.5,
            key="l32_rate"
        )

        st.markdown("### 🧮 Step 2 — Estimate monthly contributions")

        months = years * 12
        monthly_rate = rate / 100 / 12

        if monthly_rate > 0:
            current_future = current * (
                1 + monthly_rate
            ) ** months

            remaining = goal - current_future

            monthly_required = max(
                0,
                remaining * monthly_rate /
                ((1 + monthly_rate) ** months - 1)
            )
        else:
            current_future = current
            remaining = goal - current_future
            monthly_required = max(
                0,
                remaining / months
            )

        st.metric(
            "Projected future value of current savings",
            f"₹{current_future:,.2f}"
        )

        st.metric(
            "Estimated monthly contribution",
            f"₹{monthly_required:,.2f}"
        )

        st.caption(
            "This estimate assumes a constant monthly return "
            "derived from the annual rate and contributions "
            "at the end of each month. Actual investment "
            "returns are variable, and the calculation "
            "does not include taxes, fees or inflation."
        )

        st.markdown("### 🧱 Step 3 — A financial foundation")

        st.write("""
        **1. Track your income and expenses**

        Understand where your money goes.

        **2. Build an emergency fund**

        Maintain accessible money for unexpected expenses.

        **3. Manage expensive debt**

        High-interest debt can make wealth building difficult.

        **4. Define your financial goals**

        Set targets, deadlines and priorities.

        **5. Invest according to your risk and time horizon**

        Different goals may require different strategies.

        **6. Review periodically**

        Avoid reacting emotionally to every market movement.
        """)

        st.markdown("### 📊 Step 4 — Your goal visualization")

        fig = go.Figure()

        fig.add_trace(go.Bar(
            x=["Target", "Current savings"],
            y=[goal, current],
            text=[
                f"₹{goal:,.0f}",
                f"₹{current:,.0f}"
            ],
            textposition="auto"
        ))

        fig.update_layout(
            title="Your financial goal",
            yaxis_title="Amount (₹)"
        )

        st.plotly_chart(fig, use_container_width=True)

        st.markdown("### 📝 Final quiz")

        wealth_quiz("chapter8_l32", [
            {
                "question": "What is a useful first step in building a wealth plan?",
                "options": [
                    "Define goals and understand your finances",
                    "Borrow as much as possible",
                    "Buy every investment available",
                    "Ignore expenses"
                ],
                "answer": "Define goals and understand your finances",
                "explanation": "Clear goals and a financial picture help determine how much to save, the time horizon and the risk that may be appropriate."
            },
            {
                "question": "Why is an emergency fund useful?",
                "options": [
                    "It helps cover unexpected expenses",
                    "It guarantees investment returns",
                    "It replaces every investment",
                    "It prevents inflation"
                ],
                "answer": "It helps cover unexpected expenses",
                "explanation": "An emergency fund can provide accessible money for unexpected needs without relying on borrowing or selling investments."
            },
            {
                "question": "Should every financial goal use the same investment strategy?",
                "options": [
                    "Yes",
                    "No, goals, time horizons and risk tolerance differ",
                    "Only if the goal is expensive",
                    "Only when inflation is zero"
                ],
                "answer": "No, goals, time horizons and risk tolerance differ",
                "explanation": "The strategy should reflect when the money is needed, the investor's risk tolerance and other constraints."
            }
        ])

        st.markdown("""
        <div style="padding:20px;background:#153448;
        border-radius:12px;color:white;">

        <h3>🎓 Chapter 8 Complete!</h3>

        <p>Alex has learned how money can grow,
        why inflation matters, how time affects
        compounding, and how to create a financial plan.</p>

        <h3>🚀 Next: Chapter 9</h3>

        </div>
        """, unsafe_allow_html=True)


