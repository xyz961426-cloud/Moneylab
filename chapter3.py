import streamlit as st

def show_chapter3():
    st.title("🏦 Chapter 3: Building Your Financial Foundation")
    st.caption("MoneyLab • Lessons 9–12")

    st.markdown("""
    <style>
    .money-story {
        padding: 18px;
        border-radius: 15px;
        background: linear-gradient(135deg, #14213d, #243b55);
        color: white;
        margin: 12px 0;
    }
    .money-highlight {
        padding: 14px;
        border-radius: 12px;
        background: #e9f5ff;
        color: #102a43;
        margin: 10px 0;
    }
    .money-warning {
        padding: 14px;
        border-radius: 12px;
        background: #fff3cd;
        color: #5c4500;
        margin: 10px 0;
    }
    .money-success {
        padding: 14px;
        border-radius: 12px;
        background: #e6f4ea;
        color: #14532d;
        margin: 10px 0;
    }
    </style>
    """, unsafe_allow_html=True)

    lessons = {
        "Lesson 9 — Your First Financial Plan": 9,
        "Lesson 10 — Income, Expenses & Cash Flow": 10,
        "Lesson 11 — The Emergency Fund": 11,
        "Lesson 12 — Needs, Wants & Smart Spending": 12,
    }

    selected = st.selectbox(
        "📚 Chapter 3 lessons",
        list(lessons.keys())
    )

    lesson_number = lessons[selected]

    st.progress((lesson_number - 8) / 4)

    if lesson_number == 9:
        lesson9()
    elif lesson_number == 10:
        lesson10()
    elif lesson_number == 11:
        lesson11()
    elif lesson_number == 12:
        lesson12()


# =========================================================
# LESSON 9 — YOUR FIRST FINANCIAL PLAN
# =========================================================

