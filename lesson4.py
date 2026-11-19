
import streamlit as st
import streamlit.components.v1 as components

def show_lesson4():

    st.title("💰 Lesson 4: Smart Spending")
    st.caption("Learn Money by Living It")

    if "l4_stage" not in st.session_state:
        st.session_state.l4_stage = 0

    if "l4_budget" not in st.session_state:
        st.session_state.l4_budget = None

    stage = st.session_state.l4_stage

    # BACK BUTTON
    if stage > 0:
        if st.button("← Back"):
            st.session_state.l4_stage -= 1
            st.rerun()

    # STAGE 0: STORY INTRO
    if stage == 0:

        components.html("""
        <div style="background:linear-gradient(135deg,#0f172a,#2563eb);
        color:white;padding:25px;border-radius:20px;text-align:center;
        font-family:sans-serif;">
        <div style="font-size:80px;animation:float 2s infinite alternate;">🧑‍💼</div>
        <h2>Meet Alex!</h2>
        <p>Alex just received a monthly salary.</p>
        <h1 style="color:#86efac;">₹30,000</h1>
        <div style="font-size:45px;animation:money 2s infinite;">💰</div>
        <p>Alex needs to make some financial decisions.</p>
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
        """, height=330)

        st.write(
            "You are Alex's financial decision-maker. "
            "Decide how to use this ₹30,000 salary."
        )

        if st.button("Start Making Decisions →"):
            st.session_state.l4_stage = 1
            st.rerun()

    # STAGE 1: DECISIONS
    elif stage == 1:

        st.subheader("📝 Make Your Spending Decisions")

        st.write("You decide how much Alex will spend in each category.")

        salary = 30000

        with st.form("l4_budget_form"):

            st.markdown("### 🟢 Needs")
            st.caption(
                "Things essential for living and daily life."
            )

            rent = st.number_input(
                "Rent (₹)", min_value=0, max_value=salary,
                value=0, step=500
            )

            food = st.number_input(
                "Food and groceries (₹)", min_value=0,
                max_value=salary, value=0, step=500
            )

            transport = st.number_input(
                "Transport (₹)", min_value=0,
                max_value=salary, value=0, step=500
            )

            bills = st.number_input(
                "Electricity, internet and other bills (₹)",
                min_value=0, max_value=salary,
                value=0, step=500
            )

            st.markdown("### 🔵 Wants")
            st.caption(
                "Things that make life enjoyable but aren't essential."
            )

            eating_out = st.number_input(
                "Restaurants and eating out (₹)",
                min_value=0, max_value=salary,
                value=0, step=500
            )

            entertainment = st.number_input(
                "Entertainment and hobbies (₹)",
                min_value=0, max_value=salary,
                value=0, step=500
            )

            st.markdown("### 🟠 Luxuries")
            st.caption(
                "Expensive extras and premium things "
                "you can live without."
            )

            luxury = st.number_input(
                "Luxury shopping and upgrades (₹)",
                min_value=0, max_value=salary,
                value=0, step=500
            )

            st.markdown("### 🟣 Future")
            st.caption(
                "Money you keep for emergencies and future goals."
            )

            savings = st.number_input(
                "Savings (₹)", min_value=0,
                max_value=salary, value=0, step=500
            )

            submit = st.form_submit_button(
                "Calculate My Decisions →"
            )

        if submit:

            total = (
                rent + food + transport + bills +
                eating_out + entertainment + luxury + savings
            )

            st.session_state.l4_budget = {
                "rent": rent,
                "food": food,
                "transport": transport,
                "bills": bills,
                "eating_out": eating_out,
                "entertainment": entertainment,
                "luxury": luxury,
                "savings": savings,
                "total": total
            }

            st.session_state.l4_stage = 2
            st.rerun()

    # STAGE 2: CONSEQUENCES
    elif stage == 2:

        b = st.session_state.l4_budget
        salary = 30000
        total = b["total"]
        remaining = salary - total

        st.subheader("📊 Alex's Financial Outcome")

        components.html("""
        <div style="background:linear-gradient(135deg,#064e3b,#10b981);
        padding:20px;border-radius:20px;text-align:center;color:white;
        font-family:sans-serif;">
        <div style="font-size:65px;animation:pop 1.5s infinite alternate;">💸</div>
        <h2>Money Report</h2>
        <p>Your decisions have changed Alex's financial situation!</p>
        <style>
        @keyframes pop {
        from {transform:scale(.9)}
        to {transform:scale(1.1)}
        }
        </style>
        </div>
        """, height=230)

        st.write(f"**Monthly income:** ₹{salary:,}")
        st.write(f"**Total allocated:** ₹{total:,}")

        st.divider()

        st.markdown("### Your Spending Breakdown")

        st.write(f"🟢 Needs: ₹{b['rent']+b['food']+b['transport']+b['bills']:,}")
        st.write(f"🔵 Wants: ₹{b['eating_out']+b['entertainment']:,}")
        st.write(f"🟠 Luxuries: ₹{b['luxury']:,}")
        st.write(f"🟣 Savings: ₹{b['savings']:,}")

        st.divider()

        if remaining >= 0:
            st.markdown(f"## 💵 Unallocated money: ₹{remaining:,}")
        else:
            st.markdown(f"## 🔴 Overspending: ₹{abs(remaining):,}")

        st.markdown("### 🧠 Decision Analysis")

        needs_total = (
            b["rent"] + b["food"] + b["transport"] + b["bills"]
        )
        wants_total = b["eating_out"] + b["entertainment"]
        luxury_total = b["luxury"]

        if total > salary:
            st.error(
                "Alex allocated more money than the salary. "
                "This budget is not financially sustainable."
            )
        else:
            st.success(
                "Alex stayed within the monthly income "
                "based on the amounts entered."
            )

        if needs_total == 0:
            st.warning(
                "No money was allocated to needs. "
                "Essential expenses should be considered first."
            )

        if wants_total + luxury_total > needs_total:
            st.warning(
                "Wants and luxuries are higher than needs. "
                "Consider whether some optional spending should be reduced."
            )
        else:
            st.info(
                "Optional spending is not greater than the needs allocation. "
                "Review whether the needs allocation is realistic."
            )

        if b["savings"] == 0:
            st.warning(
                "Alex allocated nothing to savings. "
                "Try building an emergency fund."
            )
        else:
            st.success(
                f"Alex saved ₹{b['savings']:,}. "
                "Saving money can help with unexpected expenses and goals."
            )

        if remaining < 0:
            st.error(
                "Alex has a budget deficit. "
                "Reduce optional spending or review the budget."
            )
        elif remaining > 0:
            st.info(
                "Some money is still unallocated. "
                "It could be saved, invested later, or reserved for future needs."
            )
        else:
            st.info(
                "Every rupee has been allocated. "
                "Make sure the budget also allows flexibility."
            )

        st.divider()

        st.markdown("## 📚 What You Learned")

        st.markdown("""
        ### 1. Needs come first
        Needs are essential for living, such as food, housing,
        basic transport and necessary bills.

        ### 2. Wants are optional
        Wants make life enjoyable, such as restaurants, entertainment
        and hobbies. They are not essential for survival.

        ### 3. Luxuries are optional upgrades
        Luxury items may be expensive or premium versions of things.
        Think carefully before buying them.

        ### 4. Save before spending everything
        Saving helps you prepare for emergencies, future plans
        and financial independence.

        ### 5. Don't spend more than you earn
        Spending more than your income can lead to debt and financial stress.

        ### 6. Every spending decision has a consequence
        Money spent today cannot be used for another purpose tomorrow.
        """)

        st.markdown("## 💡 A Smarter Way to Spend")

        st.markdown("""
        - **First:** Plan essential needs.
        - **Second:** Decide how much you can afford for wants.
        - **Third:** Avoid unnecessary luxury purchases.
        - **Fourth:** Set aside savings for emergencies and goals.
        - **Fifth:** Review your budget before spending.

        <div style="background:linear-gradient(135deg,#1e3a8a,#2563eb);
        padding:20px;border-radius:18px;color:white;text-align:center;">
        <h3>Needs → Savings → Wants → Luxuries</h3>
        <p>Prioritize your essentials, protect your future
        and enjoy the money you can afford to spend.</p>
        </div>
        """, unsafe_allow_html=True)

        if st.button("🔄 Play Again"):
            st.session_state.l4_stage = 0
            st.session_state.l4_budget = None
            st.rerun()

    st.divider()
    st.caption("MoneyLab | Learn Money by Living It")
