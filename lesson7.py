
import streamlit as st
import random

def lesson7():

    if "l7_scene" not in st.session_state:
        st.session_state.l7_scene = 0

    if "l7_choice" not in st.session_state:
        st.session_state.l7_choice = None

    scene = st.session_state.l7_scene

    st.markdown("""
    <style>
    @keyframes float {
        0%,100% {transform:translateY(0px);}
        50% {transform:translateY(-15px);}
    }
    @keyframes glow {
        0%,100% {box-shadow:0 0 5px #f59e0b;}
        50% {box-shadow:0 0 25px #f59e0b;}
    }
    @keyframes appear {
        from {opacity:0;transform:translateY(20px);}
        to {opacity:1;transform:translateY(0);}
    }
    .character {
        font-size:100px;
        text-align:center;
        animation:float 2s infinite;
    }
    .scene-box {
        background:linear-gradient(135deg,#172554,#1e3a8a);
        padding:25px;
        border-radius:20px;
        color:white;
        text-align:center;
        animation:appear 0.8s;
    }
    .offer {
        background:#172033;
        border:1px solid #334155;
        padding:20px;
        border-radius:15px;
        margin:10px 0;
        color:white;
        animation:appear 1s;
    }
    .warning {
        background:#451a03;
        border:2px solid #f59e0b;
        padding:20px;
        border-radius:15px;
        color:#fde68a;
        animation:glow 3s infinite;
    }
    .money {
        font-size:30px;
        font-weight:bold;
        text-align:center;
        padding:20px;
        color:#86efac;
        background:#14532d;
        border-radius:15px;
    }
    .danger {
        font-size:25px;
        font-weight:bold;
        text-align:center;
        padding:20px;
        color:#fca5a5;
        background:#450a0a;
        border-radius:15px;
    }
    .story {
        background:#0f172a;
        border-left:5px solid #38bdf8;
        padding:20px;
        border-radius:12px;
        color:white;
    }
    </style>
    """, unsafe_allow_html=True)

    st.title("🎯 Lesson 7 — The Risk Trap")
    st.caption("MoneyLab • Learn Money by Living It")

    st.progress((scene + 1) / 8)

    # SCENE 0
    if scene == 0:

        st.markdown('<div class="character">🧑‍💻</div>',
                    unsafe_allow_html=True)

        st.markdown("""
        <div class="scene-box">
        <h2>Alex enters the investment world</h2>
        <h3>He has ₹10,000 to invest.</h3>
        </div>
        """, unsafe_allow_html=True)

        st.write("""
        In Lesson 6, Alex learned that investments can help
        money grow over time.

        But today, he discovers something new.

        **Investments can also lose money.**
        """)

        st.info("Lesson 6 taught growth. Lesson 7 teaches risk.")

    # SCENE 1
    elif scene == 1:

        st.markdown('<div class="character">💼</div>',
                    unsafe_allow_html=True)

        st.markdown("## Three investment offers")

        st.write("Alex receives three different offers.")

        st.markdown("""
        <div class="offer">
        <h3>🛡️ Offer A — Lower Risk</h3>
        <p>Potentially lower returns and relatively
        lower risk, depending on the product.</p>
        </div>

        <div class="offer">
        <h3>📈 Offer B — Market Investment</h3>
        <p>Returns can rise or fall.
        The value may change with the market.</p>
        </div>

        <div class="offer">
        <h3>🚀 Offer C — The Big Promise</h3>
        <p>Someone promises 30% profit every month
        with absolutely no risk.</p>
        </div>
        """, unsafe_allow_html=True)

        st.warning("Which offer sounds the most dangerous?")

    # SCENE 2
    elif scene == 2:

        st.markdown('<div class="character">⚠️</div>',
                    unsafe_allow_html=True)

        st.markdown("## What is investment risk?")

        st.markdown("""
        <div class="story">
        Risk means that the outcome is uncertain.

        You might earn money.

        You might earn less than expected.

        You might lose some or all of the money you invested,
        depending on the investment.
        </div>
        """, unsafe_allow_html=True)

        st.write("### Imagine investing ₹10,000")

        st.markdown("""
        <div class="money">Possible Gain: +₹2,000</div>
        <br>
        <div class="danger">Possible Loss: -₹2,000</div>
        """, unsafe_allow_html=True)

        st.write("""
        Neither outcome is guaranteed.

        **Risk does not mean loss will definitely happen.
        It means the outcome is uncertain.**
        """)

    # SCENE 3
    elif scene == 3:

        st.markdown('<div class="character">📊</div>',
                    unsafe_allow_html=True)

        st.markdown("## Return is not guaranteed")

        st.write("""
        Alex invests ₹10,000 in a market investment.

        Let's see three possible outcomes after a period
        of time.
        """)

        st.markdown("""
        <div class="offer">
        <h3>🟢 Scenario 1</h3>
        <h2>₹12,000</h2>
        <p>His investment increased by ₹2,000.</p>
        </div>

        <div class="offer">
        <h3>🟡 Scenario 2</h3>
        <h2>₹10,500</h2>
        <p>His investment increased by ₹500.</p>
        </div>

        <div class="offer">
        <h3>🔴 Scenario 3</h3>
        <h2>₹8,000</h2>
        <p>His investment decreased by ₹2,000.</p>
        </div>
        """, unsafe_allow_html=True)

        st.caption("Illustrative outcomes, not a forecast.")

        st.write("""
        The same investment can have different outcomes.

        This is why investors should not assume that
        past returns will continue in the future.
        """)

    # SCENE 4
    elif scene == 4:

        st.markdown('<div class="character">🧺</div>',
                    unsafe_allow_html=True)

        st.markdown("## Don't put everything in one basket")

        st.write("""
        Alex has ₹10,000.

        He is thinking about putting all his money
        into a single company.
        """)

        st.markdown("""
        <div class="danger">
        ₹10,000 → ONE COMPANY
        </div>
        """, unsafe_allow_html=True)

        st.write("""
        If that company performs badly,
        a large part of his investment could suffer.
        """)

        st.markdown("### What if he diversifies?")

        st.markdown("""
        <div class="offer">
        🏢 Company A — ₹2,500
        </div>
        <div class="offer">
        🏢 Company B — ₹2,500
        </div>
        <div class="offer">
        🏢 Company C — ₹2,500
        </div>
        <div class="offer">
        🏢 Company D — ₹2,500
        </div>
        """, unsafe_allow_html=True)

        st.success("""
        Diversification means spreading investments
        across different assets instead of relying
        on just one.
        """)

        st.warning("""
        Diversification can reduce concentration risk,
        but it cannot eliminate all investment risk.
        """)

    # SCENE 5
    elif scene == 5:

        st.markdown('<div class="character">🎮</div>',
                    unsafe_allow_html=True)

        st.markdown("## Alex's Risk Simulator")

        st.write("Alex invests ₹10,000.")

        outcome = st.selectbox(
            "Choose a possible market outcome:",
            [
                "Strong Market (+20%)",
                "Moderate Market (+5%)",
                "Market Decline (-20%)",
                "Severe Decline (-50%)"
            ],
            key="l7_simulator"
        )

        if st.button("Simulate Outcome", key="l7_sim_button"):

            outcomes = {
                "Strong Market (+20%)": 12000,
                "Moderate Market (+5%)": 10500,
                "Market Decline (-20%)": 8000,
                "Severe Decline (-50%)": 5000
            }

            st.session_state.l7_sim_result = outcomes[outcome]

        if "l7_sim_result" in st.session_state:

            result = st.session_state.l7_sim_result

            if result > 10000:
                st.success(f"Investment Value: ₹{result:,}")
                st.write(f"Profit: ₹{result - 10000:,}")

            elif result < 10000:
                st.error(f"Investment Value: ₹{result:,}")
                st.write(f"Loss: ₹{10000 - result:,}")

            else:
                st.info("No profit or loss.")

        st.caption("Simulated outcomes. Not predictions.")

    # SCENE 6
    elif scene == 6:

        st.markdown('<div class="character">🚨</div>',
                    unsafe_allow_html=True)

        st.markdown("## The Guaranteed Profit Trap")

        st.markdown("""
        <div class="warning">
        <h2>30% PROFIT EVERY MONTH!</h2>
        <h3>ZERO RISK!</h3>
        <h3>YOUR MONEY IS 100% SAFE!</h3>
        </div>
        """, unsafe_allow_html=True)

        st.write("""
        Alex receives this message from a stranger.
        """)

        st.markdown("""
        <div class="story">
        "Send ₹10,000 today.

        We guarantee ₹3,000 profit every month.

        You cannot lose money!"
        </div>
        """, unsafe_allow_html=True)

        st.write("### 🚩 Warning signs")

        st.markdown("""
        - Guaranteed unusually high returns.
        - Claims of zero risk.
        - Pressure to send money immediately.
        - No clear explanation of how the investment works.
        - Unverified company or person.
        """)

        st.error("""
        High guaranteed returns with no risk are a major
        warning sign of a potential scam.

        Always independently verify the person,
        company and investment before sending money.
        """)

    # SCENE 7
    elif scene == 7:

        st.markdown('<div class="character">🏆</div>',
                    unsafe_allow_html=True)

        st.markdown("## 🧠 Final Challenge")

        q1 = st.radio(
            "1. What does investment risk mean?",
            [
                "Profit is guaranteed",
                "The outcome is uncertain",
                "The investor always loses money"
            ],
            key="l7_q1"
        )

        q2 = st.radio(
            "2. What is diversification?",
            [
                "Investing everything in one company",
                "Borrowing money to invest",
                "Spreading investments across different assets"
            ],
            key="l7_q2"
        )

        q3 = st.radio(
            "3. Which statement is a warning sign?",
            [
                "Returns can vary",
                "All investments have different risks",
                "30% monthly return guaranteed with zero risk"
            ],
            key="l7_q3"
        )

        if st.button("Check My Answers", key="l7_quiz_check"):

            score = 0

            if q1 == "The outcome is uncertain":
                score += 1

            if q2 == "Spreading investments across different assets":
                score += 1

            if q3 == "30% monthly return guaranteed with zero risk":
                score += 1

            st.session_state.l7_score = score

        if "l7_score" in st.session_state:

            score = st.session_state.l7_score

            st.markdown("---")

            if score == 3:
                st.success("🏆 Excellent! 3/3")

            elif score == 2:
                st.success(f"Good work! {score}/3")

            else:
                st.info(f"You scored {score}/3. Review the lesson.")

            st.markdown("### What you learned")

            st.markdown("""
            - Investment risk and uncertainty.
            - Potential profits and losses.
            - Why returns are not guaranteed.
            - Diversification.
            - Recognizing suspicious investment promises.
            """)

            st.markdown("---")

            st.markdown("""
            <div class="scene-box">
            <h2>Lesson 7 Completed!</h2>
            <h3>Alex now understands that investing
            isn't only about making money.</h3>
            <p>It's also about understanding what
            could go wrong.</p>
            <h2>🔓 Next: Lesson 8</h2>
            </div>
            """, unsafe_allow_html=True)

    # NAVIGATION

    st.markdown("---")

    col1, col2 = st.columns(2)

    with col1:
        if scene > 0:
            if st.button("⬅️ Previous Scene", key="l7_previous"):
                st.session_state.l7_scene -= 1
                st.rerun()

    with col2:
        if scene < 7:
            if st.button("Next Scene ➡️", key="l7_next"):
                st.session_state.l7_scene += 1
                st.rerun()

    st.caption("MoneyLab • Chapter 1 • Lesson 7")