def lesson9():
    st.header("🎯 Lesson 9: Your First Financial Plan")

    st.markdown("""
    <div class="money-story">
    <h3>Alex has a new problem...</h3>
    Alex has learned how money works, why investing involves risk,
    and how to make investment decisions.

    But he still has no plan for his own money.

    He wants a laptop, wants to save for the future, and wants to
    avoid financial problems. He doesn't know where to begin.

    <b>He needs a financial plan.</b>
    </div>
    """, unsafe_allow_html=True)

    st.subheader("1. What is a financial plan?")

    st.write("""
    A financial plan is a strategy for managing your money to achieve
    financial goals.

    It helps you decide:
    - What you want to achieve.
    - How much money you need.
    - When you need it.
    - How you will save or earn that money.
    - What you may need to change to reach your goal.
    """)

    st.markdown("""
    <div class="money-highlight">
    <b>A financial goal without a plan is just a wish.</b>
    </div>
    """, unsafe_allow_html=True)

    st.subheader("2. Alex's goals")

    st.write("""
    Alex has three goals. Each goal has a different time horizon.
    """)

    goals = [
        ("Short-term", "Buy headphones", "6 months"),
        ("Medium-term", "Buy a laptop", "2 years"),
        ("Long-term", "Build wealth for the future", "20 years"),
    ]

    for name, goal, duration in goals:
        with st.expander(f"🗓️ {name} goal — {goal}"):
            st.write(f"**Time horizon:** {duration}")
            if name == "Short-term":
                st.write("Short-term goals generally need money relatively soon. "
                         "Protecting the money from large losses may matter more than growth.")
            elif name == "Medium-term":
                st.write("Medium-term goals require balancing growth, risk and the deadline.")
            else:
                st.write("Long-term goals may allow more time for growth, but investment "
                         "risk still matters and returns are never guaranteed.")

    st.subheader("3. Make a goal measurable")

    st.write("""
    A useful financial goal has an amount and a deadline.
    """)

    target = st.number_input(
        "How much money do you need? (₹)",
        min_value=0,
        value=24000,
        step=1000,
        key="l9_target"
    )

    months = st.number_input(
        "How many months do you have?",
        min_value=1,
        value=12,
        step=1,
        key="l9_months"
    )

    monthly = target / months if months else 0

    st.metric("Monthly saving required", f"₹{monthly:,.2f}")

    st.write("""
    This calculation assumes you save the same amount each month and
    ignores interest, investment returns and unexpected changes.
    """)

    st.subheader("4. Build Alex's financial plan")

    st.write("Help Alex decide how much money to allocate.")

    income = st.number_input(
        "Alex's monthly income (₹)",
        min_value=0,
        value=30000,
        step=1000,
        key="l9_income"
    )

    essentials = st.number_input(
        "Essential expenses (₹)",
        min_value=0,
        value=12000,
        step=500,
        key="l9_essential"
    )

    savings = st.number_input(
        "Savings and goal money (₹)",
        min_value=0,
        value=5000,
        step=500,
        key="l9_savings"
    )

    other = st.number_input(
        "Other spending (₹)",
        min_value=0,
        value=4000,
        step=500,
        key="l9_other"
    )

    remaining = income - essentials - savings - other

    st.metric("Money remaining", f"₹{remaining:,.2f}")

    if remaining < 0:
        st.error("Alex has allocated more money than he earns.")
    elif remaining == 0:
        st.success("Every rupee is allocated. Alex has a balanced plan.")
    else:
        st.info("Alex has money left. He could review his priorities and decide how to allocate it.")

    st.subheader("5. What makes a financial plan useful?")

    st.markdown("""
    - **Realistic:** It matches your actual income.
    - **Specific:** It includes amounts and deadlines.
    - **Flexible:** It can change when circumstances change.
    - **Prioritized:** Essential expenses and financial safety matter.
    - **Reviewed:** It should be updated when life changes.
    """)

    quiz(
        "l9",
        [
            {
                "q": "Which is the most useful financial goal?",
                "options": [
                    "I want to become rich.",
                    "I want to save ₹24,000 within 12 months.",
                    "I want to spend less someday.",
                ],
                "correct": 1,
                "explanation": "The ₹24,000 goal has a specific amount and deadline. "
                              "It is measurable and can be turned into a monthly saving plan."
            },
            {
                "q": "Why can two people need different financial plans?",
                "options": [
                    "Everyone should follow the same plan.",
                    "Income, goals, responsibilities and circumstances differ.",
                    "Plans are only needed by wealthy people.",
                ],
                "correct": 1,
                "explanation": "Financial plans depend on personal circumstances, goals, "
                              "income, responsibilities and risk tolerance."
            },
            {
                "q": "What should Alex do if his financial circumstances change?",
                "options": [
                    "Never change the plan.",
                    "Review and adjust his plan.",
                    "Ignore the change.",
                ],
                "correct": 1,
                "explanation": "A financial plan should be flexible. New income, expenses, "
                              "responsibilities or goals may require adjustments."
            }
        ]
    )

    st.markdown("""
    <div class="money-success">
    <b>Lesson 9 connection:</b> Alex now has a plan, but he still needs to
    understand how money enters and leaves his account. That's our next lesson.
    </div>
    """, unsafe_allow_html=True)


# =========================================================
# LESSON 10 — INCOME, EXPENSES & CASH FLOW
# =========================================================

