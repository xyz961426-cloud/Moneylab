import streamlit as st
import plotly.graph_objects as go

# ============================================================
# MONEYLAB — CHAPTER 3 REBUILT
# Building Your Financial Foundation
# Lessons 9–12
# ============================================================

LESSONS = [
    "Lesson 9 — Build Your Financial Plan",
    "Lesson 10 — Master Your Cash Flow",
    "Lesson 11 — Protect Yourself",
    "Lesson 12 — Spend With Intelligence",
]

def init_state():
    defaults = {
        "c3_new_lesson": 0,
        "c3_new_completed": set(),
        "c3_new_quiz9": None,
        "c3_new_quiz10": None,
        "c3_new_quiz11": None,
        "c3_new_quiz12": None,
        "c3_new_decision": None,
        "c3_new_budget_income": 30000,
        "c3_new_goal": 40000,
    }

    for key, value in defaults.items():
        if key not in st.session_state:
            st.session_state[key] = value


def money(value):
    return f"₹{value:,.0f}"


def hero(title, subtitle, emoji):
    st.markdown(
        f"""
        <div class="c3-hero">
            <div class="c3-hero-emoji">{emoji}</div>
            <h1>{title}</h1>
            <p>{subtitle}</p>
        </div>
        """,
        unsafe_allow_html=True,
    )


def scene(title, story, emoji="🎬"):
    st.markdown(
        f"""
        <div class="c3-scene">
            <div class="c3-scene-emoji">{emoji}</div>
            <h3>{title}</h3>
            <p>{story}</p>
        </div>
        """,
        unsafe_allow_html=True,
    )


def info_card(title, content, emoji="💡"):
    st.markdown(
        f"""
        <div class="c3-card">
            <h4>{emoji} {title}</h4>
            <p>{content}</p>
        </div>
        """,
        unsafe_allow_html=True,
    )


