
import streamlit as st
import streamlit.components.v1 as components

def lesson2():

    st.title("🏦 Alex and the Bank")
    st.caption("Chapter 1 • How Money Is Created")

    if "l2_scene" not in st.session_state:
        st.session_state.l2_scene = 0

    scene = st.session_state.l2_scene

    def animation(html):
        components.html(html, height=250)

    def next_scene():
        st.session_state.l2_scene += 1
        st.rerun()

    def previous_scene():
        st.session_state.l2_scene -= 1
        st.rerun()

    # SCENE 0 — INTRO

    if scene == 0:

        animation("""
        <div style="height:230px;background:linear-gradient(135deg,#172554,#2563eb);
        border-radius:20px;display:flex;align-items:center;justify-content:center;
        flex-direction:column;color:white;font-family:sans-serif">

        <div style="font-size:80px;animation:bounce 2s infinite">🧑</div>
        <h2>Meet Alex!</h2>
        <p>Alex wants to understand how banks work.</p>

        <style>
        @keyframes bounce {
        0%,100% {transform:translateY(0)}
        50% {transform:translateY(-15px)}
        }
        </style>
        </div>
        """)

        st.markdown("""
        Alex wants to buy a laptop for his education.

        The laptop costs **₹10,000**.

        Alex doesn't have enough money, so he visits a bank.
        """)

        if st.button("🏦 Visit the Bank", key="l2_start"):
            next_scene()

    # SCENE 1 — LOAN OFFER

    elif scene == 1:

        st.header("🏦 The Bank's Offer")

        animation("""
        <div style="height:230px;background:#dcfce7;border-radius:20px;
        display:flex;align-items:center;justify-content:space-around;
        font-family:sans-serif">

        <div style="text-align:center">
        <div style="font-size:75px">🧑</div>
        <b>Alex</b>
        </div>

        <div style="font-size:40px;animation:pulse 1.5s infinite">➡️</div>

        <div style="text-align:center">
        <div style="font-size:75px">🏦</div>
        <b>Bank</b>
        </div>

        <style>
        @keyframes pulse {
        0%,100% {transform:scale(1)}
        50% {transform:scale(1.2)}
        }
        </style>
        </div>
        """)

        st.markdown("""
        The bank offers Alex a loan of **₹10,000**.

        But a loan is borrowed money. Alex must repay it,
        usually with interest and according to the loan agreement.
        """)

        st.markdown("### 💰 Loan Offer")

        st.metric("Loan Amount", "₹10,000")

        st.warning("Borrowing gives Alex money now, but creates a repayment obligation.")

        decision = st.radio(
            "What should Alex do?",
            ["Accept the loan", "Reject the loan"],
            key="l2_decision"
        )

        if st.button("Make Decision", key="l2_decide"):

            st.session_state.l2_choice = decision

            if decision == "Accept the loan":
                st.session_state.l2_scene = 2
            else:
                st.session_state.l2_scene = 3

            st.rerun()

    # SCENE 2 — LOAN ACCEPTED

    elif scene == 2:

        st.header("💳 Alex Accepts the Loan")

        animation("""
        <div style="height:230px;background:linear-gradient(135deg,#14532d,#16a34a);
        border-radius:20px;color:white;display:flex;align-items:center;
        justify-content:center;flex-direction:column;font-family:sans-serif">

        <div style="font-size:65px;animation:bounce 2s infinite">💰</div>
        <h2>₹10,000 Deposited!</h2>
        <p>Alex's bank account balance increases.</p>

        <style>
        @keyframes bounce {
        0%,100% {transform:translateY(0)}
        50% {transform:translateY(-12px)}
        }
        </style>
        </div>
        """)

        st.markdown("### Alex's financial position")

        st.markdown("""
        <div style="background:#14532d;padding:20px;border-radius:15px;
        color:white;text-align:center;font-size:24px">
        Bank Deposit<br>+ ₹10,000
        </div>
        """, unsafe_allow_html=True)

        st.markdown("""
        <div style="background:#7f1d1d;padding:20px;border-radius:15px;
        color:white;text-align:center;font-size:24px;margin-top:10px">
        Loan Debt<br>₹10,000
        </div>
        """, unsafe_allow_html=True)

        st.write("""
        Alex now has ₹10,000 in his bank account.

        But he also owes ₹10,000 to the bank, before interest
        and any applicable fees.
        """)

        st.info("Money in the account is not the same as wealth. The loan creates a corresponding liability.")

        if st.button("How Did the Bank Create This Money? ➡️", key="l2_next2"):
            next_scene()

    # SCENE 3 — LOAN REJECTED

    elif scene == 3:

        st.header("🙂 Alex Rejects the Loan")

        animation("""
        <div style="height:230px;background:#fef3c7;border-radius:20px;
        display:flex;align-items:center;justify-content:center;
        flex-direction:column">

        <div style="font-size:75px;animation:bounce 2s infinite">🧑</div>
        <h2>No Loan Taken</h2>
        <p>Alex avoids a new debt obligation.</p>

        <style>
        @keyframes bounce {
        0%,100% {transform:translateY(0)}
        50% {transform:translateY(-12px)}
        }
        </style>
        </div>
        """)

        st.write("""
        Alex rejected the offer.

        His bank balance did not increase from this loan,
        and he did not take on the loan debt.
        """)

        st.info("Rejecting a loan can be sensible if the borrowing isn't necessary or affordable.")

        if st.button("Learn How Banks Create Money ➡️", key="l2_reject_next"):
            st.session_state.l2_scene = 4
            st.rerun()

    # SCENE 4 — MONEY CREATION

    elif scene == 4:

        st.header("⚙️ How Banks Create Money")

        animation("""
        <div style="height:230px;background:#e0f2fe;border-radius:20px;
        display:flex;align-items:center;justify-content:center;
        flex-direction:column;font-family:sans-serif">

        <div style="font-size:70px;animation:pulse 2s infinite">🏦</div>
        <h2>Loan → Deposit</h2>
        <div style="font-size:28px">₹10,000</div>

        <style>
        @keyframes pulse {
        0%,100% {transform:scale(1)}
        50% {transform:scale(1.1)}
        }
        </style>
        </div>
        """)

        st.markdown("### What happens when a bank makes a loan?")

        st.markdown("""
        In a typical bank loan:

        **1.** The bank approves the loan.

        **2.** The bank records a loan asset on its balance sheet.

        **3.** The bank generally credits the borrower's deposit account.

        **4.** The borrower now has a deposit and a debt.
        """)

        st.markdown("### 📊 The simplified accounting")

        st.markdown("""
        | Bank | Change |
        |---|---:|
        | Loan asset | +₹10,000 |
        | Deposit liability | +₹10,000 |
        """)

        st.info("""
        Commercial banks generally create deposits when they lend.
        They are not simply handing out existing deposits one-for-one.

        However, lending is constrained by capital, liquidity, risk,
        regulation, funding costs and demand for credit.
        """)

        if st.button("Explore Loan Interest ➡️", key="l2_next4"):
            next_scene()

    # SCENE 5 — INTEREST SIMULATOR

    elif scene == 5:

        st.header("🧮 Loan Interest Simulator")

        st.write("Let's calculate how much Alex might repay.")

        amount = st.slider(
            "Loan amount (₹)",
            1000, 100000, 10000, 1000,
            key="l2_amount"
        )

        rate = st.slider(
            "Annual interest rate (%)",
            1.0, 30.0, 10.0, 0.5,
            key="l2_rate"
        )

        years = st.slider(
            "Loan duration (years)",
            1, 10, 2,
            key="l2_years"
        )

        monthly_rate = rate / 100 / 12
        months = years * 12

        if monthly_rate > 0:
            emi = amount * monthly_rate * (1 + monthly_rate) ** months / ((1 + monthly_rate) ** months - 1)
        else:
            emi = amount / months

        total_payment = emi * months
        total_interest = total_payment - amount

        st.markdown("---")

        st.metric("Estimated Monthly EMI", f"₹{emi:,.2f}")
        st.metric("Total Repayment", f"₹{total_payment:,.2f}")
        st.metric("Total Interest", f"₹{total_interest:,.2f}")

        st.caption("Illustrative EMI calculation assuming fixed rate, monthly payments and no additional fees.")

        if st.button("Next ➡️", key="l2_next5"):
            next_scene()

    # SCENE 6 — GOOD OR BAD BORROWING

    elif scene == 6:

        st.header("🤔 Is Borrowing Always Bad?")

        animation("""
        <div style="height:230px;background:#f3e8ff;border-radius:20px;
        display:flex;align-items:center;justify-content:space-around;
        font-family:sans-serif">

        <div style="text-align:center">
        <div style="font-size:65px">💻</div>
        <b>Education</b>
        </div>

        <div style="text-align:center">
        <div style="font-size:65px">🛍️</div>
        <b>Impulse shopping</b>
        </div>
        </div>
        """)

        st.write("""
        Borrowing isn't automatically good or bad.

        It depends on the purpose, cost, risk and ability to repay.
        """)

        scenario = st.radio(
            "Which borrowing decision appears more financially sensible?",
            [
                "Borrow at any cost to buy expensive luxury items",
                "Carefully evaluate an affordable loan for an important need",
                "Borrow without checking the interest rate"
            ],
            key="l2_borrowing"
        )

        if st.button("Check My Decision", key="l2_borrow_check"):

            if scenario == "Carefully evaluate an affordable loan for an important need":
                st.success("""
                Correct! Borrowing can be useful when the purpose,
                repayment plan, cost and risks are carefully evaluated.
                """)
            else:
                st.warning("""
                Be careful. Borrowing without considering cost,
                affordability and purpose can create financial problems.
                """)

        if st.button("Final Knowledge Check ➡️", key="l2_next6"):
            next_scene()

    # SCENE 7 — QUIZ

    elif scene == 7:

        st.header("🧠 Knowledge Check")

        question = st.radio(
            "When a commercial bank generally makes a loan, what happens?",
            [
                "Only the borrower's debt increases",
                "A deposit is generally created alongside the loan",
                "The bank prints physical currency",
                "The loan automatically becomes free money"
            ],
            key="l2_quiz"
        )

        if st.button("Check Answer", key="l2_quiz_check"):

            if question == "A deposit is generally created alongside the loan":
                st.session_state.l2_quiz_passed = True
                st.success("Correct! A bank loan generally creates a deposit and a corresponding loan asset.")
            else:
                st.session_state.l2_quiz_passed = False
                st.error("Not quite. Think about what the bank records when it lends.")

        if st.session_state.get("l2_quiz_passed", False):

            if st.button("🏁 Complete Lesson 2", key="l2_finish"):
                st.session_state.l2_scene = 8
                st.rerun()

    # SCENE 8 — COMPLETION

    elif scene == 8:

        st.balloons()

        animation("""
        <div style="height:230px;background:linear-gradient(135deg,#14532d,#16a34a);
        border-radius:20px;color:white;display:flex;align-items:center;
        justify-content:center;flex-direction:column">

        <div style="font-size:80px;animation:bounce 2s infinite">🎓</div>
        <h2>Lesson Completed!</h2>

        <style>
        @keyframes bounce {
        0%,100% {transform:translateY(0)}
        50% {transform:translateY(-12px)}
        }
        </style>
        </div>
        """)

        st.markdown("## 🎉 Great Work!")

        st.write("""
        You learned:

        - How bank loans work.
        - The difference between deposits and debt.
        - How commercial banks generally create deposits through lending.
        - How interest affects loan repayment.
        - Why borrowing decisions matter.
        """)

        st.markdown("---")

        st.markdown("### 🔓 Next: Lesson 3")

        st.write("Continue your journey to learn the next financial concept.")

        if st.button("➡️ Continue to Lesson 3", key="l2_to_l3"):

            if "page" in st.session_state:
                st.session_state.page = "Lesson 3"

            st.session_state.l2_scene = 0
            st.rerun()

    # NAVIGATION

    if scene > 0 and scene < 8:

        st.markdown("---")

        if st.button("⬅️ Previous Scene", key=f"l2_back_{scene}"):

            if scene == 4 and st.session_state.get("l2_choice") == "Accept the loan":
                st.session_state.l2_scene = 2
            elif scene == 4 and st.session_state.get("l2_choice") == "Reject the loan":
                st.session_state.l2_scene = 3
            else:
                previous_scene()

            st.rerun()

    st.caption("MoneyLab • Learn Money by Living It")