def lesson10():
    st.header("💸 Lesson 10: Income, Expenses & Cash Flow")

    st.markdown("""
    <div class="money-story">
    <h3>Alex's money disappears...</h3>
    Alex receives ₹30,000 every month.

    He believes he earns enough. But at the end of the month,
    he is surprised by how little money remains.

    He decides to investigate where his money goes.
    </div>
    """, unsafe_allow_html=True)

    st.subheader("1. Understanding income")

    st.write("""
    Income is money received.

    Common sources include:
    - Salary or wages.
    - Business income.
    - Freelancing.
    - Interest.
    - Dividends.
    - Rental income.

    Income is not the same as wealth. A person may earn a large income
    but still have little wealth if they spend everything or accumulate debt.
    """)

    st.subheader("2. Understanding expenses")

    st.write("""
    Expenses are money spent.

    **Fixed expenses:** Usually remain relatively stable for a period,
    such as rent or a regular subscription.

    **Variable expenses:** Change over time, such as groceries,
    electricity, transport or entertainment.

    Some expenses are essential, while others are discretionary.
    These categories can depend on a person's circumstances.
    """)

    st.subheader("3. Cash flow")

    st.write("""
    Cash flow describes the movement of money in and out over a period.

    **Cash flow = Money received − Money spent**

    Positive cash flow means more money came in than went out
    during that period.

    Negative cash flow means more money went out than came in.
    """)

    st.subheader("4. Alex's monthly budget simulator")

    income = st.number_input(
        "Monthly income (₹)",
        min_value=0,
        value=30000,
        step=1000,
        key="l10_income"
    )

    rent = st.number_input(
        "Housing (₹)",
        min_value=0,
        value=8000,
        step=500,
        key="l10_rent"
    )

    food = st.number_input(
        "Food (₹)",
        min_value=0,
        value=4000,
        step=500,
        key="l10_food"
    )

    transport = st.number_input(
        "Transport (₹)",
        min_value=0,
        value=2000,
        step=500,
        key="l10_transport"
    )

    bills = st.number_input(
        "Bills and utilities (₹)",
        min_value=0,
        value=2000,
        step=500,
        key="l10_bills"
    )

    shopping = st.number_input(
        "Shopping and entertainment (₹)",
        min_value=0,
        value=4000,
        step=500,
        key="l10_shopping"
    )

    other = st.number_input(
        "Other expenses (₹)",
        min_value=0,
        value=1000,
        step=500,
        key="l10_other"
    )

    total_expenses = rent + food + transport + bills + shopping + other
    cash_flow = income - total_expenses

    st.divider()

    st.metric("Total expenses", f"₹{total_expenses:,.2f}")
    st.metric("Monthly cash flow", f"₹{cash_flow:,.2f}")

    if cash_flow > 0:
        st.success(f"Alex has ₹{cash_flow:,.2f} remaining this month.")
    elif cash_flow == 0:
        st.info("Alex has used all of his income.")
    else:
        st.error(f"Alex has a shortfall of ₹{abs(cash_flow):,.2f}.")

    st.subheader("5. What if Alex earns more?")

    new_income = st.number_input(
        "Try a different income (₹)",
        min_value=0,
        value=40000,
        step=1000,
        key="l10_new_income"
    )

    new_flow = new_income - total_expenses

    st.metric("Cash flow at new income", f"₹{new_flow:,.2f}")

    st.write("""
    Higher income can improve cash flow, but only if spending doesn't
    increase by the same amount or more.
    """)

    st.subheader("6. Why tracking matters")

    st.write("""
    Tracking money can help identify:
    - Repeated unnecessary spending.
    - Expenses that are increasing.
    - Opportunities to save.
    - Whether goals are realistic.
    - Problems before they become serious.

    A budget isn't a punishment. It is a tool for making choices.
    """)

    quiz(
        "l10",
        [
            {
                "q": "Alex earns ₹25,000 and spends ₹22,000. What is his cash flow?",
                "options": ["₹3,000 positive", "₹3,000 negative", "₹47,000"],
                "correct": 0,
                "explanation": "₹25,000 − ₹22,000 = ₹3,000 positive cash flow."
            },
            {
                "q": "What does a higher income guarantee?",
                "options": [
                    "Higher wealth.",
                    "No financial problems.",
                    "Nothing by itself; spending and other factors matter."
                ],
                "correct": 2,
                "explanation": "Higher income alone doesn't guarantee wealth. "
                              "Expenses, saving, debt, investments and other factors matter."
            },
            {
                "q": "What is the purpose of tracking expenses?",
                "options": [
                    "To understand where money goes.",
                    "To stop all spending.",
                    "To make income unnecessary."
                ],
                "correct": 0,
                "explanation": "Tracking expenses helps understand spending patterns "
                              "and make informed financial decisions."
            }
        ]
    )

    st.markdown("""
    <div class="money-success">
    <b>Lesson 10 connection:</b> Alex understands his cash flow.
    But a surprise expense could still destroy his monthly plan.
    He needs protection. Next: emergency funds.
    </div>
    """, unsafe_allow_html=True)


