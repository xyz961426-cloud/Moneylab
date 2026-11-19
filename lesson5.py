
import streamlit as st
import streamlit.components.v1 as components

def show_lesson5():

    st.title("🚨 Lesson 5: The Emergency Trap")
    st.caption("MoneyLab | Learn Money by Living It")

    if "l5_stage" not in st.session_state:
        st.session_state.l5_stage = 0
    if "l5_choice" not in st.session_state:
        st.session_state.l5_choice = None

    stage = st.session_state.l5_stage

    # BACK BUTTON
    if stage > 0:
        if st.button("← Back"):
            st.session_state.l5_stage -= 1
            st.rerun()

    # SCENE 1: INTRO
    if stage == 0:

        components.html("""
        <div style="background:linear-gradient(135deg,#0f172a,#1d4ed8);
        padding:25px;border-radius:20px;color:white;text-align:center;
        font-family:sans-serif;">
        <div style="font-size:80px;animation:float 2s infinite alternate;">🧑‍💼</div>
        <h2>Meet Alex!</h2>
        <p>Alex works hard and earns money every month.</p>
        <div style="font-size:60px;animation:money 2s infinite;">💰</div>
        <p>But today something unexpected happens...</p>
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

        if st.button("Continue →"):
            st.session_state.l5_stage = 1
            st.rerun()

    # SCENE 2: EMERGENCY
    elif stage == 1:

        st.subheader("🏍️ The Unexpected Emergency")

        components.html("""
        <div style="background:linear-gradient(135deg,#7f1d1d,#dc2626);
        padding:25px;border-radius:20px;color:white;text-align:center;
        font-family:sans-serif;">
        <div style="font-size:80px;animation:shake 1s infinite;">🏍️</div>
        <h2>Motorcycle Breakdown!</h2>
        <p>Alex needs his motorcycle to get to work.</p>
        <h2>Repair cost: ₹4,000</h2>
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
        """, height=280)

        st.write(
            "The mechanic says the repair will cost ₹4,000. "
            "Alex only has ₹1,000 in emergency savings."
        )

        if st.button("See Alex's Options →"):
            st.session_state.l5_stage = 2
            st.rerun()

    # SCENE 3: CHOICES
    elif stage == 2:

        st.subheader("🤔 What Should Alex Do?")

        st.write("You must decide how Alex will handle this emergency.")

        st.markdown("### 🟢 Option 1: Use Savings + Borrow")
        st.write(
            "Alex uses his ₹1,000 savings and borrows "
            "the remaining ₹3,000."
        )

        if st.button("Choose Option 1"):
            st.session_state.l5_choice = 1
            st.session_state.l5_stage = 3
            st.rerun()

        st.divider()

        st.markdown("### 🔴 Option 2: Borrow the Entire Amount")
        st.write("Alex borrows the full ₹4,000.")

        if st.button("Choose Option 2"):
            st.session_state.l5_choice = 2
            st.session_state.l5_stage = 3
            st.rerun()

        st.divider()

        st.markdown("### 🟡 Option 3: Delay the Repair")
        st.write("Alex delays the repair and tries to manage without it.")

        if st.button("Choose Option 3"):
            st.session_state.l5_choice = 3
            st.session_state.l5_stage = 4
            st.rerun()

    # SCENE 4: LOAN CALCULATOR
    elif stage == 3:

        choice = st.session_state.l5_choice

        if choice == 1:
            loan = 3000
            st.subheader("💳 Alex Borrows ₹3,000")
            st.write("Alex uses ₹1,000 of savings.")
        else:
            loan = 4000
            st.subheader("💳 Alex Borrows ₹4,000")
            st.write("Alex keeps his ₹1,000 savings untouched.")

        st.write("Now let's see what borrowing actually costs.")

        with st.form("l5_loan_form"):

            rate = st.number_input(
                "Monthly interest rate (%)",
                min_value=0.0,
                max_value=100.0,
                value=3.0,
                step=0.5
            )

            months = st.number_input(
                "Repayment period (months)",
                min_value=1,
                max_value=60,
                value=3,
                step=1
            )

            submit = st.form_submit_button("Calculate Loan →")

        if submit:

            total_interest = loan * (rate / 100) * months
            total_repayment = loan + total_interest

            st.session_state.l5_loan = loan
            st.session_state.l5_interest = total_interest
            st.session_state.l5_repayment = total_repayment
            st.session_state.l5_months = months
            st.session_state.l5_rate = rate

            st.session_state.l5_stage = 5
            st.rerun()

    # SCENE 5: LOAN RESULT
    elif stage == 5:

        loan = st.session_state.l5_loan
        interest = st.session_state.l5_interest
        repayment = st.session_state.l5_repayment
        months = st.session_state.l5_months

        st.subheader("📊 The Cost of Borrowing")

        components.html("""
        <div style="background:linear-gradient(135deg,#7c2d12,#ea580c);
        padding:20px;border-radius:20px;color:white;text-align:center;
        font-family:sans-serif;">
        <div style="font-size:60px;animation:pop 1.5s infinite alternate;">💸</div>
        <h2>Borrowing Isn't Free!</h2>
        <style>
        @keyframes pop {
        from {transform:scale(.9)}
        to {transform:scale(1.1)}
        }
        </style>
        </div>
        """, height=220)

        st.write(f"**Amount borrowed:** ₹{loan:,}")
        st.write(f"**Interest:** ₹{interest:,.2f}")
        st.write(f"**Total repayment:** ₹{repayment:,.2f}")
        st.write(f"**Repayment period:** {months} months")

        st.info(
            "This calculator uses simple interest for learning. "
            "Actual loans may use different interest calculations, "
            "fees and repayment structures."
        )

        st.markdown(
            f"### Approximate monthly payment: "
            f"₹{repayment/months:,.2f}"
        )

        if st.button("See the Consequences →"):
            st.session_state.l5_stage = 6
            st.rerun()

    # SCENE 6: DELAY
    elif stage == 4:

        st.subheader("⏳ Alex Delays the Repair")

        components.html("""
        <div style="background:linear-gradient(135deg,#1e3a8a,#2563eb);
        padding:25px;border-radius:20px;color:white;text-align:center;
        font-family:sans-serif;">
        <div style="font-size:75px;animation:float 2s infinite alternate;">🚶</div>
        <h2>No Immediate Loan</h2>
        <p>Alex tries to manage without repairing the motorcycle.</p>
        <style>
        @keyframes float {
        from {transform:translateY(0)}
        to {transform:translateY(-10px)}
        }
        </style>
        </div>
        """, height=250)

        st.write("""
        Alex avoids borrowing today. However, he may face transport
        problems, delays or additional costs.

        Delaying is not always the cheapest option. The consequences
        depend on how urgently the motorcycle is needed and what
        alternatives are available.
        """)

        if st.button("See the Outcome →"):
            st.session_state.l5_stage = 6
            st.rerun()

    # SCENE 7: FINAL ANALYSIS
    elif stage == 6:

        choice = st.session_state.l5_choice

        st.subheader("📚 The Financial Lesson")

        if choice == 1:

            components.html("""
            <div style="background:linear-gradient(135deg,#065f46,#10b981);
            padding:25px;border-radius:20px;color:white;text-align:center;
            font-family:sans-serif;">
            <div style="font-size:65px;">🛡️</div>
            <h2>Alex Used His Savings!</h2>
            <p>He reduced the amount he needed to borrow.</p>
            </div>
            """, height=230)

            st.success(
                "Using part of an emergency fund can reduce "
                "the amount of debt and interest."
            )

        elif choice == 2:

            components.html("""
            <div style="background:linear-gradient(135deg,#7f1d1d,#dc2626);
            padding:25px;border-radius:20px;color:white;text-align:center;
            font-family:sans-serif;">
            <div style="font-size:65px;">💳</div>
            <h2>Alex Borrowed Everything!</h2>
            <p>His savings stayed intact, but he owes more.</p>
            </div>
            """, height=230)

            st.warning(
                "Keeping savings can sometimes be useful, "
                "but borrowing more can increase interest costs. "
                "Compare the cost of borrowing with the value "
                "of keeping your emergency money."
            )

        else:

            components.html("""
            <div style="background:linear-gradient(135deg,#1e3a8a,#60a5fa);
            padding:25px;border-radius:20px;color:white;text-align:center;
            font-family:sans-serif;">
            <div style="font-size:65px;">🚶</div>
            <h2>Alex Delayed!</h2>
            <p>He avoided borrowing for now.</p>
            </div>
            """, height=230)

            st.info(
                "Avoiding debt may be helpful, but delaying "
                "an essential repair can also create costs. "
                "Evaluate alternatives before deciding."
            )

        st.markdown("## 🧠 What You Learned")

        st.markdown("""
        ### 1. What is an emergency fund?
        Money set aside for unexpected but necessary expenses,
        such as repairs, medical costs or sudden income loss.

        ### 2. Why save before an emergency?
        Savings can reduce the need to borrow when something
        unexpected happens.

        ### 3. Borrowing has a cost
        Interest and fees can make borrowed money more expensive
        than the original amount.

        ### 4. Avoid unnecessary debt
        Borrow only after understanding the total repayment,
        interest, fees and your ability to repay.

        ### 5. Build financial protection
        Start with a small emergency fund and gradually increase it.
        Even small savings can help.

        ### 6. Compare your options
        Using savings, borrowing or delaying may have different
        consequences. Consider urgency, costs, risks and alternatives.
        """)

        st.markdown("## 💡 A Better Financial Approach")

        st.markdown("""
        - Build emergency savings gradually.
        - Keep emergency money accessible.
        - Understand loan costs before borrowing.
        - Avoid borrowing for unnecessary purchases.
        - Plan for unexpected expenses.
        """)

        st.markdown(
            "<div style='background:linear-gradient(135deg,#064e3b,#059669);"
            "padding:20px;border-radius:18px;color:white;text-align:center;'>"
            "<h3>Prepare Before the Emergency!</h3>"
            "<p>Your savings can give you choices when life becomes unpredictable.</p>"
            "</div>",
            unsafe_allow_html=True
        )

        if st.button("🔄 Play Again"):
            st.session_state.l5_stage = 0
            st.session_state.l5_choice = None
            for key in [
                "l5_loan", "l5_interest", "l5_repayment",
                "l5_months", "l5_rate"
            ]:
                if key in st.session_state:
                    del st.session_state[key]
            st.rerun()

    st.divider()
    st.caption("MoneyLab | Learn Money by Living It")