def animated_flow():
    st.markdown(
        """
        <div class="c3-flow">
            <div class="c3-flow-item">
                <div>💼</div>
                <b>Income</b>
            </div>
            <div class="c3-arrow">➜</div>
            <div class="c3-flow-item">
                <div>🧾</div>
                <b>Expenses</b>
            </div>
            <div class="c3-arrow">➜</div>
            <div class="c3-flow-item">
                <div>🏦</div>
                <b>Savings</b>
            </div>
            <div class="c3-arrow">➜</div>
            <div class="c3-flow-item">
                <div>🎯</div>
                <b>Goals</b>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )


def quiz(question, options, correct, explanation, key):
    st.markdown("### 🧠 Decision Challenge")
    st.write(question)

    selected = st.radio(
        "Choose your answer",
        options,
        index=None,
        key=key + "_choice",
    )

    if st.button("Check answer", key=key + "_check"):
        st.session_state[key] = selected

    answer = st.session_state.get(key)

    if answer is not None:
        if answer == correct:
            st.success("Correct! " + explanation)
        else:
            st.error(
                "That answer is incorrect. "
                "The correct answer is: "
                + correct
            )
            st.info(explanation)

    return selected


def completion_button(lesson_number):
    if st.button(
        "✅ Mark this lesson complete",
        key=f"c3_new_finish_{lesson_number}",
        use_container_width=True,
    ):
        st.session_state.c3_new_completed.add(lesson_number)
        st.success("Lesson completed!")
        st.balloons()


def navigation():
    current = st.session_state.c3_new_lesson

    st.progress((current + 1) / len(LESSONS))

    st.caption(
        f"Chapter progress • Lesson {current + 1} of {len(LESSONS)}"
    )

    st.selectbox(
        "Go to lesson",
        LESSONS,
        index=current,
        key="c3_new_navigation",
        on_change=change_lesson,
    )

    left, right = st.columns(2)

    with left:
        if st.button(
            "⬅ Previous lesson",
            disabled=current == 0,
            key="c3_new_previous",
            use_container_width=True,
        ):
            st.session_state.c3_new_lesson -= 1
            st.rerun()

    with right:
        if st.button(
            "Next lesson ➡",
            disabled=current == 3,
            key="c3_new_next",
            use_container_width=True,
        ):
            st.session_state.c3_new_lesson += 1
            st.rerun()


def change_lesson():
    st.session_state.c3_new_lesson = (
        LESSONS.index(st.session_state.c3_new_navigation)
    )


def show_lesson9():

    hero(
        "Your First Financial Plan",
        "Give your money a purpose before it disappears.",
        "🧭",
    )

    scene(
        "Alex's first paycheck",
        "Alex receives ₹30,000. He wants a laptop, "
        "financial security and a better future. "
        "But he has never made a financial plan.",
        "🧑‍💼",
    )

    animated_flow()

    st.subheader("Why a financial plan matters")

    st.write(
        "A financial plan helps you decide how money should "
        "be used instead of making every decision at the moment "
        "you spend."
    )

    st.markdown("""
    - **Protect:** Prepare for unexpected expenses.
    - **Control:** Understand spending.
    - **Plan:** Work toward purchases.
    - **Grow:** Build long-term financial goals.
    """)

    with st.expander("What is a financial goal?"):
        st.write(
            "A financial goal is something you want to achieve "
            "with money. Goals can be short-term, medium-term "
            "or long-term."
        )

        st.markdown("""
        **Short-term:** A phone, emergency savings or a trip.

        **Medium-term:** Education, a vehicle or a larger purchase.

        **Long-term:** Retirement, wealth-building or financial independence.
        """)

    st.subheader("🎮 Create Alex's plan")

    income = st.number_input(
        "Monthly take-home income",
        min_value=0,
        value=30000,
        step=1000,
        key="c3_new_l9_income",
    )

    essentials = st.slider(
        "Essential expenses",
        0,
        max(1, income),
        min(15000, income),
        step=500,
        key="c3_new_l9_essential",
    )

    lifestyle = st.slider(
        "Lifestyle spending",
        0,
        max(1, income),
        min(4000, income),
        step=500,
        key="c3_new_l9_lifestyle",
    )

    emergency = st.slider(
        "Emergency fund contribution",
        0,
        max(1, income),
        min(3000, income),
        step=500,
        key="c3_new_l9_emergency",
    )

    goals = st.slider(
        "Goal savings",
        0,
        max(1, income),
        min(3000, income),
        step=500,
        key="c3_new_l9_goal",
    )

    allocated = essentials + lifestyle + emergency + goals
    remainder = income - allocated

    fig = go.Figure(
        go.Pie(
            labels=[
                "Essentials",
                "Lifestyle",
                "Emergency",
                "Goals",
                "Unallocated",
            ],
            values=[
                essentials,
                lifestyle,
                emergency,
                goals,
                max(0, remainder),
            ],
            hole=0.55,
        )
    )

    fig.update_layout(
        height=380,
        title="Your monthly financial allocation",
    )

    st.plotly_chart(fig, use_container_width=True)

    st.metric("Income", money(income))
    st.metric("Allocated", money(allocated))
    st.metric("Remaining", money(remainder))

    if remainder < 0:
        st.error(
            "You allocated more than your income. "
            "Reduce one or more categories."
        )
    elif remainder > 0:
        st.info(
            "You still have money without a specific purpose. "
            "Consider assigning it to a goal or future expense."
        )
    else:
        st.success("Your entire income has been allocated.")

    st.subheader("🎯 Goal planning simulator")

    goal_amount = st.number_input(
        "What is Alex's goal?",
        min_value=1000,
        value=40000,
        step=1000,
        key="c3_new_l9_goal_amount",
    )

    monthly_saving = st.slider(
        "Monthly savings toward this goal",
        500,
        30000,
        5000,
        step=500,
        key="c3_new_l9_monthly",
    )

    goal_months = goal_amount / monthly_saving

    st.metric(
        "Estimated time",
        f"{goal_months:.1f} months",
    )

    st.write(
        f"At {money(monthly_saving)} per month, "
        f"Alex needs approximately {goal_months:.1f} months "
        f"to save {money(goal_amount)}."
    )

    months = list(range(0, 25))
    projected = [
        min(goal_amount, monthly_saving * m)
        for m in months
    ]

    fig = go.Figure()

    fig.add_trace(
        go.Scatter(
            x=months,
            y=projected,
            mode="lines+markers",
            name="Savings",
        )
    )

    fig.add_hline(
        y=goal_amount,
        line_dash="dash",
        annotation_text="Goal",
    )

    fig.update_layout(
        title="Your savings journey",
        xaxis_title="Months",
        yaxis_title="Savings (₹)",
        height=350,
    )

    st.plotly_chart(fig, use_container_width=True)

    st.subheader("Real-world explanation")

    st.write("""
    This projection assumes the money is saved consistently
    and that there is no interest, investment return or
    withdrawal.

    If income changes, the plan should be adjusted.

    A plan is a guide, not a guarantee.
    """)

    quiz(
        "Alex wants a ₹40,000 laptop. He saves ₹5,000 every month. "
        "How long will it take?",
        ["4 months", "8 months", "10 months", "12 months"],
        "8 months",
        "₹40,000 divided by ₹5,000 is 8 months. "
        "The calculation assumes no interest and no withdrawals.",
        "c3_new_quiz9",
    )

    st.markdown("### 🔗 What comes next?")

    st.write(
        "Alex has created a plan. Now he needs to understand "
        "the money actually entering and leaving his account. "
        "Next: Cash flow."
    )

    completion_button(9)


def show_lesson10():

    hero(
        "Master Your Cash Flow",
        "Know where your money comes from and where it goes.",
        "💸",
    )

    scene(
        "Where did the money go?",
        "Alex earns ₹30,000, but at the end of the month "
        "he doesn't know why his balance is so low. "
        "He starts recording every expense.",
        "🔎",
    )

    animated_flow()

    st.subheader("Three important concepts")

    with st.expander("💼 Income"):
        st.write(
            "Income is money received, such as salary, freelance "
            "earnings, business income or rent."
        )

    with st.expander("🧾 Expenses"):
        st.write(
            "Expenses are money spent. They may be fixed, "
            "variable or irregular."
        )

    with st.expander("💰 Cash flow"):
        st.write(
            "Cash flow is the difference between money entering "
            "and leaving during a period."
        )

    st.subheader("🎮 Build your own cash flow")

    income = st.number_input(
        "Monthly income",
        min_value=0,
        value=30000,
        step=1000,
        key="c3_new_l10_income",
    )

    categories = {
        "Housing": 8000,
        "Food": 5000,
        "Transport": 2000,
        "Bills": 2000,
        "Shopping": 4000,
        "Other": 1000,
    }

    expenses = {}

    for name, default in categories.items():
        expenses[name] = st.number_input(
            name,
            min_value=0,
            value=default,
            step=500,
            key=f"c3_new_l10_{name}",
        )

    total = sum(expenses.values())
    cashflow = income - total

    st.metric("Total expenses", money(total))
    st.metric("Monthly cash flow", money(cashflow))

    fig = go.Figure()

    fig.add_trace(
        go.Bar(
            x=list(expenses.keys()),
            y=list(expenses.values()),
            text=[money(x) for x in expenses.values()],
            textposition="auto",
        )
    )

    fig.update_layout(
        title="Where your money goes",
        height=350,
        yaxis_title="₹",
    )

    st.plotly_chart(fig, use_container_width=True)

    if cashflow > 0:
        st.success(
            f"Positive cash flow: {money(cashflow)}. "
            "This is an opportunity to save, invest or plan."
        )
    elif cashflow == 0:
        st.warning(
            "Your income and expenses are equal. "
            "You have no surplus this month."
        )
    else:
        st.error(
            f"Negative cash flow: {money(cashflow)}. "
            "You are spending more than you earn."
        )

    st.subheader("📉 What happens if spending increases?")

    extra = st.slider(
        "Extra monthly spending",
        0,
        10000,
        0,
        step=500,
        key="c3_new_l10_extra",
    )

    adjusted = cashflow - extra

    st.metric(
        "Cash flow after extra spending",
        money(adjusted),
    )

    if adjusted < 0:
        st.error("Your extra spending creates a deficit.")
    else:
        st.info(
            "This spending fits within the current cash flow, "
            "but consider whether it supports your goals."
        )

    st.subheader("🧠 Decision challenge")

    quiz(
        "Alex earns ₹30,000 and spends ₹27,000. "
        "What is his cash flow?",
        ["₹1,000", "₹2,000", "₹3,000", "₹5,000"],
        "₹3,000",
        "₹30,000 minus ₹27,000 equals ₹3,000. "
        "Positive cash flow can help fund goals.",
        "c3_new_quiz10",
    )

    st.markdown("### 🔗 What comes next?")

    st.write(
        "Alex now knows his cash flow. But an unexpected "
        "expense could still disrupt his plan. "
        "Next: The emergency fund."
    )

    completion_button(10)


def show_lesson11():

    hero(
        "Build Your Financial Safety Net",
        "Prepare for unexpected events before they happen.",
        "🛡️",
    )

    scene(
        "The unexpected repair",
        "Alex's laptop breaks. Repairing it costs ₹8,000. "
        "He has only ₹5,000 in savings. "
        "He discovers why emergency savings matter.",
        "💻",
    )

    st.subheader("What is an emergency fund?")

    st.write("""
    An emergency fund is money kept accessible for
    unexpected expenses or income interruptions.

    It can help you avoid relying on expensive borrowing
    or selling investments at an inconvenient time.
    """)

    st.markdown("""
    **Common emergencies:**
    - Medical expenses
    - Essential repairs
    - Loss of income
    - Emergency travel
    - Unexpected necessary bills
    """)

    info_card(
        "Emergency savings are not an investment strategy",
        "Their main purpose is safety and access. "
        "You generally shouldn't depend on volatile investments "
        "to pay for an emergency.",
        "🧯",
    )

    st.subheader("🎮 Calculate your emergency fund")

    monthly_essentials = st.number_input(
        "Essential monthly expenses",
        min_value=0,
        value=15000,
        step=1000,
        key="c3_new_l11_essentials",
    )

    target_months = st.slider(
        "Months of protection",
        1,
        12,
        6,
        key="c3_new_l11_target_months",
    )

    target = monthly_essentials * target_months

    st.metric(
        "Emergency fund target",
        money(target),
    )

    st.write(
        "A commonly used planning target is 3–6 months "
        "of essential expenses. Your circumstances may "
        "justify a different amount."
    )

    current = st.number_input(
        "Current emergency savings",
        min_value=0,
        value=5000,
        step=1000,
        key="c3_new_l11_current",
    )

    contribution = st.slider(
        "Monthly savings contribution",
        0,
        50000,
        3000,
        step=500,
        key="c3_new_l11_contribution",
    )

    missing = max(0, target - current)

    st.metric(
        "Amount still needed",
        money(missing),
    )

    if contribution > 0:
        months_needed = missing / contribution
        st.metric(
            "Estimated time to target",
            f"{months_needed:.1f} months",
        )
    elif missing > 0:
        st.warning(
            "Set a monthly contribution to estimate "
            "how long it will take."
        )
    else:
        st.success("You have reached this target.")

    progress = min(
        current / target if target > 0 else 0,
        1.0,
    )

    st.progress(progress)

    st.caption(
        f"Target progress: {progress*100:.1f}%"
    )

    st.subheader("📈 Build your savings timeline")

    if contribution > 0:

        timeline = list(range(0, 37))

        values = [
            current + contribution * month
            for month in timeline
        ]

        fig = go.Figure()

        fig.add_trace(
            go.Scatter(
                x=timeline,
                y=values,
                mode="lines+markers",
                name="Emergency savings",
            )
        )

        fig.add_hline(
            y=target,
            line_dash="dash",
            annotation_text="Target",
        )

        fig.update_layout(
            title="Emergency fund timeline",
            xaxis_title="Months",
            yaxis_title="₹",
            height=350,
        )

        st.plotly_chart(fig, use_container_width=True)

    st.subheader("⚠️ Emergency scenario")

    repair = st.number_input(
        "Emergency expense",
        min_value=0,
        value=8000,
        step=500,
        key="c3_new_l11_repair",
    )

    available = st.number_input(
        "Money available for the emergency",
        min_value=0,
        value=5000,
        step=500,
        key="c3_new_l11_available",
    )

    shortfall = max(0, repair - available)

    st.metric(
        "Potential shortfall",
        money(shortfall),
    )

    st.write(
        "The shortfall is the amount that isn't covered "
        "by available funds. It is not automatically "
        "the amount you should borrow."
    )

    quiz(
        "A repair costs ₹8,000. Alex has ₹5,000 available. "
        "How much is missing?",
        ["₹1,000", "₹2,000", "₹3,000", "₹5,000"],
        "₹3,000",
        "₹8,000 minus ₹5,000 equals ₹3,000. "
        "Alex must consider his options for the shortfall.",
        "c3_new_quiz11",
    )

    st.markdown("### 🔗 What comes next?")

    st.write(
        "Alex understands saving. Now he must make everyday "
        "spending decisions without sacrificing every enjoyable "
        "thing in life. Next: Needs, wants and spending."
    )

    completion_button(11)


def show_lesson12():

    hero(
        "Spend With Intelligence",
        "Make deliberate decisions without eliminating enjoyment.",
        "🛍️",
    )

    scene(
        "The headphone decision",
        "Alex wants ₹6,000 headphones. He also wants to "
        "save for his laptop and emergency fund. "
        "He must decide whether the purchase fits his plan.",
        "🎧",
    )

    st.subheader("Needs and wants")

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("""
        ### 🏠 Needs

        Examples:
        - Housing
        - Essential food
        - Basic healthcare
        - Essential transport
        - Necessary bills
        """)

    with col2:
        st.markdown("""
        ### 🎮 Wants

        Examples:
        - Luxury upgrades
        - Extra entertainment
        - Premium accessories
        - Non-essential subscriptions
        - Impulse purchases
        """)

    st.info(
        "A purchase can be a need for one person and a want "
        "for another. Context matters."
    )

    st.subheader("🎮 Spending simulator")

    income = st.number_input(
        "Monthly income",
        min_value=0,
        value=30000,
        step=1000,
        key="c3_new_l12_income",
    )

    needs = st.slider(
        "Needs",
        0,
        max(1, income),
        min(15000, income),
        step=500,
        key="c3_new_l12_needs",
    )

    savings = st.slider(
        "Savings",
        0,
        max(1, income),
        min(5000, income),
        step=500,
        key="c3_new_l12_savings",
    )

    wants = st.slider(
        "Wants",
        0,
        max(1, income),
        min(5000, income),
        step=500,
        key="c3_new_l12_wants",
    )

    allocated = needs + savings + wants

    remaining = income - allocated

    st.metric(
        "Money remaining",
        money(remaining),
    )

    fig = go.Figure(
        go.Pie(
            labels=["Needs", "Savings", "Wants", "Remaining"],
            values=[
                needs,
                savings,
                wants,
                max(0, remaining),
            ],
            hole=0.5,
        )
    )

    fig.update_layout(
        title="Spending plan",
        height=350,
    )

    st.plotly_chart(fig, use_container_width=True)

    if remaining < 0:
        st.error("Your plan exceeds your income.")
    elif remaining == 0:
        st.success("Your plan allocates all available income.")
    else:
        st.info("You have unallocated money.")

    st.subheader("🧠 Purchase decision")

    price = st.number_input(
        "Purchase price",
        min_value=0,
        value=6000,
        step=500,
        key="c3_new_l12_price",
    )

    available_money = st.number_input(
        "Money available after essentials and savings",
        min_value=0,
        value=5000,
        step=500,
        key="c3_new_l12_available",
    )

    gap = max(0, price - available_money)

    st.metric(
        "Amount you would need to find",
        money(gap),
    )

    if gap > 0:
        st.warning(
            "This purchase exceeds the available budget. "
            "Consider waiting, saving more or choosing "
            "a less expensive alternative."
        )
    else:
        st.success(
            "This purchase fits within the money you "
            "specified as available. Check that the "
            "budget is realistic."
        )

    st.subheader("🧠 Decision challenge")

    quiz(
        "Alex wants headphones costing ₹6,000. "
        "He has ₹5,000 available after his planned expenses. "
        "What is a reasonable approach?",
        [
            "Buy immediately using borrowed money",
            "Ignore his financial goals",
            "Wait, save more or reconsider the purchase",
            "Never buy anything enjoyable",
        ],
        "Wait, save more or reconsider the purchase",
        "The purchase exceeds his available budget by ₹1,000. "
        "Waiting or adjusting the purchase can help protect "
        "his financial plan. Enjoyment is not the problem; "
        "unplanned spending is.",
        "c3_new_quiz12",
    )

    st.subheader("⏳ The 24-hour rule")

    st.write("""
    For non-essential purchases, consider waiting 24 hours.

    For expensive purchases, consider waiting longer.

    During that time:
    - Compare prices.
    - Check your budget.
    - Think about the goal it might delay.
    - Consider alternatives.
    - Decide whether you still want it.

    This is a practical decision-making technique,
    not a guarantee.
    """)

    st.subheader("🏆 Final challenge — Alex's financial blueprint")

    final_income = 30000

    final_needs = st.slider(
        "Essential expenses",
        0,
        final_income,
        15000,
        step=500,
        key="c3_new_final_needs",
    )

    final_emergency = st.slider(
        "Emergency fund",
        0,
        final_income,
        3000,
        step=500,
        key="c3_new_final_emergency",
    )

    final_goal = st.slider(
        "Laptop goal",
        0,
        final_income,
        3000,
        step=500,
        key="c3_new_final_goal",
    )

    final_wants = st.slider(
        "Entertainment & wants",
        0,
        final_income,
        3000,
        step=500,
        key="c3_new_final_wants",
    )

    final_other = st.slider(
        "Other expenses",
        0,
        final_income,
        2000,
        step=500,
        key="c3_new_final_other",
    )

    final_total = (
        final_needs +
        final_emergency +
        final_goal +
        final_wants +
        final_other
    )

    final_remaining = final_income - final_total

    fig = go.Figure(
        go.Pie(
            labels=[
                "Needs",
                "Emergency",
                "Laptop",
                "Wants",
                "Other",
                "Remaining",
            ],
            values=[
                final_needs,
                final_emergency,
                final_goal,
                final_wants,
                final_other,
                max(0, final_remaining),
            ],
            hole=0.55,
        )
    )

    fig.update_layout(
        title="Alex's monthly blueprint",
        height=400,
    )

    st.plotly_chart(fig, use_container_width=True)

    st.metric(
        "Total allocated",
        money(final_total),
    )

    st.metric(
        "Remaining",
        money(final_remaining),
    )

    if final_remaining < 0:
        st.error(
            "Your blueprint exceeds ₹30,000. "
            "Adjust the allocations."
        )
    elif final_remaining == 0:
        st.success(
            "Every rupee has a purpose. "
            "Your plan balances."
        )
    else:
        st.info(
            "You still have money to assign. "
            "Consider another goal or future expense."
        )

    st.subheader("🎓 What you learned")

    st.markdown("""
    - Financial planning
    - Cash flow
    - Income and expenses
    - Emergency savings
    - Needs and wants
    - Budgeting
    - Goal planning
    - Spending decisions
    """)

    st.markdown("""
    <div class="c3-scene">
        <div class="c3-scene-emoji">🏆</div>
        <h2>Financial Foundation Complete</h2>
        <p>
        Good financial decisions are not about being perfect.
        They are about understanding your money and making
        deliberate choices consistently.
        </p>
    </div>
    """, unsafe_allow_html=True)

    st.write(
        "Next chapter: Understanding debt, interest, "
        "borrowing and repayment."
    )

    completion_button(12)


# ============================================================
# MAIN
# ============================================================

def show_chapter3():

    init_state()

    st.markdown(
        """
        <style>
        @keyframes c3float {
            0% { transform:translateY(0px); }
            50% { transform:translateY(-9px); }
            100% { transform:translateY(0px); }
        }

        @keyframes c3slide {
            from {opacity:0;transform:translateY(15px);}
            to {opacity:1;transform:translateY(0px);}
        }

        @keyframes c3glow {
            0% {opacity:.7;}
            50% {opacity:1;}
            100% {opacity:.7;}
        }

        .c3-hero {
            background:linear-gradient(135deg,#0f172a,#164e63,#134e4a);
            border:1px solid #286577;
            border-radius:25px;
            padding:28px 20px;
            text-align:center;
            animation:c3slide .6s ease;
        }

        .c3-hero h1 {
            color:white;
            font-size:30px;
        }

        .c3-hero p {
            color:#c7e6f5;
            font-size:17px;
        }

        .c3-hero-emoji {
            font-size:65px;
            animation:c3float 3s infinite;
        }

        .c3-scene {
            background:linear-gradient(135deg,#14263c,#1b3a57);
            border:1px solid #2d5675;
            border-radius:20px;
            padding:22px;
            margin:15px 0;
            animation:c3slide .5s ease;
        }

        .c3-scene h3,.c3-scene h2 {
            color:#e2f2ff;
        }

        .c3-scene p {
            color:#c4d9ea;
        }

        .c3-scene-emoji {
            font-size:55px;
            text-align:center;
            animation:c3float 4s infinite;
        }

        .c3-card {
            background:linear-gradient(135deg,#10243c,#17365a);
            border:1px solid #2b5279;
            border-radius:18px;
            padding:20px;
            margin:12px 0;
            animation:c3slide .5s ease;
        }

        .c3-card h4 {
            color:#a5f3fc;
        }

        .c3-card p {
            color:#d5e7f5;
        }

        .c3-flow {
            display:flex;
            flex-wrap:wrap;
            align-items:center;
            justify-content:center;
            gap:10px;
            margin:15px 0;
        }

        .c3-flow-item {
            min-width:100px;
            background:linear-gradient(135deg,#17365a,#10243c);
            border:1px solid #2b5279;
            border-radius:17px;
            padding:14px;
            text-align:center;
            color:#d8e8f5;
            animation:c3slide .7s ease;
        }

        .c3-flow-item div {
            font-size:35px;
            animation:c3glow 3s infinite;
        }

        .c3-arrow {
            font-size:25px;
            color:#34d399;
            font-weight:bold;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )

    st.title("💰 MoneyLab")

    st.caption(
        "Chapter 3 • Building Your Financial Foundation"
    )

    st.markdown(
        """
        <div class="c3-scene">
            <h2>🗺️ Your financial journey</h2>
            <p>
            You are learning to manage money in the real world.
            Make decisions, experiment with numbers and
            understand the consequences.
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    completed = st.session_state.c3_new_completed

    completed_count = len(completed)

    st.progress(completed_count / 4)

    st.caption(
        f"{completed_count}/4 lessons marked complete"
    )

    navigation()

    st.divider()

    current = st.session_state.c3_new_lesson

    if current == 0:
        show_lesson9()

    elif current == 1:
        show_lesson10()

    elif current == 2:
        show_lesson11()

    elif current == 3:
        show_lesson12()

    st.divider()

    st.markdown(
        """
        <div style="
            text-align:center;
            padding:15px;
            color:gray;
        ">
        MoneyLab • Learn Money by Living It
        </div>
        """,
        unsafe_allow_html=True,
    )