# =========================================================
# LESSON 11 — THE EMERGENCY FUND
# =========================================================

def lesson11():
    st.header("🛡️ Lesson 11: The Emergency Fund")

    st.markdown("""
    <div class="money-story">
    <h3>An unexpected problem</h3>
    Alex has been managing his monthly money.

    One day, his phone breaks. Later, he faces an unexpected medical
    expense and a sudden travel need.

    These expenses were not part of his normal plan.

    <b>What should he do?</b>
    </div>
    """, unsafe_allow_html=True)

    st.subheader("1. What is an emergency fund?")

    st.write("""
    An emergency fund is money set aside for unexpected, necessary
    expenses or financial disruptions.

    Examples may include:
    - Unexpected medical costs.
    - Job loss or interruption of income.
    - Essential repairs.
    - Emergency travel.
    - Other urgent expenses.

    It is not generally intended for planned shopping, vacations
    or speculative investments.
    """)

    st.subheader("2. Why is it important?")

    st.write("""
    Without emergency savings, a sudden expense may force someone to:
    - Borrow money.
    - Use expensive credit.
    - Sell investments at an inconvenient time.
    - Delay necessary payments.

    Emergency savings can help reduce the need for these choices.
    """)

    st.subheader("3. How much could someone save?")

    st.write("""
    A common planning guideline is to build savings equal to several
    months of essential expenses. The appropriate amount depends on
    employment stability, responsibilities, health, insurance, access
    to support and other circumstances.

    The goal is not a universal fixed number.
    """)

    monthly_essential = st.number_input(
        "Essential monthly expenses (₹)",
        min_value=0,
        value=15000,
        step=1000,
        key="l11_essential"
    )

    months = st.slider(
        "Months of expenses to plan for",
        min_value=1,
        max_value=12,
        value=6,
        key="l11_months"
    )

    target = monthly_essential * months

    st.metric("Emergency fund target", f"₹{target:,.2f}")

    st.write("""
    This is a planning estimate. You may build toward it gradually.
    """)

    st.subheader("4. Build the fund gradually")

    current = st.number_input(
        "Current emergency savings (₹)",
        min_value=0,
        value=5000,
        step=1000,
        key="l11_current"
    )

    monthly_save = st.number_input(
        "Monthly contribution (₹)",
        min_value=0,
        value=3000,
        step=500,
        key="l11_contribution"
    )

    remaining = max(target - current, 0)

    st.metric("Amount still needed", f"₹{remaining:,.2f}")

    if remaining == 0:
        st.success("Alex has reached this target!")
    elif monthly_save > 0:
        needed_months = (remaining + monthly_save - 1) // monthly_save
        st.info(f"At this contribution, Alex would need approximately {needed_months} months.")
    else:
        st.warning("Enter a monthly contribution to estimate the time required.")

    st.subheader("5. Where should emergency money be kept?")

    st.write("""
    Emergency savings generally prioritize accessibility and preservation
    of money rather than high returns.

    Depending on the country, financial institution and circumstances,
    options may include:
    - Savings accounts.
    - Other suitable liquid, low-risk arrangements.

    Consider access, safety, applicable protections, fees and withdrawal
    restrictions. An investment that can lose substantial value may not
    be appropriate for money needed immediately.
    """)

    st.subheader("6. Emergency fund decision simulator")

    st.write("Alex has ₹20,000 in emergency savings.")

    event = st.selectbox(
        "Choose an unexpected event",
        [
            "Essential repair costing ₹5,000",
            "Unexpected bill costing ₹12,000",
            "Temporary loss of income",
            "Want to buy a new gaming console"
        ],
        key="l11_event"
    )

    if event == "Essential repair costing ₹5,000":
        st.success("An emergency fund may be appropriate for an essential unexpected repair.")
    elif event == "Unexpected bill costing ₹12,000":
        st.success("If the bill is necessary and unexpected, emergency savings may help.")
    elif event == "Temporary loss of income":
        st.info("Emergency savings can help cover essential expenses while income is interrupted.")
    else:
        st.warning("A gaming console is normally a planned purchase, not an emergency. "
                   "Consider saving separately for it.")

    quiz(
        "l11",
        [
            {
                "q": "What is the main purpose of an emergency fund?",
                "options": [
                    "To buy luxury items.",
                    "To help handle unexpected necessary expenses.",
                    "To speculate on stocks."
                ],
                "correct": 1,
                "explanation": "Emergency savings are intended to help manage unexpected "
                              "necessary expenses or disruptions."
            },
            {
                "q": "Why may emergency savings be kept in a liquid, low-risk place?",
                "options": [
                    "Because access and preservation matter.",
                    "Because it guarantees the highest return.",
                    "Because it cannot ever lose purchasing power."
                ],
                "correct": 0,
                "explanation": "Emergency money may be needed quickly. Accessibility and "
                              "preservation generally matter more than maximizing returns."
            },
            {
                "q": "Is six months of expenses a universal rule?",
                "options": [
                    "Yes, for every person.",
                    "No, it is a common guideline that depends on circumstances.",
                    "Emergency funds are unnecessary."
                ],
                "correct": 1,
                "explanation": "Several months of essential expenses is a common guideline, "
                              "but an appropriate target varies by personal circumstances."
            }
        ]
    )

    st.markdown("""
    <div class="money-success">
    <b>Lesson 11 connection:</b> Alex now has a financial safety net.
    He must also learn to make thoughtful spending decisions so he doesn't
    unnecessarily weaken that safety net.
    </div>
    """, unsafe_allow_html=True)


