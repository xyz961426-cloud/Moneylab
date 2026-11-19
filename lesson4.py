import streamlit as st

def show_lesson4():

    st.title("💼 Your First Salary")
    st.caption("MoneyLab | Learn Money by Living It")

    st.markdown("""
    <div style="background:linear-gradient(135deg,#132b46,#1c5a72);
    padding:25px;border-radius:18px;color:white;">
    <h2>Welcome to your first month of financial independence!</h2>
    <p>You have just received your salary. Your decisions will determine
    how much money you keep, save and spend.</p>
    </div>
    """, unsafe_allow_html=True)

    if "l4_started" not in st.session_state:
        st.session_state.l4_started = False
        st.session_state.l4_cash = 30000
        st.session_state.l4_savings = 0
        st.session_state.l4_paid = set()
        st.session_state.l4_purchases = set()
        st.session_state.l4_emergency = False
        st.session_state.l4_emergency_paid = False

    if not st.session_state.l4_started:

        st.markdown("### 💰 Your Salary")
        st.metric("Monthly Salary", "₹30,000")

        st.markdown("""
        Your salary has arrived.

        Your mission:
        - Pay essential expenses.
        - Make smart spending decisions.
        - Handle an unexpected emergency.
        - Protect your savings.
        """)

        if st.button("Start Your Month 🚀", use_container_width=True):
            st.session_state.l4_started = True
            st.rerun()

    else:

        st.markdown("### 🏦 Your Financial Dashboard")

        col1, col2, col3 = st.columns(3)

        col1.metric("Available Cash", f"₹{st.session_state.l4_cash:,}")
        col2.metric("Savings", f"₹{st.session_state.l4_savings:,}")
        col3.metric(
            "Total Wealth",
            f"₹{st.session_state.l4_cash + st.session_state.l4_savings:,}"
        )

        st.progress(
            min(
                (st.session_state.l4_cash +
                 st.session_state.l4_savings) / 30000,
                1.0
            )
        )

        st.markdown("---")
        st.markdown("### 🏠 Step 1 — Essential Expenses")

        expenses = {
            "Rent": 8000,
            "Food": 4000,
            "Transport": 2000,
            "Utilities": 1500
        }

        for name, amount in expenses.items():

            if name in st.session_state.l4_paid:
                st.success(f"✅ {name} paid — ₹{amount:,}")

            else:
                if st.button(
                    f"Pay {name} — ₹{amount:,}",
                    key=f"l4_exp_{name}",
                    use_container_width=True
                ):

                    if st.session_state.l4_cash >= amount:

                        st.session_state.l4_cash -= amount
                        st.session_state.l4_paid.add(name)

                        st.rerun()

                    else:
                        st.error("Insufficient money!")

        st.markdown("---")
        st.markdown("### 🛍️ Step 2 — Lifestyle Choices")

        shopping = {
            "Headphones": 3000,
            "Shoes": 2500,
            "Gaming Subscription": 1000
        }

        for name, amount in shopping.items():

            if name in st.session_state.l4_purchases:
                st.info(f"Purchased: {name} — ₹{amount:,}")

            else:

                if st.button(
                    f"Buy {name} — ₹{amount:,}",
                    key=f"l4_buy_{name}",
                    use_container_width=True
                ):

                    if st.session_state.l4_cash >= amount:

                        st.session_state.l4_cash -= amount
                        st.session_state.l4_purchases.add(name)

                        st.rerun()

                    else:
                        st.error("You cannot afford this purchase.")

        st.markdown("---")
        st.markdown("### 🚨 Step 3 — Unexpected Emergency")

        if not st.session_state.l4_emergency:

            st.warning(
                "Your phone suddenly breaks. "
                "Repair cost: ₹2,000."
            )

            if st.button("Reveal Emergency", use_container_width=True):
                st.session_state.l4_emergency = True
                st.rerun()

        else:

            if st.session_state.l4_emergency_paid:
                st.success("Phone repaired.")

            else:

                st.warning("Phone repair costs ₹2,000.")

                if st.button("Repair Phone", use_container_width=True):

                    if st.session_state.l4_cash >= 2000:

                        st.session_state.l4_cash -= 2000
                        st.session_state.l4_emergency_paid = True

                        st.rerun()

                    else:
                        st.error(
                            "You don't have enough cash. "
                            "Consider whether your savings plan was too aggressive."
                        )

        st.markdown("---")
        st.markdown("### 💰 Step 4 — Build Your Savings")

        st.write(
            "Move money from your available cash into savings. "
            "Savings are still your money."
        )

        if st.session_state.l4_cash > 0:

            amount = st.number_input(
                "Amount to save",
                min_value=0,
                max_value=st.session_state.l4_cash,
                step=500,
                key="l4_saving_input"
            )

            if st.button("Transfer to Savings", use_container_width=True):

                st.session_state.l4_cash -= amount
                st.session_state.l4_savings += amount

                st.rerun()

        else:
            st.info("No cash available to save.")

        st.markdown("---")
        st.markdown("### 📊 Financial Summary")

        total_salary = 30000
        total_cash = st.session_state.l4_cash
        total_savings = st.session_state.l4_savings
        total_wealth = total_cash + total_savings

        total_paid = sum(
            expenses[name]
            for name in st.session_state.l4_paid
        )

        total_shopping = sum(
            shopping[name]
            for name in st.session_state.l4_purchases
        )

        emergency_cost = (
            2000 if st.session_state.l4_emergency_paid else 0
        )

        st.metric("Salary Received", f"₹{total_salary:,}")
        st.metric("Essential Expenses Paid", f"₹{total_paid:,}")
        st.metric("Lifestyle Purchases", f"₹{total_shopping:,}")
        st.metric("Emergency Cost", f"₹{emergency_cost:,}")
        st.metric("Money Saved", f"₹{total_savings:,}")
        st.metric("Cash Remaining", f"₹{total_cash:,}")

        st.markdown("### 🧠 What Did You Learn?")

        if total_wealth >= 20000:

            st.success(
                "Strong financial decisions! You protected a large "
                "portion of your salary."
            )

        elif total_wealth >= 10000:

            st.info(
                "You managed your money reasonably well. "
                "Try reducing unnecessary spending next time."
            )

        else:

            st.warning(
                "Most of your salary has been used. "
                "Planning expenses before spending can help."
            )

        st.markdown("""
        **Real financial lessons:**

        - A salary is not the same as wealth.
        - Essential expenses should be planned first.
        - Unexpected expenses are part of real life.
        - Savings are not expenses; they remain your assets.
        - Spending decisions have opportunity costs.
        """)

        if st.button("Restart Your Month 🔄", use_container_width=True):

            for key in [
                "l4_started",
                "l4_cash",
                "l4_savings",
                "l4_paid",
                "l4_purchases",
                "l4_emergency",
                "l4_emergency_paid"
            ]:
                del st.session_state[key]

            st.rerun()
