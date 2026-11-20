import streamlit as st


def lesson8():

    if "l8_scene" not in st.session_state:
        st.session_state.l8_scene = 0

    scene = st.session_state.l8_scene

    st.markdown("""
    <style>
    @keyframes float {
        0%,100% {transform:translateY(0);}
        50% {transform:translateY(-10px);}
    }
    @keyframes appear {
        from {opacity:0;transform:translateY(15px);}
        to {opacity:1;transform:translateY(0);}
    }
    .character {
        font-size:90px;
        text-align:center;
        animation:float 2s infinite;
    }
    .storybox {
        background:linear-gradient(135deg,#172554,#1e3a8a);
        padding:24px;
        border-radius:18px;
        color:white;
        animation:appear 0.7s;
    }
    .info-box {
        background:#172033;
        padding:20px;
        border-radius:15px;
        border:1px solid #334155;
        color:white;
        animation:appear 0.7s;
    }
    .warning-box {
        background:#451a03;
        padding:20px;
        border-radius:15px;
        border:2px solid #f59e0b;
        color:#fde68a;
    }
    .success-box {
        background:#14532d;
        padding:20px;
        border-radius:15px;
        color:#dcfce7;
    }
    .money-box {
        background:#123524;
        padding:20px;
        border-radius:15px;
        text-align:center;
        color:#86efac;
        font-size:25px;
        font-weight:bold;
    }
    </style>
    """, unsafe_allow_html=True)

    st.title("🧭 Lesson 8 — The Investor's Decision")
    st.caption("MoneyLab • Learn Money by Living It")

    st.progress((scene + 1) / 8)
    st.caption(f"Scene {scene + 1} of 8")

    # SCENE 0: CONNECT TO LESSON 7

    if scene == 0:

        st.markdown(
            '<div class="character">🧑</div>',
            unsafe_allow_html=True
        )

        st.markdown("""
        <div class="storybox">
        <h2>Alex has learned about risk!</h2>
        <h3>But how does he actually choose an investment?</h3>
        </div>
        """, unsafe_allow_html=True)

        st.write("""
        In Lesson 7, Alex learned:

        - Investments can lose money.
        - Returns are not guaranteed.
        - Diversification can reduce concentration risk.
        - Suspicious promises can be dangerous.

        But knowing about risk is not enough.

        Alex must learn how to make a sensible
        investment decision.
        """)

        st.markdown("""
        <div class="warning-box">
        <h3>Alex's new question:</h3>

        How do I decide where my money should go?
        </div>
        """, unsafe_allow_html=True)

        st.info("""
        Lesson 7: Understand the risk.

        Lesson 8: Make a thoughtful investment decision.
        """)

    # SCENE 1: INVESTMENT GOALS

    elif scene == 1:

        st.markdown(
            '<div class="character">🎯</div>',
            unsafe_allow_html=True
        )

        st.markdown("## Step 1 — Know your goal")

        st.write("""
        Alex has ₹20,000.

        Before choosing an investment,
        he must decide why he wants to invest.
        """)

        st.markdown("""
        <div class="info-box">
        <h3>Goal A — A new laptop</h3>

        Alex wants to buy a laptop in 6 months.
        </div>
        """, unsafe_allow_html=True)

        st.markdown("""
        <div class="info-box">
        <h3>Goal B — Higher education</h3>

        Alex wants to save money for education
        in 5 years.
        </div>
        """, unsafe_allow_html=True)

        st.markdown("""
        <div class="info-box">
        <h3>Goal C — Retirement</h3>

        Alex wants to build wealth for a future
        that is several decades away.
        </div>
        """, unsafe_allow_html=True)

        st.markdown("### Why does the goal matter?")

        st.write("""
        The goal influences how much risk someone
        may be able to take, how much money they
        need, and when they need it.

        A person saving for something in 6 months
        may need a different approach from someone
        investing for decades.
        """)

        st.markdown("""
        <div class="success-box">
        <b>First rule:</b> Define the financial goal
        before selecting an investment.
        </div>
        """, unsafe_allow_html=True)

    # SCENE 2: TIME HORIZON

    elif scene == 2:

        st.markdown(
            '<div class="character">⏳</div>',
            unsafe_allow_html=True
        )

        st.markdown("## Step 2 — Understand time")

        st.write("""
        Time horizon means the length of time
        you expect to keep money invested
        before needing it.
        """)

        st.markdown("""
        <div class="info-box">
        <h3>Short-term</h3>

        You may need your money soon.

        <p>Example: A laptop purchase in 6 months.</p>
        </div>
        """, unsafe_allow_html=True)

        st.markdown("""
        <div class="info-box">
        <h3>Medium-term</h3>

        You may need your money in a few years.

        <p>Example: A future education expense.</p>
        </div>
        """, unsafe_allow_html=True)

        st.markdown("""
        <div class="info-box">
        <h3>Long-term</h3>

        You may not need your money for many years.

        <p>Example: Retirement planning.</p>
        </div>
        """, unsafe_allow_html=True)

        st.markdown("### Why does time matter?")

        st.write("""
        Investments that fluctuate in value may be
        unsuitable for money you need very soon.

        If the investment falls shortly before
        you need the money, you may have to sell
        at a loss.

        A longer time horizon may allow someone
        to tolerate more fluctuations, but it does
        not guarantee recovery or profit.
        """)

        st.warning("""
        Time alone does not make a risky investment safe.
        """)

    # SCENE 3: EMERGENCY SAVINGS

    elif scene == 3:

        st.markdown(
            '<div class="character">🛟</div>',
            unsafe_allow_html=True
        )

        st.markdown("## Step 3 — Protect your emergency money")

        st.write("""
        Alex has ₹20,000.

        But he has no emergency savings.

        What if he suddenly needs money
        for medical expenses, repairs or an emergency?
        """)

        st.markdown("""
        <div class="warning-box">
        <h3>Unexpected expense!</h3>

        Alex suddenly needs ₹5,000.
        </div>
        """, unsafe_allow_html=True)

        st.write("""
        If all his money is invested in something
        that has fallen in value or cannot easily
        be withdrawn, he may face a problem.
        """)

        st.markdown("### What are emergency savings?")

        st.write("""
        Emergency savings are money set aside
        for unexpected expenses.

        They are generally kept somewhere
        accessible and relatively stable,
        rather than exposed to large market
        fluctuations.
        """)

        st.markdown("""
        <div class="success-box">
        Emergency savings help reduce the chance
        of being forced to sell investments
        at an unfavorable time.
        </div>
        """, unsafe_allow_html=True)

        st.markdown("### How much should someone save?")

        st.write("""
        A common planning target is several months
        of essential expenses, but the appropriate
        amount depends on income stability,
        obligations, insurance, dependents
        and personal circumstances.

        It is not a universal fixed number.
        """)

    # SCENE 4: RESEARCH

    elif scene == 4:

        st.markdown(
            '<div class="character">🔎</div>',
            unsafe_allow_html=True
        )

        st.markdown("## Step 4 — Research before investing")

        st.write("""
        Alex discovers an investment he has never
        heard about.

        Instead of immediately buying it,
        he investigates.
        """)

        st.markdown("### What should he investigate?")

        st.markdown("""
        <div class="info-box">
        <h3>1. What am I investing in?</h3>

        Understand what the product actually owns,
        does or represents.
        </div>
        """, unsafe_allow_html=True)

        st.markdown("""
        <div class="info-box">
        <h3>2. How can I make or lose money?</h3>

        Understand how returns are generated
        and what could cause losses.
        </div>
        """, unsafe_allow_html=True)

        st.markdown("""
        <div class="info-box">
        <h3>3. Who is offering it?</h3>

        Verify the provider, company and relevant
        registration or regulatory status
        independently where applicable.
        </div>
        """, unsafe_allow_html=True)

        st.markdown("""
        <div class="info-box">
        <h3>4. Can I withdraw my money?</h3>

        Understand withdrawal restrictions,
        lock-in periods and liquidity.
        </div>
        """, unsafe_allow_html=True)

        st.markdown("""
        <div class="info-box">
        <h3>5. What could go wrong?</h3>

        Consider losses, fraud, market risk,
        credit risk and other risks relevant
        to the investment.
        </div>
        """, unsafe_allow_html=True)

        st.markdown("""
        <div class="success-box">
        Research is not about finding a guarantee.

        It is about understanding what you are buying
        and the risks involved.
        </div>
        """, unsafe_allow_html=True)

    # SCENE 5: FEES

    elif scene == 5:

        st.markdown(
            '<div class="character">🧾</div>',
            unsafe_allow_html=True
        )

        st.markdown("## Step 5 — Understand investment costs")

        st.write("""
        Alex finds two investment products
        with similar investments.

        But they charge different fees.
        """)

        st.markdown("""
        <div class="info-box">
        <h3>Investment A</h3>

        Annual cost: 0.2%
        </div>
        """, unsafe_allow_html=True)

        st.markdown("""
        <div class="info-box">
        <h3>Investment B</h3>

        Annual cost: 1.5%
        </div>
        """, unsafe_allow_html=True)

        st.write("""
        Suppose both investments have ₹1,00,000
        invested and the fee is calculated
        on that amount for one year.
        """)

        st.markdown("""
        <div class="success-box">
        Investment A

        0.2% of ₹1,00,000 = ₹200 per year
        </div>
        """, unsafe_allow_html=True)

        st.markdown("""
        <div class="warning-box">
        Investment B

        1.5% of ₹1,00,000 = ₹1,500 per year
        </div>
        """, unsafe_allow_html=True)

        st.markdown("### Why are fees important?")

        st.write("""
        Costs reduce the money available
        to remain invested.

        Over many years, repeated fees can
        significantly affect investment growth.
        """)

        st.markdown("### Try a cost calculator")

        amount = st.number_input(
            "Investment amount (₹)",
            min_value=1000,
            max_value=10000000,
            value=100000,
            step=1000,
            key="l8_fee_amount"
        )

        fee = st.slider(
            "Annual fee (%)",
            min_value=0.0,
            max_value=3.0,
            value=1.0,
            step=0.1,
            key="l8_fee_rate"
        )

        annual_cost = amount * fee / 100

        st.markdown("""
        <div class="money-box">
        """, unsafe_allow_html=True)

        st.metric("Estimated annual fee", f"₹{annual_cost:,.2f}")

        st.write("""
        This is a simplified fee calculation
        using the starting investment amount.

        Actual fees may be calculated differently
        and may include additional charges.
        """)

    # SCENE 6: ALEX MAKES A DECISION

    elif scene == 6:

        st.markdown(
            '<div class="character">🧭</div>',
            unsafe_allow_html=True
        )

        st.markdown("## Alex's investment decision")

        st.write("""
        Alex has ₹20,000.

        He wants to buy a laptop in 6 months.

        He sees an investment that can lose
        30% or more in a market decline.

        He has not yet built emergency savings.

        What should he consider first?
        """)

        choice = st.radio(
            "What would be the most sensible first step?",
            [
                "A. Invest all ₹20,000 immediately",
                "B. Understand his goal, protect needed money "
                "and research suitable options",
                "C. Borrow more money and invest",
                "D. Invest because someone said the returns are guaranteed"
            ],
            key="l8_decision"
        )

        if st.button("Evaluate My Decision", key="l8_decision_button"):

            st.session_state.l8_decision_result = choice

        if "l8_decision_result" in st.session_state:

            result = st.session_state.l8_decision_result

            if result == choice:

                st.markdown("---")

                if result.startswith("B."):

                    st.success("A thoughtful approach!")

                    st.write("""
                    Alex should first understand his financial
                    goal, the time horizon, emergency needs,
                    the investment risks and available options.

                    Since he needs the laptop in 6 months,
                    he should be cautious about exposing
                    the money to investments that may
                    lose value over that period.
                    """)

                elif result.startswith("A."):

                    st.error("This decision is too hasty.")

                    st.write("""
                    Investing all the money immediately
                    ignores the 6-month goal and the
                    lack of emergency savings.

                    A market decline could leave Alex
                    with less money when he needs
                    to buy the laptop.
                    """)

                elif result.startswith("C."):

                    st.error("Borrowing adds another risk.")

                    st.write("""
                    Borrowing creates a repayment obligation.

                    If the investment loses value,
                    Alex may still owe the loan
                    and its interest.
                    """)

                else:

                    st.error("A guarantee is not proof.")

                    st.write("""
                    Promises of guaranteed returns
                    do not prove an investment is safe.

                    Alex should investigate the offer
                    independently and be especially
                    cautious about unrealistic promises.
                    """)

                st.markdown("### The reasoning")

                st.write("""
                A good investment decision starts
                with the financial goal, the time horizon,
                financial circumstances, risks, costs
                and reliable information.

                The investment itself is not the first step.
                """)

    # SCENE 7: FINAL QUIZ

    elif scene == 7:

        st.markdown(
            '<div class="character">🏆</div>',
            unsafe_allow_html=True
        )

        st.markdown("## Final Challenge")

        st.write("""
        Let's see whether Alex has learned
        how to make better investment decisions.
        """)

        q1 = st.radio(
            "1. Why should someone define a financial goal "
            "before investing?",
            [
                "A. Every investment guarantees success",
                "B. The goal helps determine the time horizon "
                "and needs",
                "C. Goals eliminate risk"
            ],
            key="l8_q1"
        )

        q2 = st.radio(
            "2. Why can emergency savings be useful?",
            [
                "A. They guarantee wealth",
                "B. They prevent every financial problem",
                "C. They help cover unexpected expenses "
                "without being forced to sell investments"
            ],
            key="l8_q2"
        )

        q3 = st.radio(
            "3. Why should investors understand fees?",
            [
                "A. Fees can reduce investment returns",
                "B. Fees always increase profits",
                "C. Fees do not matter"
            ],
            key="l8_q3"
        )

        q4 = st.radio(
            "4. What should someone do before investing "
            "in an unfamiliar product?",
            [
                "A. Trust the advertisement",
                "B. Send money immediately",
                "C. Research the product, provider, risks "
                "and costs"
            ],
            key="l8_q4"
        )

        answers = (q1, q2, q3, q4)

        if st.button("Check My Answers", key="l8_quiz_check"):

            st.session_state.l8_checked_answers = answers

        if (
            "l8_checked_answers" in st.session_state
            and st.session_state.l8_checked_answers == answers
        ):

            selected = st.session_state.l8_checked_answers

            correct = [
                "B. The goal helps determine the time horizon and needs",
                "C. They help cover unexpected expenses without being forced to sell investments",
                "A. Fees can reduce investment returns",
                "C. Research the product, provider, risks and costs"
            ]

            explanations = [

                {
                    "A. Every investment guarantees success":
                    (
                        "Incorrect. Investments do not guarantee "
                        "success. Goals help investors plan "
                        "for what the money is intended to do."
                    ),

                    correct[0]:
                    (
                        "Correct! Goals help determine when "
                        "money is needed, how much is required "
                        "and what types of risks may be appropriate."
                    ),

                    "C. Goals eliminate risk":
                    (
                        "Incorrect. A goal does not eliminate risk. "
                        "It helps someone make decisions that "
                        "better match their financial needs."
                    )
                },

                {
                    "A. They guarantee wealth":
                    (
                        "Incorrect. Emergency savings do not "
                        "guarantee wealth. They provide money "
                        "for unexpected needs."
                    ),

                    "B. They prevent every financial problem":
                    (
                        "Incorrect. Emergency savings cannot "
                        "prevent all financial problems, "
                        "but they can help manage unexpected costs."
                    ),

                    correct[1]:
                    (
                        "Correct! Accessible emergency savings "
                        "can help someone pay unexpected expenses "
                        "without needing to sell investments "
                        "at an unfavorable time."
                    )
                },

                {
                    correct[2]:
                    (
                        "Correct! Fees reduce the amount of money "
                        "that remains invested or the returns "
                        "available to the investor."
                    ),

                    "B. Fees always increase profits":
                    (
                        "Incorrect. Fees are costs. They do not "
                        "guarantee profits and generally reduce "
                        "the investor's returns."
                    ),

                    "C. Fees do not matter":
                    (
                        "Incorrect. Fees can accumulate over time "
                        "and affect investment growth."
                    )
                },

                {
                    "A. Trust the advertisement":
                    (
                        "Incorrect. Advertisements may omit "
                        "important risks or costs. Independent "
                        "verification is important."
                    ),

                    "B. Send money immediately":
                    (
                        "Incorrect. Rushing without understanding "
                        "the investment can expose someone "
                        "to unnecessary risks or fraud."
                    ),

                    correct[3]:
                    (
                        "Correct! Investors should understand "
                        "what they are buying, who is offering it, "
                        "the risks, fees and withdrawal conditions."
                    )
                }
            ]

            score = sum(
                selected[i] == correct[i]
                for i in range(4)
            )

            st.markdown("---")
            st.subheader(f"Your score: {score}/4")

            for i in range(4):

                answer = selected[i]

                if answer == correct[i]:

                    st.success(f"Question {i + 1}: Correct!")

                else:

                    st.error(f"Question {i + 1}: Incorrect.")

                st.markdown(f"**Your answer:** {answer}")

                st.markdown(f"**Correct answer:** {correct[i]}")

                st.write(explanations[i][answer])

                st.markdown("---")

            if score == 4:

                st.success("""
                Excellent! You understand the basics
                of making thoughtful investment decisions.
                """)

            elif score >= 2:

                st.info("""
                Good work! Review the explanations
                for the questions you missed.
                """)

            else:

                st.info("""
                Review the lesson and explanations.
                Understanding the reasoning is more
                important than memorizing answers.
                """)

            st.markdown("""
            <div class="storybox">
            <h2>Lesson 8 Completed!</h2>

            <h3>Alex now knows how to think
            before investing.</h3>

            <p>Goals, time, emergency savings,
            research and costs all matter.</p>

            <h2>🔓 Next: Lesson 9</h2>
            </div>
            """, unsafe_allow_html=True)

    # NAVIGATION

    st.markdown("---")

    col1, col2 = st.columns(2)

    with col1:

        if scene > 0:

            if st.button("⬅️ Previous Scene", key="l8_prev"):

                st.session_state.l8_scene -= 1
                st.rerun()

    with col2:

        if scene < 7:

            if st.button("Next Scene ➡️", key="l8_next"):

                st.session_state.l8_scene += 1
                st.rerun()

    st.caption("MoneyLab • Chapter 1 • Lesson 8")
