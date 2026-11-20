
import streamlit as st
import plotly.graph_objects as go


def economy_quiz(key, questions):
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


def show_chapter9():

    st.title("🏛️ Chapter 9: Banking, Central Banks & the Economy")
    st.caption("MoneyLab • Learn Money by Living It")

    st.markdown("""
    <div style="padding:20px;background:#153448;
    border-radius:12px;color:white;">

    <h3>Alex Enters the Banking World</h3>

    <p>Alex has learned how to invest, build wealth
    and understand financial markets.</p>

    <p>But Alex now asks a bigger question:</p>

    <p><b>Where does money come from, how do banks
    work, and who influences interest rates?</b></p>

    </div>
    """, unsafe_allow_html=True)

    lesson = st.selectbox(
        "Choose your lesson",
        [
            "Lesson 33 — How Commercial Banks Work",
            "Lesson 34 — What Central Banks Do",
            "Lesson 35 — Interest Rates & the Economy",
            "Lesson 36 — Inflation, Money & the Economy"
        ]
    )

    # --------------------------------------------------
    # LESSON 33
    # --------------------------------------------------

    if lesson == "Lesson 33 — How Commercial Banks Work":

        st.header("📘 Lesson 33 — How Commercial Banks Work")

        st.markdown("""
        ### The story

        Alex deposits ₹10,000 into a bank account.

        Alex now has a bank deposit.

        The bank records the deposit as a liability because
        it owes that money to Alex under the account terms.

        The bank also has assets, such as loans and reserves.

        Banks do not simply take every deposit and hand it
        directly to another person. Modern banking involves
        balance sheets, lending, payments, funding,
        liquidity and capital.
        """)

        st.markdown("### 🏦 A simplified bank balance sheet")

        st.markdown("""
        <div style="padding:20px;background:#102B3F;
        border-radius:15px;color:white;">

        <h3>Bank assets</h3>

        <p>💰 Reserves and cash</p>
        <p>📄 Loans</p>
        <p>🏦 Other assets</p>

        <hr>

        <h3>Bank liabilities</h3>

        <p>👤 Customer deposits</p>
        <p>💳 Borrowings</p>

        <hr>

        <h3>Bank equity</h3>

        <p>🛡️ Capital that absorbs losses</p>

        </div>
        """, unsafe_allow_html=True)

        st.markdown("### 📊 Balance sheet simulator")

        deposits = st.number_input(
            "Customer deposits (₹)",
            min_value=100000,
            value=1000000,
            step=100000
        )

        loans = st.number_input(
            "Bank loans (₹)",
            min_value=0,
            value=700000,
            step=50000
        )

        reserves = st.number_input(
            "Reserves and cash (₹)",
            min_value=0,
            value=200000,
            step=50000
        )

        other_assets = st.number_input(
            "Other assets (₹)",
            min_value=0,
            value=100000,
            step=50000
        )

        other_liabilities = st.number_input(
            "Other liabilities (₹)",
            min_value=0,
            value=50000,
            step=50000
        )

        total_assets = loans + reserves + other_assets

        total_liabilities = deposits + other_liabilities

        equity = total_assets - total_liabilities

        st.metric("Total assets", f"₹{total_assets:,.0f}")
        st.metric("Total liabilities", f"₹{total_liabilities:,.0f}")
        st.metric("Illustrative bank equity", f"₹{equity:,.0f}")

        fig = go.Figure()

        fig.add_trace(go.Bar(
            x=["Assets", "Liabilities + Equity"],
            y=[
                total_assets,
                total_liabilities + equity
            ],
            text=[
                f"₹{total_assets:,.0f}",
                f"₹{total_liabilities + equity:,.0f}"
            ],
            textposition="auto"
        ))

        fig.update_layout(
            title="Bank balance sheet identity",
            yaxis_title="Amount (₹)"
        )

        st.plotly_chart(fig, use_container_width=True)

        st.info(
            "In a properly constructed balance sheet, "
            "assets equal liabilities plus equity. "
            "This simulator uses simplified categories "
            "and does not represent a real bank."
        )

        st.markdown("### 🧠 How banks create money")

        st.write("""
        When a bank makes a loan, it can create a deposit
        in the borrower's account at the same time.

        For example, when a bank approves a ₹1,00,000 loan,
        it may record:

        **Bank asset:** +₹1,00,000 loan receivable.

        **Bank liability:** +₹1,00,000 deposit.

        The borrower now has a bank deposit and a debt.

        Lending is constrained by capital, liquidity,
        creditworthiness, funding, regulation, risk and
        economic conditions. Banks cannot lend without limits.
        """)

        st.markdown("### 🎮 Loan creation illustration")

        loan = st.slider(
            "New bank loan (₹)",
            10000, 1000000, 100000, 10000
        )

        fig = go.Figure()

        fig.add_trace(go.Bar(
            x=["Loan asset", "Deposit liability"],
            y=[loan, loan],
            text=[
                f"₹{loan:,.0f}",
                f"₹{loan:,.0f}"
            ],
            textposition="auto"
        ))

        fig.update_layout(
            title="Illustrative entries when a loan is created",
            yaxis_title="Amount (₹)"
        )

        st.plotly_chart(fig, use_container_width=True)

        st.caption(
            "This illustration shows two balance-sheet entries. "
            "It is not a prediction of total money supply, "
            "and actual lending and payments involve "
            "additional processes."
        )

        st.markdown("### 📝 Quick quiz")

        economy_quiz("chapter9_l33", [
            {
                "question": "When a customer deposits money into a bank, what is the deposit generally to the bank?",
                "options": [
                    "A liability",
                    "A bank profit",
                    "A stock",
                    "A tax"
                ],
                "answer": "A liability",
                "explanation": "The deposit is generally a liability because the bank owes the customer the amount under the account terms."
            },
            {
                "question": "When a commercial bank creates a new loan, what can happen?",
                "options": [
                    "A loan asset and a deposit liability can be created together",
                    "The bank automatically earns the entire loan amount",
                    "The borrower receives free money",
                    "All bank deposits disappear"
                ],
                "answer": "A loan asset and a deposit liability can be created together",
                "explanation": "Loan creation can simultaneously increase the bank's loan asset and deposit liability."
            }
        ])

    # --------------------------------------------------
    # LESSON 34
    # --------------------------------------------------

    elif lesson == "Lesson 34 — What Central Banks Do":

        st.header("📗 Lesson 34 — What Central Banks Do")

        st.markdown("""
        ### Alex discovers the central bank

        Alex discovers that countries have central banks.

        In India, the Reserve Bank of India (RBI)
        is the central bank.

        Central banks generally influence monetary conditions,
        oversee important parts of the financial system
        according to their mandates, and support financial
        stability.
        """)

        st.markdown("""
        <div style="padding:20px;background:#153448;
        border-radius:12px;color:white;">

        <h3>🏛️ Central Bank</h3>

        <p>Monetary policy</p>
        <p>💹 Interest-rate decisions</p>
        <p>💰 Liquidity operations</p>
        <p>🛡️ Financial stability responsibilities</p>
        <p>🏦 Banking oversight functions, depending on jurisdiction</p>

        </div>
        """, unsafe_allow_html=True)

        st.markdown("### What does the RBI do?")

        with st.expander("📈 Monetary policy"):
            st.write("""
            The RBI uses monetary-policy tools to influence
            financial conditions and support its policy objectives,
            including price stability.
            """)

        with st.expander("💰 Liquidity management"):
            st.write("""
            Central banks conduct operations that can
            influence liquidity in the financial system.
            """)

        with st.expander("🏦 Banking and financial system"):
            st.write("""
            The RBI has regulatory and supervisory
            responsibilities over specified financial institutions
            and activities.
            """)

        with st.expander("💵 Currency"):
            st.write("""
            The RBI has responsibilities relating to
            currency issuance and currency management
            in India, subject to the legal framework.
            """)

        with st.expander("🛡️ Financial stability"):
            st.write("""
            Central banks may work to address risks
            to the financial system and maintain confidence.
            """)

        st.markdown("### 🎮 Policy scenario")

        st.write("""
        Imagine inflation is persistently above the central bank's
        target, and the central bank decides to raise its policy rate.
        """)

        policy_rate = st.slider(
            "Illustrative policy rate (%)",
            1.0, 15.0, 6.5, 0.25
        )

        st.metric(
            "Scenario policy rate",
            f"{policy_rate:.2f}%"
        )

        if policy_rate >= 8:
            st.warning(
                "In this hypothetical scenario, the policy rate is relatively high. "
                "Higher rates can tighten financial conditions, "
                "although the impact depends on the economy."
            )
        elif policy_rate <= 4:
            st.info(
                "In this hypothetical scenario, the policy rate is relatively low. "
                "Lower rates may support borrowing and spending, "
                "but they do not guarantee economic growth."
            )
        else:
            st.success(
                "This is a hypothetical intermediate-rate scenario. "
                "The actual effects depend on the policy, "
                "economy and transmission mechanisms."
            )

        st.markdown("""
        ### The central bank is not the same as a commercial bank

        **Commercial bank:**

        - Provides bank accounts and payment services.
        - Makes loans.
        - Offers banking products.

        **Central bank:**

        - Conducts monetary policy.
        - Influences monetary and financial conditions.
        - Has responsibilities related to currency,
          financial stability and the banking system.
        """)

        st.markdown("### 📝 Quick quiz")

        economy_quiz("chapter9_l34", [
            {
                "question": "What is the central bank of India?",
                "options": [
                    "RBI",
                    "SEBI",
                    "NSE",
                    "SBI"
                ],
                "answer": "RBI",
                "explanation": "The Reserve Bank of India is India's central bank."
            },
            {
                "question": "What is one important role of a central bank?",
                "options": [
                    "Conduct monetary policy",
                    "Guarantee every stock's price",
                    "Manage every private company",
                    "Guarantee every loan"
                ],
                "answer": "Conduct monetary policy",
                "explanation": "Central banks conduct monetary policy to influence monetary and financial conditions."
            }
        ])

    # --------------------------------------------------
    # LESSON 35
    # --------------------------------------------------

    elif lesson == "Lesson 35 — Interest Rates & the Economy":

        st.header("📙 Lesson 35 — Interest Rates & the Economy")

        st.markdown("""
        ### The interest-rate chain

        Alex discovers that changes in policy rates
        can affect commercial borrowing costs.

        But the transmission is not immediate or identical
        for every borrower.
        """)

        st.markdown("""
        <div style="padding:20px;background:#102B3F;
        border-radius:15px;color:white;text-align:center;">

        <h3>🏛️ Central bank changes policy rate</h3>

        <p>⬇️</p>

        <h3>🏦 Financial conditions may change</h3>

        <p>⬇️</p>

        <h3>💳 Borrowing and saving rates may change</h3>

        <p>⬇️</p>

        <h3>🏢 Businesses and households respond</h3>

        <p>⬇️</p>

        <h3>📈📉 Economic activity and inflation may change</h3>

        </div>
        """, unsafe_allow_html=True)

        st.markdown("### 🎮 Loan-cost simulator")

        principal = st.number_input(
            "Loan amount (₹)",
            min_value=10000,
            value=500000,
            step=10000
        )

        old_rate = st.slider(
            "Original annual loan rate (%)",
            1.0, 20.0, 8.0, 0.5
        )

        new_rate = st.slider(
            "New annual loan rate (%)",
            1.0, 20.0, 10.0, 0.5
        )

        years = st.slider(
            "Loan duration (years)",
            1, 30, 10,
            key="l35_years"
        )

        def calculate_emi(p, r, n):
            monthly = r / 100 / 12
            total_months = n * 12

            if monthly == 0:
                return p / total_months

            return (
                p * monthly * (1 + monthly) ** total_months
                / ((1 + monthly) ** total_months - 1)
            )

        old_emi = calculate_emi(
            principal, old_rate, years
        )

        new_emi = calculate_emi(
            principal, new_rate, years
        )

        st.metric(
            "Original monthly EMI",
            f"₹{old_emi:,.2f}"
        )

        st.metric(
            "New monthly EMI",
            f"₹{new_emi:,.2f}"
        )

        st.metric(
            "Monthly difference",
            f"₹{new_emi - old_emi:,.2f}"
        )

        fig = go.Figure()

        fig.add_trace(go.Bar(
            x=["Original rate", "New rate"],
            y=[old_emi, new_emi],
            text=[
                f"₹{old_emi:,.0f}",
                f"₹{new_emi:,.0f}"
            ],
            textposition="auto"
        ))

        fig.update_layout(
            title="Illustrative monthly EMI comparison",
            yaxis_title="Monthly payment (₹)"
        )

        st.plotly_chart(fig, use_container_width=True)

        st.caption(
            "This assumes a fixed principal, fixed rate for the "
            "entire term and a standard amortizing loan. "
            "Actual loans may use variable rates, fees, "
            "different repayment schedules and other terms."
        )

        st.markdown("### How interest rates can affect the economy")

        st.write("""
        **Households:** Borrowing costs and saving returns may change.

        **Businesses:** Investment decisions may change.

        **Housing:** Mortgage and financing costs may change.

        **Markets:** Bonds, equities and other assets may respond.

        **Inflation:** Changes in demand and financial conditions
        can influence inflation over time.
        """)

        st.warning(
            "Interest-rate transmission is complex. "
            "Higher rates do not automatically reduce every price, "
            "and lower rates do not automatically increase "
            "every investment."
        )

        st.markdown("### 📝 Quick quiz")

        economy_quiz("chapter9_l35", [
            {
                "question": "What may happen when borrowing rates rise?",
                "options": [
                    "Borrowing may become more expensive",
                    "Every loan becomes free",
                    "Every company makes more profit",
                    "Inflation is instantly zero"
                ],
                "answer": "Borrowing may become more expensive",
                "explanation": "Higher borrowing rates can increase financing costs, depending on the loan and how rates are transmitted."
            },
            {
                "question": "Does a central bank rate change affect every loan immediately?",
                "options": [
                    "Yes, every loan instantly",
                    "No, transmission varies",
                    "Only stock loans",
                    "Only government loans"
                ],
                "answer": "No, transmission varies",
                "explanation": "Loan pricing depends on contract terms, lender decisions, market conditions and the transmission of policy rates."
            }
        ])

    # --------------------------------------------------
    # LESSON 36
    # --------------------------------------------------

    elif lesson == "Lesson 36 — Inflation, Money & the Economy":

        st.header("📕 Lesson 36 — Inflation, Money & the Economy")

        st.markdown("""
        ### Alex tries to understand inflation

        Alex discovers that inflation is a sustained increase
        in the general price level.

        Inflation is not simply one product becoming expensive.

        It can be influenced by multiple factors,
        including demand, supply, costs, expectations,
        exchange rates and monetary conditions.
        """)

        st.markdown("""
        <div style="padding:20px;background:#153448;
        border-radius:12px;color:white;">

        <h3>📈 Inflation</h3>

        <p>General prices rise over time.</p>

        <p>💰 Purchasing power may decline.</p>

        <p>🏛️ Economic policies can influence
        inflation and demand.</p>

        </div>
        """, unsafe_allow_html=True)

        st.markdown("### 🧠 Different causes of inflation")

        with st.expander("🛒 Demand-driven inflation"):
            st.write("""
            Demand for goods and services may grow faster
            than the economy's ability to supply them.
            """)

        with st.expander("🏭 Supply-driven inflation"):
            st.write("""
            Disruptions, shortages, higher production costs
            or transport costs can affect prices.
            """)

        with st.expander("🌍 Imported inflation"):
            st.write("""
            Changes in international prices and exchange rates
            can influence the domestic price of imported goods.
            """)

        with st.expander("💰 Monetary and financial conditions"):
            st.write("""
            Monetary and financial conditions can influence
            demand, expectations and inflation over time.
            Their effects depend on economic circumstances.
            """)

        st.markdown("### 🎮 Inflation scenario simulator")

        base = st.number_input(
            "Current basket of goods cost (₹)",
            min_value=1000,
            value=10000,
            step=1000
        )

        inflation_rate = st.slider(
            "Annual inflation (%)",
            0.0, 20.0, 5.0, 0.5,
            key="l36_inflation"
        )

        period = st.slider(
            "Years",
            1, 30, 10,
            key="l36_period"
        )

        future = base * (
            1 + inflation_rate / 100
        ) ** period

        st.metric(
            "Illustrative future cost",
            f"₹{future:,.2f}"
        )

        st.metric(
            "Increase in cost",
            f"₹{future - base:,.2f}"
        )

        values = [
            base * (1 + inflation_rate / 100) ** year
            for year in range(period + 1)
        ]

        fig = go.Figure()

        fig.add_trace(go.Scatter(
            x=list(range(period + 1)),
            y=values,
            mode="lines",
            name="Basket cost"
        ))

        fig.update_layout(
            title="Illustrative price-level change",
            xaxis_title="Years",
            yaxis_title="Cost (₹)"
        )

        st.plotly_chart(fig, use_container_width=True)

        st.markdown("""
        ### What can governments and central banks do?

        **Central banks:**

        - Change policy rates.
        - Conduct liquidity operations.
        - Communicate policy expectations.

        **Governments:**

        - Adjust taxation and spending.
        - Improve infrastructure.
        - Address certain supply constraints.
        - Use other economic policies.

        Different policies have different effects,
        trade-offs and time horizons.
        """)

        st.markdown("### 📝 Final quiz")

        economy_quiz("chapter9_l36", [
            {
                "question": "What is inflation?",
                "options": [
                    "A sustained increase in the general price level",
                    "A decrease in every price",
                    "A guaranteed investment return",
                    "An increase in one company's shares"
                ],
                "answer": "A sustained increase in the general price level",
                "explanation": "Inflation is a sustained increase in the general price level, which generally reduces purchasing power."
            },
            {
                "question": "Can supply disruptions contribute to inflation?",
                "options": [
                    "Yes",
                    "No, only interest rates cause inflation",
                    "Only stock markets cause inflation",
                    "Never"
                ],
                "answer": "Yes",
                "explanation": "Supply disruptions and shortages can raise prices and contribute to inflation."
            },
            {
                "question": "Does inflation always have only one cause?",
                "options": [
                    "Yes",
                    "No, it can have multiple causes",
                    "Only banks cause it",
                    "Only consumers cause it"
                ],
                "answer": "No, it can have multiple causes",
                "explanation": "Inflation can arise from demand, supply, expectations, monetary conditions and other factors."
            }
        ])

        st.markdown("""
        <div style="padding:20px;background:#153448;
        border-radius:12px;color:white;">

        <h3>🎓 Chapter 9 Complete!</h3>

        <p>Alex now understands commercial banks,
        central banks, interest rates and inflation.</p>

        <p>Alex has connected personal finance
        with the wider economy.</p>

        <h3>🚀 Next: Chapter 10</h3>

        </div>
        """, unsafe_allow_html=True)