# =========================================================
# LESSON 12 — NEEDS, WANTS & SMART SPENDING
# =========================================================

def lesson12():
    st.header("🛒 Lesson 12: Needs, Wants & Smart Spending")

    st.markdown("""
    <div class="money-story">
    <h3>Alex enters a shopping store...</h3>
    Alex has money available.

    He sees shoes, a phone, food, headphones and several attractive offers.

    He wants everything. But he has limited money and financial goals.

    <b>He must choose.</b>
    </div>
    """, unsafe_allow_html=True)

    st.subheader("1. Needs vs wants")

    st.write("""
    **Needs:** Expenses required for basic living, responsibilities,
    safety or functioning. Examples can include food, basic housing,
    essential medicine and necessary transport.

    **Wants:** Purchases that improve enjoyment, comfort or convenience
    but are not currently essential.

    The distinction depends on circumstances. A phone may be a want for
    one person and essential for another person's work.
    """)

    st.subheader("2. The opportunity cost")

    st.write("""
    Opportunity cost is the value of the next-best alternative you give
    up when making a choice.

    If Alex spends ₹5,000 on headphones, he may no longer have that
    ₹5,000 available for a laptop, savings or another goal.

    Money spent has trade-offs.
    """)

    st.subheader("3. Impulse buying")

    st.write("""
    Impulse buying happens when someone purchases something without
    enough deliberate consideration.

    Common triggers:
    - Limited-time offers.
    - Social pressure.
    - Emotional stress.
    - Advertising.
    - FOMO.
    - Easy access to credit.

    A discount does not automatically make a purchase financially wise.
    """)

    st.subheader("4. The 24-hour decision technique")

    st.write("""
    For non-essential purchases, waiting before buying can help.

    Ask:
    - Do I actually need this?
    - Can I afford it without borrowing?
    - Does it fit my plan?
    - Would I buy it if there were no discount?
    - What am I giving up by purchasing it?
    """)

    st.subheader("5. Alex's shopping decision game")

    budget = st.number_input(
        "Alex's available spending budget (₹)",
        min_value=0,
        value=10000,
        step=1000,
        key="l12_budget"
    )

    items = {
        "Groceries": 2500,
        "Essential shoes": 2000,
        "Headphones": 3000,
        "Gaming accessory": 2500,
        "Movie night": 1000,
        "Laptop savings contribution": 4000,
    }

    st.write("Choose items Alex wants to allocate money toward.")

    selected_items = []

    for item, cost in items.items():
        if st.checkbox(f"{item} — ₹{cost:,}", key=f"l12_{item}"):
            selected_items.append((item, cost))

    total = sum(cost for _, cost in selected_items)

    st.metric("Total selected", f"₹{total:,.2f}")
    st.metric("Remaining budget", f"₹{budget - total:,.2f}")

    if total > budget:
        st.error("Alex has exceeded his budget.")
    else:
        st.success("Alex is within his budget.")

    if selected_items:
        st.write("**Alex's choices:**")
        for item, cost in selected_items:
            st.write(f"- {item}: ₹{cost:,}")

    st.subheader("6. Smart spending doesn't mean spending nothing")

    st.write("""
    Smart spending is about making purchases that fit your priorities,
    resources and goals.

    A sustainable plan may include enjoyment. The objective isn't to
    eliminate every want; it's to make deliberate choices and avoid
    sacrificing important goals unnecessarily.
    """)

    quiz(
        "l12",
        [
            {
                "q": "What is opportunity cost?",
                "options": [
                    "The value of the next-best alternative you give up.",
                    "The price of every item in a shop.",
                    "The money a bank lends."
                ],
                "correct": 0,
                "explanation": "Opportunity cost is the value of the next-best alternative "
                              "you give up when choosing one option."
            },
            {
                "q": "Does a 50% discount automatically mean a smart purchase?",
                "options": [
                    "Yes, every discount is worth buying.",
                    "No, it still depends on need, affordability and priorities.",
                    "Yes, even if you borrow to buy it."
                ],
                "correct": 1,
                "explanation": "A discount reduces the price but doesn't make an unnecessary "
                              "purchase valuable or affordable by itself."
            },
            {
                "q": "Which approach can help reduce impulse buying?",
                "options": [
                    "Buy immediately.",
                    "Use credit for every purchase.",
                    "Pause, review priorities and wait before non-essential purchases."
                ],
                "correct": 2,
                "explanation": "Pausing helps you consider affordability, goals and alternatives "
                              "before making a non-essential purchase."
            },
            {
                "q": "What does smart spending mean?",
                "options": [
                    "Never spending money on enjoyment.",
                    "Making deliberate purchases that fit your priorities.",
                    "Buying everything that is discounted."
                ],
                "correct": 1,
                "explanation": "Smart spending balances needs, wants, goals and available resources. "
                              "It doesn't require eliminating all enjoyment."
            }
        ]
    )

    st.markdown("""
    <div class="money-success">
    <h3>🎉 Chapter 3 completed!</h3>

    Alex has now learned to:

    - Create a financial plan.
    - Understand income and expenses.
    - Calculate cash flow.
    - Build an emergency fund.
    - Distinguish needs and wants.
    - Think about opportunity cost.
    - Make smarter spending decisions.

    <b>Next chapter: Chapter 4 — Understanding Debt.</b>
    </div>
    """, unsafe_allow_html=True)


