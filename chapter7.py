
import streamlit as st
import plotly.graph_objects as go


def fund_quiz(key, questions):
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
                    f"Why: {q['explanation']}"
                )


def show_chapter7():

    st.title("📊 Chapter 7: Mutual Funds & ETFs")
    st.caption("MoneyLab • Learn Money by Living It")

    st.markdown("""
    <div style="padding:20px;background:#153448;
    border-radius:12px;color:white;">

    <h3>Alex's Diversification Discovery</h3>

    <p>Alex now understands stocks and bonds, but buying many
    different investments requires money, research and time.</p>

    <p>Alex discovers that many investors pool their money
    together into investment funds.</p>

    </div>
    """, unsafe_allow_html=True)

    lesson = st.selectbox(
        "Choose your lesson",
        [
            "Lesson 25 — What Is a Mutual Fund?",
            "Lesson 26 — Understanding ETFs",
            "Lesson 27 — Index Funds & Diversification",
            "Lesson 28 — Fees, NAV & Fund Selection"
        ]
    )

    # --------------------------------------------------
    # LESSON 25
    # --------------------------------------------------

    if lesson == "Lesson 25 — What Is a Mutual Fund?":

        st.header("📘 Lesson 25 — What Is a Mutual Fund?")

        st.markdown("""
        ### The story

        Alex has ₹5,000 to invest.

        Alex wants to own shares in multiple companies but
        cannot individually buy and research every company.

        A mutual fund collects money from many investors
        and invests it according to its investment strategy.

        Each investor owns units of the fund.
        """)

        st.markdown("### 🧺 How pooled investing works")

        st.markdown("""
        <div style="padding:20px;background:#102B3F;
        border-radius:15px;color:white;text-align:center;">

        <h3>👤 Alex + 👤 Investor B + 👤 Investor C</h3>

        <p>⬇️ Pool their money ⬇️</p>

        <h3>🧺 Investment Fund</h3>

        <p>⬇️ Invests according to its strategy ⬇️</p>

        <h3>🏢 Stocks + 🏛️ Bonds + Other Assets</h3>

        </div>
        """, unsafe_allow_html=True)

        st.markdown("### 🧮 Pooling money simulation")

        alex = st.number_input(
            "Alex invests (₹)",
            min_value=100,
            value=5000,
            step=500
        )

        investor_b = st.number_input(
            "Investor B (₹)",
            min_value=100,
            value=10000,
            step=500
        )

        investor_c = st.number_input(
            "Investor C (₹)",
            min_value=100,
            value=15000,
            step=500
        )

        total = alex + investor_b + investor_c

        st.metric("Total pooled money", f"₹{total:,.0f}")

        fig = go.Figure(data=[go.Pie(
            labels=["Alex", "Investor B", "Investor C"],
            values=[alex, investor_b, investor_c],
            hole=0.4
        )])

        fig.update_layout(title="Contribution to the fund pool")

        st.plotly_chart(fig, use_container_width=True)

        st.markdown("""
        ### What does the fund manager do?

        A fund manager follows the fund's strategy.

        Depending on the fund, the manager may:

        - Research and select investments.
        - Manage the portfolio.
        - Monitor risk.
        - Rebalance investments.
        - Follow the fund's stated objectives.

        **Important:** Not every fund is actively managed.
        Some funds follow an index with little discretionary
        stock selection.
        """)

        st.markdown("### 📝 Quick quiz")

        fund_quiz("chapter7_l25", [
            {
                "question": "What is a mutual fund?",
                "options": [
                    "A bank loan",
                    "A pool of investors' money invested according to a strategy",
                    "A guaranteed savings account",
                    "A government tax"
                ],
                "answer": "A pool of investors' money invested according to a strategy",
                "explanation": "A mutual fund pools investor money and invests it in assets according to its objectives."
            },
            {
                "question": "What do investors typically own in a mutual fund?",
                "options": [
                    "Units of the fund",
                    "The fund manager's house",
                    "The exchange itself",
                    "A guaranteed amount of profit"
                ],
                "answer": "Units of the fund",
                "explanation": "Investors own fund units representing their share of the fund's assets."
            }
        ])

    # --------------------------------------------------
    # LESSON 26
    # --------------------------------------------------

    elif lesson == "Lesson 26 — Understanding ETFs":

        st.header("📗 Lesson 26 — Understanding ETFs")

        st.markdown("""
        ### Alex discovers ETFs

        Alex discovers another type of fund: an ETF.

        ETF stands for Exchange-Traded Fund.

        Many ETFs hold a collection of investments,
        but ETF shares generally trade on an exchange
        throughout the trading day.
        """)

        st.markdown("""
        <div style="padding:20px;background:#153448;
        border-radius:12px;color:white;">

        <h3>🧺 ETF</h3>

        <p>A collection of investments packaged into a fund.</p>

        <p>🔄 Its shares trade on an exchange during
        market hours, like stocks.</p>

        </div>
        """, unsafe_allow_html=True)

        st.markdown("### Mutual funds vs ETFs")

        comparison = {
            "Feature": [
                "Buying and selling",
                "Pricing",
                "Trading",
                "Management"
            ],
            "Mutual fund": [
                "Typically transacted through the fund",
                "Usually NAV-based",
                "Typically once per day at applicable NAV",
                "Active or passive"
            ],
            "ETF": [
                "Typically through an exchange broker",
                "Market price",
                "Trades during market hours",
                "Active or passive"
            ]
        }

        st.table(comparison)

        st.caption(
            "This is a general comparison. Fund structures, "
            "transaction processes and pricing rules vary by country and fund."
        )

        st.markdown("### 🎮 ETF market-price simulator")

        nav = st.slider(
            "ETF indicative underlying value (₹)",
            50, 500, 100
        )

        premium = st.slider(
            "Market premium / discount (%)",
            -5.0, 5.0, 0.0, 0.1
        )

        market_price = nav * (1 + premium / 100)

        st.metric("Illustrative market price", f"₹{market_price:.2f}")

        if premium > 0:
            st.warning("The ETF is trading at an illustrative premium.")
        elif premium < 0:
            st.info("The ETF is trading at an illustrative discount.")
        else:
            st.success("The ETF is trading at the illustrative underlying value.")

        st.markdown("""
        ### Why can an ETF trade at a premium or discount?

        - Supply and demand.
        - Liquidity of the ETF.
        - Liquidity of underlying assets.
        - Market volatility.
        - Trading and arbitrage conditions.

        ETF market price is not guaranteed to equal its NAV at every moment.
        """)

        st.markdown("### 📝 Quick quiz")

        fund_quiz("chapter7_l26", [
            {
                "question": "What does ETF stand for?",
                "options": [
                    "Exchange-Traded Fund",
                    "Electronic Trading Fee",
                    "Equity Transfer Formula",
                    "Extra Tax Fund"
                ],
                "answer": "Exchange-Traded Fund",
                "explanation": "ETF means Exchange-Traded Fund. ETF shares generally trade on exchanges."
            },
            {
                "question": "When can exchange-traded ETFs generally be bought and sold?",
                "options": [
                    "Only once per year",
                    "During exchange trading hours",
                    "Only after maturity",
                    "Only when the fund manager permits every individual trade"
                ],
                "answer": "During exchange trading hours",
                "explanation": "ETF shares generally trade throughout exchange trading hours, subject to market availability and trading rules."
            }
        ])

    # --------------------------------------------------
    # LESSON 27
    # --------------------------------------------------

    elif lesson == "Lesson 27 — Index Funds & Diversification":

        st.header("📙 Lesson 27 — Index Funds & Diversification")

        st.markdown("""
        ### Alex learns about indexes

        Alex discovers that some funds attempt to track an index.

        An index measures the performance of a group
        of securities according to a defined methodology.

        For example, an index might represent large companies
        in a particular country or a particular sector.
        """)

        st.markdown("""
        <div style="padding:20px;background:#153448;
        border-radius:12px;color:white;">

        <h3>📈 Index</h3>

        <p>A measurement of a selected group of investments.</p>

        <h3>🧺 Index fund</h3>

        <p>A fund designed to track the performance
        of a specified index.</p>

        </div>
        """, unsafe_allow_html=True)

        st.markdown("### 🌍 Diversification")

        st.write("""
        Diversification means spreading investments across
        different assets, companies, sectors or markets
        to reduce the impact of individual risks.
        """)

        st.markdown("### 🎮 Concentration vs diversification simulation")

        investment = st.number_input(
            "Total portfolio (₹)",
            min_value=1000,
            value=10000,
            step=1000
        )

        loss = st.slider(
            "One investment declines (%)",
            0, 100, 50
        )

        st.markdown("#### Portfolio A — Entire amount in one company")

        concentrated_loss = investment * loss / 100

        st.metric(
            "Loss if the investment declines",
            f"₹{concentrated_loss:,.0f}"
        )

        st.markdown("#### Portfolio B — Equal allocation across 10 companies")

        exposure = investment / 10

        diversified_loss = exposure * loss / 100

        st.metric(
            "Loss if only one company declines",
            f"₹{diversified_loss:,.0f}"
        )

        st.info(
            "This simulation assumes the other nine investments "
            "remain unchanged. Real portfolios can decline together. "
            "Diversification reduces some risks but does not guarantee "
            "profit or prevent losses."
        )

        fig = go.Figure()

        fig.add_trace(go.Bar(
            x=["Concentrated portfolio", "Diversified portfolio"],
            y=[concentrated_loss, diversified_loss],
            text=[
                f"₹{concentrated_loss:,.0f}",
                f"₹{diversified_loss:,.0f}"
            ],
            textposition="auto"
        ))

        fig.update_layout(
            title="Illustrative losses from one company decline",
            yaxis_title="Loss (₹)"
        )

        st.plotly_chart(fig, use_container_width=True)

        st.markdown("""
        ### Diversification does not mean owning everything

        A portfolio can still be concentrated if it owns:

        - Many companies in the same industry.
        - Similar investments that move together.
        - Mostly one country.
        - Mostly one asset class.

        True diversification considers how investments
        behave together, not just how many are owned.
        """)

        st.markdown("### 📝 Quick quiz")

        fund_quiz("chapter7_l27", [
            {
                "question": "What is the primary purpose of diversification?",
                "options": [
                    "Guarantee profit",
                    "Reduce exposure to individual investment risks",
                    "Prevent all market declines",
                    "Always outperform an index"
                ],
                "answer": "Reduce exposure to individual investment risks",
                "explanation": "Diversification spreads exposure so one investment has less influence on the overall portfolio."
            },
            {
                "question": "What is an index fund designed to do?",
                "options": [
                    "Guarantee a fixed return",
                    "Track a specified index",
                    "Avoid every loss",
                    "Always buy the cheapest stock"
                ],
                "answer": "Track a specified index",
                "explanation": "Index funds generally seek to track the performance of an index, subject to tracking differences."
            }
        ])

    # --------------------------------------------------
    # LESSON 28
    # --------------------------------------------------

    elif lesson == "Lesson 28 — Fees, NAV & Fund Selection":

        st.header("📕 Lesson 28 — Fees, NAV & Fund Selection")

        st.markdown("""
        ### Alex discovers that fees matter

        Two funds may invest in similar assets,
        but charge different fees.

        Over time, fees can affect the amount
        of money an investor keeps.
        """)

        st.markdown("### 🧮 Fee impact calculator")

        amount = st.number_input(
            "Initial investment (₹)",
            min_value=1000,
            value=100000,
            step=10000
        )

        annual_return = st.slider(
            "Illustrative annual return before fees (%)",
            1.0, 20.0, 10.0, 0.5
        )

        fee = st.slider(
            "Annual fund fee (%)",
            0.0, 3.0, 1.0, 0.1
        )

        period = st.slider(
            "Investment duration (years)",
            1, 40, 20
        )

        before_fee = amount * (
            1 + annual_return / 100
        ) ** period

        after_fee = amount * (
            1 + (annual_return - fee) / 100
        ) ** period

        difference = before_fee - after_fee

        st.metric(
            "Illustrative value without fee",
            f"₹{before_fee:,.2f}"
        )

        st.metric(
            "Illustrative value with fee",
            f"₹{after_fee:,.2f}"
        )

        st.metric(
            "Illustrative difference",
            f"₹{difference:,.2f}"
        )

        fig = go.Figure()

        fig.add_trace(go.Bar(
            x=["Without fee", "With fee"],
            y=[before_fee, after_fee],
            text=[
                f"₹{before_fee:,.0f}",
                f"₹{after_fee:,.0f}"
            ],
            textposition="auto"
        ))

        fig.update_layout(
            title="Illustrative long-term fee impact",
            yaxis_title="Portfolio value (₹)"
        )

        st.plotly_chart(fig, use_container_width=True)

        st.caption(
            "This simplified calculator assumes constant annual returns "
            "and annual fee deductions modeled by subtracting the fee "
            "from the return. Actual fund fees, returns, taxes, timing "
            "and compounding differ."
        )

        st.markdown("### What is NAV?")

        st.write("""
        NAV stands for Net Asset Value.

        It generally represents the value of a fund's assets
        minus liabilities, divided by the number of units
        outstanding.

        NAV per unit is not, by itself, a measure of whether
        a fund is cheap or expensive.
        """)

        st.markdown("### 🎮 NAV calculator")

        assets = st.number_input(
            "Fund assets (₹)",
            min_value=1000,
            value=1000000,
            step=100000
        )

        liabilities = st.number_input(
            "Fund liabilities (₹)",
            min_value=0,
            value=50000,
            step=10000
        )

        units = st.number_input(
            "Units outstanding",
            min_value=1,
            value=95000,
            step=1000
        )

        nav = (assets - liabilities) / units

        st.metric("Illustrative NAV per unit", f"₹{nav:.2f}")

        st.markdown("### 🔍 What should investors evaluate?")

        st.write("**Investment objective:** What is the fund designed to hold?")
        st.write("**Fees:** What costs are charged?")
        st.write("**Risk:** What can cause losses?")
        st.write("**Diversification:** How concentrated is the portfolio?")
        st.write("**Tracking difference:** How closely does an index fund track its benchmark?")
        st.write("**Liquidity:** Can units be bought or sold reasonably?")
        st.write("**Fund manager and process:** Are the strategy and management consistent?")
        st.write("**Time horizon:** Does the fund suit the investor's needs?")

        st.markdown("### 📝 Final quiz")

        fund_quiz("chapter7_l28", [
            {
                "question": "What does NAV generally represent?",
                "options": [
                    "The fund's guaranteed future return",
                    "Net assets divided by units outstanding",
                    "The fund's annual fee",
                    "The price of every stock in the market"
                ],
                "answer": "Net assets divided by units outstanding",
                "explanation": "NAV per unit is generally net fund assets divided by the number of units outstanding."
            },
            {
                "question": "Why can higher fund fees matter?",
                "options": [
                    "They always improve returns",
                    "They can reduce the amount investors retain over time",
                    "They guarantee lower risk",
                    "They prevent compounding"
                ],
                "answer": "They can reduce the amount investors retain over time",
                "explanation": "Fees reduce the investment return available to investors and can compound over time."
            },
            {
                "question": "Does a lower NAV automatically make a fund cheaper?",
                "options": [
                    "Yes, always",
                    "No, NAV alone doesn't indicate value or cheapness",
                    "Only for ETFs",
                    "Only for index funds"
                ],
                "answer": "No, NAV alone doesn't indicate value or cheapness",
                "explanation": "NAV per unit depends on the fund's assets and unit count. A lower NAV doesn't mean the underlying investments are cheaper."
            }
        ])

        st.markdown("""
        <div style="padding:20px;background:#153448;
        border-radius:12px;color:white;">

        <h3>🎓 Chapter 7 Complete!</h3>

        <p>Alex now understands mutual funds, ETFs,
        index funds, diversification, NAV and fees.</p>

        <p>Alex has learned that investing is not only
        about choosing assets, but also about building
        a portfolio and understanding costs.</p>

        <h3>🚀 Next: Chapter 8</h3>

        </div>
        """, unsafe_allow_html=True)


