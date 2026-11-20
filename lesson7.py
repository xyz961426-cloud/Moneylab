import streamlit as st

def lesson7():

    if "l7_scene" not in st.session_state:
        st.session_state.l7_scene = 0

    scene = st.session_state.l7_scene

    st.markdown("""
    <style>
    @keyframes float {
        0%,100% {transform:translateY(0px);}
        50% {transform:translateY(-12px);}
    }
    @keyframes appear {
        from {opacity:0;transform:translateY(15px);}
        to {opacity:1;transform:translateY(0);}
    }
    @keyframes glow {
        0%,100% {box-shadow:0 0 5px #f59e0b;}
        50% {box-shadow:0 0 20px #f59e0b;}
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
    .loss-box {
        background:#450a0a;
        padding:20px;
        border-radius:15px;
        color:#fecaca;
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
    .scene-heading {
        animation:appear 0.7s;
    }
    </style>
    """, unsafe_allow_html=True)

    st.title("🎯 Lesson 7 — The Risk Trap")
    st.caption("MoneyLab • Learn Money by Living It")

    st.progress((scene + 1) / 8)
    st.caption(f"Scene {scene + 1} of 8")

    # SCENE 0: CONNECTION WITH LESSON 6

    if scene == 0:

        st.markdown('<div class="character">🧑</div>',
                    unsafe_allow_html=True)

        st.markdown("""
        <div class="storybox">
        <h2>Meet Alex again!</h2>
        <h3>Alex is ready to invest.</h3>
        </div>
        """, unsafe_allow_html=True)

        st.write("""
        In Lesson 6, Alex learned that investing can help
        money grow over time.

        He now understands that investing can be a way
        to build wealth.

        But today, Alex has a new question:
        """)

        st.markdown("""
        <div class="warning-box">
        <h3>Can investments also make me lose money?</h3>
        </div>
        """, unsafe_allow_html=True)

        st.markdown("### The new problem")

        st.write("""
        Alex has ₹10,000.

        He wants to invest it, but he doesn't understand
        what could happen if the investment performs badly.

        Before investing, he needs to learn something
        important: **risk**.
        """)

        st.info("""
        Lesson 6: How money can grow.

        Lesson 7: What can go wrong when we invest?
        """)

    # SCENE 1: UNDERSTANDING RISK

    elif scene == 1:

        st.markdown('<div class="character">⚖️</div>',
                    unsafe_allow_html=True)

        st.markdown("## What is investment risk?")

        st.write("""
        Imagine you invest ₹10,000 in an investment
        whose value changes with the market.
        """)

        st.markdown("""
        <div class="money-box">
        Starting Investment: ₹10,000
        </div>
        """, unsafe_allow_html=True)

        st.markdown("### Three possible outcomes")

        st.markdown("""
        <div class="success-box">
        <h3>📈 Outcome A</h3>
        <h2>₹12,000</h2>
        <p>Your investment increases.</p>
        </div>
        """, unsafe_allow_html=True)

        st.markdown("""
        <div class="info-box">
        <h3>➖ Outcome B</h3>
        <h2>₹10,000</h2>
        <p>Your investment stays at the same value.</p>
        </div>
        """, unsafe_allow_html=True)

        st.markdown("""
        <div class="loss-box">
        <h3>📉 Outcome C</h3>
        <h2>₹8,000</h2>
        <p>Your investment decreases.</p>
        </div>
        """, unsafe_allow_html=True)

        st.markdown("### Why can this happen?")

        st.write("""
        Investment prices can change because of:

        - Company profits or losses.
        - Economic conditions.
        - Interest rates.
        - Investor expectations.
        - Unexpected events.

        """)

        st.markdown("""
        <div class="warning-box">
        <b>Risk means uncertainty about an outcome.</b>

        An investment may perform better or worse
        than expected. Risk does not mean that a loss
        will definitely happen.
        </div>
        """, unsafe_allow_html=True)

    # SCENE 2: DIFFERENT INVESTMENTS

    elif scene == 2:

        st.markdown('<div class="character">🏦</div>',
                    unsafe_allow_html=True)

        st.markdown("## Different investments, different risks")

        st.write("""
        Alex discovers that not every investment
        behaves in the same way.
        """)

        st.markdown("""
        <div class="info-box">
        <h3>🛡️ Option A — Bank Deposit</h3>

        A bank deposit may offer a relatively predictable
        interest rate, subject to the product's terms.

        <p>Risks can include inflation, bank-related risk
        beyond applicable protections, and restrictions
        on withdrawals.</p>
        </div>
        """, unsafe_allow_html=True)

        st.markdown("""
        <div class="info-box">
        <h3>📊 Option B — Diversified Stock Fund</h3>

        It invests in many companies.

        <p>Its value may rise or fall with the market.
        Diversification may reduce company-specific risk,
        but market losses are still possible.</p>
        </div>
        """, unsafe_allow_html=True)

        st.markdown("""
        <div class="info-box">
        <h3>🚀 Option C — Single Company Stock</h3>

        You invest in one company's shares.

        <p>If that company performs well, the shares
        may increase in value. If the company struggles,
        the shares may lose significant value.</p>
        </div>
        """, unsafe_allow_html=True)

        st.markdown("### What should Alex understand?")

        st.write("""
        Different investments have different risks,
        liquidity, costs, and expected returns.

        An investment that is relatively less risky
        is not automatically suitable for everyone.

        Alex must understand the product before
        deciding where to put his money.
        """)

    # SCENE 3: PROFIT AND LOSS SIMULATOR

    elif scene == 3:

        st.markdown('<div class="character">🎮</div>',
                    unsafe_allow_html=True)

        st.markdown("## Alex's Investment Simulator")

        st.write("""
        Alex invests ₹10,000.

        Choose a possible outcome to see how his
        investment value changes.
        """)

        outcome = st.selectbox(
            "Choose a simulated market outcome:",
            [
                "Market rises by 20%",
                "Market rises by 5%",
                "Market falls by 20%",
                "Market falls by 50%"
            ],
            key="l7_sim_choice"
        )

        if st.button("Simulate Outcome", key="l7_sim_button"):

            changes = {
                "Market rises by 20%": 0.20,
                "Market rises by 5%": 0.05,
                "Market falls by 20%": -0.20,
                "Market falls by 50%": -0.50
            }

            change = changes[outcome]

            result = round(10000 * (1 + change))

            st.session_state.l7_sim_result = {
                "choice": outcome,
                "value": result,
                "change": change
            }

        if "l7_sim_result" in st.session_state:

            sim = st.session_state.l7_sim_result

            if sim["choice"] == outcome:

                value = sim["value"]

                st.markdown("---")

                if value > 10000:

                    st.success("📈 The investment increased!")

                    st.markdown(f"""
                    <div class="money-box">
                    Investment Value: ₹{value:,}
                    </div>
                    """, unsafe_allow_html=True)

                    st.write(f"""
                    Initial investment: ₹10,000

                    Current simulated value: ₹{value:,}

                    **Profit: ₹{value - 10000:,}**
                    """)

                elif value < 10000:

                    st.error("📉 The investment decreased!")

                    st.markdown(f"""
                    <div class="loss-box">
                    Investment Value: ₹{value:,}
                    </div>
                    """, unsafe_allow_html=True)

                    st.write(f"""
                    Initial investment: ₹10,000

                    Current simulated value: ₹{value:,}

                    **Loss: ₹{10000 - value:,}**
                    """)

                else:

                    st.info("The investment has not changed.")

                st.markdown("### What does this teach us?")

                st.write("""
                Investment returns are uncertain.

                You cannot assume that an investment
                will always increase in value.

                A loss means the value of your investment
                has decreased. If you sell at that value,
                the loss becomes realized, before considering
                any costs or taxes.
                """)

                st.caption(
                    "Illustrative simulation, not a forecast."
                )

    # SCENE 4: DIVERSIFICATION

    elif scene == 4:

        st.markdown('<div class="character">🧺</div>',
                    unsafe_allow_html=True)

        st.markdown("## Don't put everything in one basket")

        st.write("""
        Alex has ₹10,000.

        He considers investing the entire amount
        in one company.
        """)

        st.markdown("""
        <div class="loss-box">
        <h2>₹10,000 → One Company</h2>
        </div>
        """, unsafe_allow_html=True)

        st.write("""
        Imagine that the company faces serious problems.

        Its share price drops by 50%.
        """)

        st.markdown("""
        <div class="loss-box">
        <h2>₹10,000 → ₹5,000</h2>
        <h3>Loss: ₹5,000</h3>
        </div>
        """, unsafe_allow_html=True)

        st.markdown("### What if Alex spreads the money?")

        st.write("""
        Instead of putting all ₹10,000 into one company,
        he spreads the investment across four companies.
        """)

        st.markdown("""
        <div class="info-box">
        Company A: ₹2,500

        Company B: ₹2,500

        Company C: ₹2,500

        Company D: ₹2,500
        </div>
        """, unsafe_allow_html=True)

        st.write("""
        Imagine Company A loses 50%, but the other
        three companies remain unchanged.
        """)

        st.markdown("""
        <div class="success-box">
        <h3>Company A</h3>
        ₹2,500 → ₹1,250
        </div>
        """, unsafe_allow_html=True)

        st.markdown("""
        <div class="info-box">
        <h3>Companies B, C and D</h3>
        ₹7,500 → ₹7,500
        </div>
        """, unsafe_allow_html=True)

        st.markdown("""
        <div class="warning-box">
        <h3>Combined value: ₹8,750</h3>

        Initial investment: ₹10,000

        Simulated loss: ₹1,250
        </div>
        """, unsafe_allow_html=True)

        st.markdown("### What is diversification?")

        st.write("""
        Diversification means spreading investments
        across different assets, companies, industries
        or other investment types.

        It can reduce the impact of one investment
        performing badly on the entire portfolio.
        """)

        st.warning("""
        Diversification does not guarantee profits
        or prevent losses. Investments can fall together,
        particularly during market-wide declines.
        """)

    # SCENE 5: RISK AND RETURN

    elif scene == 5:

        st.markdown('<div class="character">⚖️</div>',
                    unsafe_allow_html=True)

        st.markdown("## Risk and potential return")

        st.write("""
        Alex notices something interesting.

        Some investments offer the possibility
        of higher returns, but those returns
        may come with greater uncertainty.
        """)

        st.markdown("""
        <div class="info-box">
        <h3>Option A</h3>
        <p>Lower potential return, with relatively
        lower risk in some circumstances.</p>
        </div>
        """, unsafe_allow_html=True)

        st.markdown("""
        <div class="info-box">
        <h3>Option B</h3>
        <p>Higher potential return, with the possibility
        of larger losses and greater uncertainty.</p>
        </div>
        """, unsafe_allow_html=True)

        st.markdown("### Does higher risk guarantee higher returns?")

        st.error("No!")

        st.write("""
        Taking more risk does not guarantee
        that you will earn more money.

        An investment can have high risk and still
        produce poor returns or losses.
        """)

        st.markdown("""
        <div class="warning-box">
        <h3>Important principle</h3>

        Higher potential returns often involve higher risk,
        but the relationship is not a guarantee.

        Risk is not a promise of reward.
        </div>
        """, unsafe_allow_html=True)

        st.markdown("### What should an investor consider?")

        st.markdown("""
        - How much money could I lose?
        - Do I understand this investment?
        - When might I need the money?
        - Can I handle a loss?
        - Am I investing based on facts or excitement?
        """)

    # SCENE 6: SCAM INVESTIGATION

    elif scene == 6:

        st.markdown('<div class="character">🚨</div>',
                    unsafe_allow_html=True)

        st.markdown("## Alex investigates a suspicious offer")

        st.markdown("""
        <div class="warning-box">
        <h2>30% PROFIT EVERY MONTH!</h2>
        <h3>ZERO RISK!</h3>
        <h3>100% GUARANTEED!</h3>
        </div>
        """, unsafe_allow_html=True)

        st.write("""
        Alex receives a message from a stranger.
        The stranger says:
        """)

        st.markdown("""
        <div class="info-box">
        "Send ₹10,000 today.

        We will give you ₹3,000 profit every month.

        You cannot lose money.

        Send it now before the offer expires!"
        </div>
        """, unsafe_allow_html=True)

        st.markdown("### Let's investigate the offer")

        st.markdown("""
        <div class="warning-box">
        🚩 Warning sign 1

        Unusually high promised returns.
        </div>
        """, unsafe_allow_html=True)

        st.markdown("""
        <div class="warning-box">
        🚩 Warning sign 2

        Claims that there is absolutely no risk.
        </div>
        """, unsafe_allow_html=True)

        st.markdown("""
        <div class="warning-box">
        🚩 Warning sign 3

        Pressure to send money immediately.
        </div>
        """, unsafe_allow_html=True)

        st.markdown("""
        <div class="warning-box">
        🚩 Warning sign 4

        No independently verified information
        about the business or investment.
        </div>
        """, unsafe_allow_html=True)

        st.markdown("### What should Alex do?")

        st.write("""
        He should not send money just because
        someone promises high returns.

        He should independently verify the person,
        company and product, check relevant
        regulatory information, and understand
        exactly how the investment works.
        """)

        st.error("""
        Guaranteed unusually high returns with
        no risk are a major warning sign.

        Never rush into an investment because
        someone is pressuring you.
        """)

    # SCENE 7: FINAL QUIZ WITH FEEDBACK

    elif scene == 7:

        st.markdown('<div class="character">🧠</div>',
                    unsafe_allow_html=True)

        st.markdown("## Final Challenge")

        st.write("""
        Alex wants to check whether he understands
        what he has learned.

        Answer all three questions.
        """)

        q1 = st.radio(
            "1. What does investment risk mean?",
            [
                "A. Profit is always guaranteed",
                "B. The outcome is uncertain",
                "C. Investors always lose money"
            ],
            key="l7_final_q1"
        )

        q2 = st.radio(
            "2. What is diversification?",
            [
                "A. Putting all money in one company",
                "B. Borrowing money to invest",
                "C. Spreading investments across assets"
            ],
            key="l7_final_q2"
        )

        q3 = st.radio(
            "3. Which is a major warning sign?",
            [
                "A. Returns may change",
                "B. Investments carry different risks",
                "C. 30% monthly profit guaranteed with zero risk"
            ],
            key="l7_final_q3"
        )

        current_answers = (q1, q2, q3)

        if st.button("Check My Answers", key="l7_final_check"):

            st.session_state.l7_checked_answers = current_answers

        if (
            "l7_checked_answers" in st.session_state
            and st.session_state.l7_checked_answers == current_answers
        ):

            answers = st.session_state.l7_checked_answers

            correct = [
                "B. The outcome is uncertain",
                "C. Spreading investments across assets",
                "C. 30% monthly profit guaranteed with zero risk"
            ]

            explanations = {

                1: {
                    "A. Profit is always guaranteed":
                    (
                        "This is incorrect because investments "
                        "do not guarantee profit. Their outcomes "
                        "can be uncertain."
                    ),

                    "B. The outcome is uncertain":
                    (
                        "Correct! Risk refers to uncertainty "
                        "about investment outcomes. An investment "
                        "may gain or lose value."
                    ),

                    "C. Investors always lose money":
                    (
                        "This is incorrect. Risk does not mean "
                        "that a loss is certain. Investments "
                        "can gain, lose or sometimes remain "
                        "at a similar value."
                    )
                },

                2: {
                    "A. Putting all money in one company":
                    (
                        "This is concentration, not diversification. "
                        "It leaves your investment more exposed "
                        "to the performance of one company."
                    ),

                    "B. Borrowing money to invest":
                    (
                        "Borrowing to invest is a financial "
                        "strategy that can increase risk. "
                        "It is not diversification."
                    ),

                    "C. Spreading investments across assets":
                    (
                        "Correct! Diversification spreads money "
                        "across different investments to reduce "
                        "concentration risk. It cannot eliminate "
                        "all risks."
                    )
                },

                3: {
                    "A. Returns may change":
                    (
                        "This is normal for many investments. "
                        "Variable returns alone are not a scam sign."
                    ),

                    "B. Investments carry different risks":
                    (
                        "This is a normal financial fact. "
                        "Different investment products have "
                        "different risks."
                    ),

                    "C. 30% monthly profit guaranteed with zero risk":
                    (
                        "Correct! Unusually high guaranteed "
                        "returns combined with claims of zero "
                        "risk are a major warning sign. "
                        "Investigate independently before "
                        "sending any money."
                    )
                }
            }

            score = sum(
                answers[i] == correct[i]
                for i in range(3)
            )

            st.markdown("---")

            st.subheader(f"Your score: {score}/3")

            for i, answer in enumerate(answers):

                question_number = i + 1

                if answer == correct[i]:
                    st.success(
                        f"Question {question_number}: Correct!"
                    )
                else:
                    st.error(
                        f"Question {question_number}: Incorrect."
                    )

                st.markdown(
                    f"**Your answer:** {answer}"
                )

                st.markdown(
                    f"**Correct answer:** {correct[i]}"
                )

                st.write(
                    explanations[question_number][answer]
                )

                st.markdown("---")

            if score == 3:

                st.success("""
                Excellent! Alex understands
                investment risk.
                """)

            elif score == 2:

                st.info("""
                Good work! Review the explanations
                for the question you missed.
                """)

            else:

                st.info("""
                Review the explanations above.
                Understanding why answers are correct
                is more important than memorizing them.
                """)

            st.markdown("""
            <div class="storybox">
            <h2>Lesson 7 Completed!</h2>

            <h3>Alex learned that investing is not
            only about making money.</h3>

            <p>It is also about understanding risks,
            protecting yourself and making informed decisions.</p>

            <h2>🔓 Next: Lesson 8</h2>
            </div>
            """, unsafe_allow_html=True)

    # NAVIGATION

    st.markdown("---")

    col1, col2 = st.columns(2)

    with col1:

        if scene > 0:

            if st.button("⬅️ Previous Scene", key="l7_prev"):

                st.session_state.l7_scene -= 1
                st.rerun()

    with col2:

        if scene < 7:

            if st.button("Next Scene ➡️", key="l7_next"):

                st.session_state.l7_scene += 1
                st.rerun()

    st.caption("MoneyLab • Chapter 1 • Lesson 7")
