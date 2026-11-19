
import streamlit as st
import streamlit.components.v1 as components

def show_lesson6():

    st.title("📈 Lesson 6: The Investing Race")
    st.caption("MoneyLab | Learn Money by Living It")

    if "l6_stage" not in st.session_state:
        st.session_state.l6_stage = 0

    if "l6_investment" not in st.session_state:
        st.session_state.l6_investment = None

    stage = st.session_state.l6_stage

    # BACK BUTTON
    if stage > 0:
        if st.button("← Back"):
            st.session_state.l6_stage -= 1
            st.rerun()

    # SCENE 1: INTRO
    if stage == 0:

        components.html("""
        <div style="background:linear-gradient(135deg,#0f172a,#1d4ed8);
        padding:25px;border-radius:20px;text-align:center;color:white;
        font-family:sans-serif;">
        <div style="font-size:80px;animation:float 2s infinite alternate;">📈</div>
        <h2>Alex Wants to Grow His Money!</h2>
        <p>Alex has some money and is thinking about investing.</p>
        <div style="font-size:55px;animation:money 2s infinite;">💰</div>
        <p>But how does investing actually work?</p>
        <style>
        @keyframes float {
        from {transform:translateY(0)}
        to {transform:translateY(-12px)}
        }
        @keyframes money {
        from {transform:scale(.9)}
        to {transform:scale(1.15)}
        }
        </style>
        </div>
        """, height=300)

        st.write("""
        Alex has already learned to manage spending and prepare
        for emergencies. Now he wants to understand investing.
        """)

        if st.button("Start Investing Simulation →"):
            st.session_state.l6_stage = 1
            st.rerun()

    # SCENE 2: INVESTMENT DECISION
    elif stage == 1:

        st.subheader("🧠 Make an Investment Decision")

        st.write("Alex wants to invest some money for the future.")

        with st.form("l6_invest_form"):

            amount = st.number_input(
                "How much does Alex want to invest? (₹)",
                min_value=100,
                max_value=1000000,
                value=10000,
                step=1000
            )

            years = st.selectbox(
                "How long will Alex invest?",
                [1, 3, 5, 10, 15, 20]
            )

            risk = st.radio(
                "Choose an illustrative investment scenario:",
                [
                    "Lower-risk scenario (4% assumed yearly return)",
                    "Moderate scenario (7% assumed yearly return)",
                    "Higher-risk scenario (12% assumed yearly return)"
                ]
            )

            submit = st.form_submit_button("Simulate Growth →")

        if submit:

            if "4%" in risk:
                rate = 0.04
                scenario = "Lower-risk illustration"
            elif "7%" in risk:
                rate = 0.07
                scenario = "Moderate illustration"
            else:
                rate = 0.12
                scenario = "Higher-risk illustration"

            final_value = amount * ((1 + rate) ** years)
            growth = final_value - amount

            st.session_state.l6_investment = {
                "amount": amount,
                "years": years,
                "rate": rate,
                "scenario": scenario,
                "final": final_value,
                "growth": growth
            }

            st.session_state.l6_stage = 2
            st.rerun()

    # SCENE 3: RESULTS
    elif stage == 2:

        data = st.session_state.l6_investment

        amount = data["amount"]
        years = data["years"]
        rate = data["rate"]
        final_value = data["final"]
        growth = data["growth"]

        st.subheader("🌱 The Growth Simulation")

        components.html("""
        <div style="background:linear-gradient(135deg,#064e3b,#10b981);
        padding:25px;border-radius:20px;text-align:center;color:white;
        font-family:sans-serif;">
        <div style="font-size:75px;animation:grow 2s infinite alternate;">🌱</div>
        <h2>Time Can Grow Money!</h2>
        <p>Let's see what happens to Alex's investment.</p>
        <style>
        @keyframes grow {
        from {transform:scale(.8)}
        to {transform:scale(1.2)}
        }
        </style>
        </div>
        """, height=260)

        st.write(f"**Initial investment:** ₹{amount:,.2f}")
        st.write(f"**Time:** {years} years")
        st.write(f"**Assumed annual return:** {rate*100:.0f}%")
        st.write(f"**Scenario:** {data['scenario']}")

        st.divider()

        st.metric(
            "Illustrative final value",
            f"₹{final_value:,.2f}",
            f"+₹{growth:,.2f}"
        )

        st.markdown("### 📊 Money Growth")

        st.write(f"Initially: ₹{amount:,.2f}")
        st.progress(0.25)

        st.write(f"Illustrative final value: ₹{final_value:,.2f}")
        st.progress(1.0)

        st.info(
            "This calculation assumes the same annual return every year "
            "and compounding. Real investments do not grow at a fixed rate. "
            "They can fall in value, and returns are not guaranteed."
        )

        if st.button("Explore the Power of Compounding →"):
            st.session_state.l6_stage = 3
            st.rerun()

    # SCENE 4: COMPOUNDING
    elif stage == 3:

        st.subheader("🔄 The Power of Compounding")

        st.write("""
        Compound growth happens when investment returns are added
        to your money, and future returns can also grow on those returns.
        """)

        st.markdown("### Example: ₹10,000 at an assumed 7% annually")

        starting = 10000

        for year in range(1, 11):
            value = starting * (1.07 ** year)
            st.write(f"**Year {year}:** ₹{value:,.2f}")

        components.html("""
        <div style="background:linear-gradient(135deg,#1e3a8a,#2563eb);
        padding:25px;border-radius:20px;text-align:center;color:white;
        font-family:sans-serif;">
        <div style="font-size:65px;animation:rise 2s infinite alternate;">🚀</div>
        <h2>Growth Builds on Growth!</h2>
        <p>Returns can compound over time.</p>
        <style>
        @keyframes rise {
        from {transform:translateY(8px)}
        to {transform:translateY(-12px)}
        }
        </style>
        </div>
        """, height=230)

        st.warning(
            "This is a mathematical example, not a prediction "
            "of actual investment performance."
        )

        if st.button("Understand Investment Risk →"):
            st.session_state.l6_stage = 4
            st.rerun()

    # SCENE 5: RISK
    elif stage == 4:

        st.subheader("⚠️ Investment Risk")

        components.html("""
        <div style="background:linear-gradient(135deg,#7f1d1d,#dc2626);
        padding:25px;border-radius:20px;text-align:center;color:white;
        font-family:sans-serif;">
        <div style="font-size:70px;animation:shake 1s infinite;">📉</div>
        <h2>Investments Can Fall!</h2>
        <p>Growth isn't guaranteed.</p>
        <style>
        @keyframes shake {
        0% {transform:rotate(0)}
        25% {transform:rotate(5deg)}
        50% {transform:rotate(-5deg)}
        75% {transform:rotate(5deg)}
        100% {transform:rotate(0)}
        }
        </style>
        </div>
        """, height=240)

        st.markdown("""
        ### Important risks:

        - **Market risk:** Prices can rise and fall.
        - **Loss risk:** You may lose part or all of your money.
        - **Inflation risk:** Money may lose purchasing power.
        - **Time risk:** Some investments need a longer horizon,
          but a longer horizon doesn't guarantee profits.
        - **Diversification:** Spreading investments can reduce
          some concentration risks, but cannot eliminate risk.
        """)

        if st.button("Finish Lesson →"):
            st.session_state.l6_stage = 5
            st.rerun()

    # SCENE 6: FINAL LESSON
    elif stage == 5:

        st.subheader("🎓 What You Learned")

        components.html("""
        <div style="background:linear-gradient(135deg,#064e3b,#059669);
        padding:25px;border-radius:20px;text-align:center;color:white;
        font-family:sans-serif;">
        <div style="font-size:70px;animation:grow 2s infinite alternate;">🌳</div>
        <h2>Build Your Financial Future!</h2>
        <p>Understand risk, time and compounding.</p>
        <style>
        @keyframes grow {
        from {transform:scale(.8)}
        to {transform:scale(1.15)}
        }
        </style>
        </div>
        """, height=240)

        st.markdown("""
        ### 1. Saving and investing are different
        Savings are generally meant for safety and accessibility.
        Investing involves risk in pursuit of potential growth.

        ### 2. Compounding
        Returns can generate additional returns over time.

        ### 3. Time matters
        Longer periods can allow more time for compounding,
        but do not guarantee a positive outcome.

        ### 4. Risk and return
        Higher potential returns often involve higher risks.

        ### 5. Don't invest emergency money carelessly
        Keep money needed for emergencies and near-term expenses
        in suitable, accessible and relatively safe places.

        ### 6. Understand before investing
        Learn about the investment, fees, risks and your own goals.
        """)

        st.markdown("## 💡 Smart Investing Principles")

        st.markdown("""
        - Invest only after understanding what you are buying.
        - Don't chase guaranteed or unrealistic returns.
        - Diversify instead of relying on one investment.
        - Understand fees and risks.
        - Be patient and think long term.
        """)

        st.success(
            "Investing is not about getting rich quickly. "
            "It is about understanding risk and building wealth "
            "carefully over time."
        )

        if st.button("🔄 Play Again"):
            st.session_state.l6_stage = 0
            st.session_state.l6_investment = None
            st.rerun()

    st.divider()
    st.caption("MoneyLab | Learn Money by Living It")
