import streamlit as st

def show_lesson4():
    st.title("💼 Lesson 4: Your First Salary")
    st.subheader("Learn money by living it")

    st.markdown("""
    Imagine you just received your first monthly salary.

    You must manage your money carefully. Every decision has consequences.
    """)

    if "salary_cash" not in st.session_state:
        st.session_state.salary_cash = 30000
        st.session_state.salary_spent = 0
        st.session_state.salary_started = False

    if not st.session_state.salary_started:
        st.markdown("### 🎬 Your Story")
        st.write("You just received ₹30,000 in your bank account.")
        st.write("Your goal is to survive the month, pay your bills and save money.")

        if st.button("Receive Salary 💰"):
            st.session_state.salary_started = True
            st.rerun()

    else:
        st.markdown("### 🏦 Your Wallet")

        col1, col2 = st.columns(2)
        col1.metric("Money Remaining", f"₹{st.session_state.salary_cash:,}")
        col2.metric("Money Spent", f"₹{st.session_state.salary_spent:,}")

        st.progress(st.session_state.salary_cash / 30000)

        st.markdown("### 🏠 Step 1: Pay Essential Expenses")

        expenses = {
            "Rent": 8000,
            "Food": 4000,
            "Transport": 2000,
            "Utilities": 1500,
        }

        for name, amount in expenses.items():
            if st.button(f"Pay {name} — ₹{amount:,}", key=name):
                if st.session_state.salary_cash >= amount:
                    st.session_state.salary_cash -= amount
                    st.session_state.salary_spent += amount
                    st.success(f"{name} paid successfully!")
                    st.rerun()
                else:
                    st.error("Not enough money!")

        st.markdown("### 🛍️ Step 2: Your Choice")

        choice = st.selectbox(
            "What do you want to buy?",
            ["Nothing", "New headphones (₹3,000)", "New shoes (₹2,500)", "Gaming subscription (₹1,000)"]
        )

        if st.button("Buy Item"):
            prices = {
                "Nothing": 0,
                "New headphones (₹3,000)": 3000,
                "New shoes (₹2,500)": 2500,
                "Gaming subscription (₹1,000)": 1000,
            }

            amount = prices[choice]

            if st.session_state.salary_cash >= amount:
                st.session_state.salary_cash -= amount
                st.session_state.salary_spent += amount
                st.success("Purchase completed!")
                st.rerun()
            else:
                st.error("You cannot afford this!")

        st.markdown("### 🚨 Step 3: Unexpected Emergency")

        if "salary_emergency" not in st.session_state:
            st.session_state.salary_emergency = False

        if not st.session_state.salary_emergency:
            if st.button("An emergency happens!"):
                st.session_state.salary_emergency = True
                st.rerun()
        else:
            st.warning("Your phone suddenly breaks. Repair cost: ₹2,000")

            if st.button("Repair Phone — ₹2,000"):
                if st.session_state.salary_cash >= 2000:
                    st.session_state.salary_cash -= 2000
                    st.session_state.salary_spent += 2000
                    st.success("Phone repaired!")
                    st.rerun()
                else:
                    st.error("You don't have enough money to repair it.")

        st.markdown("### 💰 Step 4: Save Money")

        save_amount = st.number_input(
            "How much money do you want to save?",
            min_value=0,
            max_value=st.session_state.salary_cash,
            step=500
        )

        if st.button("Save Money"):
            st.session_state.salary_cash -= save_amount
            st.session_state.salary_spent += save_amount
            st.success(f"₹{save_amount:,} moved to savings!")
            st.rerun()

        st.markdown("---")
        st.markdown("### 📊 Your Final Financial Situation")

        st.metric("Remaining Cash", f"₹{st.session_state.salary_cash:,}")
        st.metric("Total Allocated", f"₹{st.session_state.salary_spent:,}")

        if st.session_state.salary_cash > 0:
            st.info("You still have money available. Think about your next financial decision.")
        else:
            st.warning("You have run out of money!")

        if st.button("Restart Simulation"):
            st.session_state.salary_cash = 30000
            st.session_state.salary_spent = 0
            st.session_state.salary_started = False
            st.session_state.salary_emergency = False
            st.rerun()