# =========================================================
# REUSABLE QUIZ WITH EXPLANATIONS
# =========================================================

def quiz(quiz_id, questions):
    st.divider()
    st.header("🧠 Knowledge Check")

    answers = []

    for i, q in enumerate(questions):
        st.markdown(f"**Question {i + 1}: {q['q']}**")

        choice = st.radio(
            "Select your answer:",
            q["options"],
            key=f"{quiz_id}_q{i}",
            index=None
        )

        answers.append(choice)

    if st.button("Check my answers", key=f"{quiz_id}_check"):
        score = 0

        for i, q in enumerate(questions):
            chosen = answers[i]

            if chosen is None:
                st.warning(f"Question {i + 1}: Please select an answer.")
                continue

            selected_index = q["options"].index(chosen)

            if selected_index == q["correct"]:
                score += 1
                st.success(f"Question {i + 1}: Correct!")
            else:
                st.error(f"Question {i + 1}: Incorrect.")

            st.write(f"**Correct answer:** {q['options'][q['correct']]}")
            st.info(q["explanation"])

        st.markdown("---")
        st.subheader(f"Your score: {score}/{len(questions)}")

        if score == len(questions):
            st.success("Excellent! You understood all the concepts.")
        elif score >= len(questions) / 2:
            st.info("Good progress! Review the explanations for the questions you missed.")
        else:
            st.warning("Review this lesson and try again to strengthen your understanding.")
