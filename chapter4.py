import streamlit as st

def show_chapter4():
    st.title("💳 Chapter 4: Understanding Debt")
    st.caption("MoneyLab • Lessons 13–16")

    lessons = {
        "Lesson 13 — How Borrowing Really Works": 13,
        "Lesson 14 — Interest: The Cost of Borrowing": 14,
        "Lesson 15 — Credit Cards, Loans & EMI Traps": 15,
        "Lesson 16 — Managing & Escaping Debt": 16,
    }

    selected = st.selectbox("📚 Chapter 4", list(lessons.keys()))
    number = lessons[selected]

    st.progress((number - 12) / 4)

    if number == 13:
        lesson13()
    elif number == 14:
        lesson14()
    elif number == 15:
        lesson15()
    elif number == 16:
        lesson16()


# =========================================================
# LESSON 13 — HOW BORROWING REALLY WORKS
# =========================================================

def lesson13():
    st.header("🤝 Lesson 13: How Borrowing Really Works")

    st.markdown("""
    ### Alex wants to buy a laptop

    Alex wants a laptop worth ₹50,000. He has only ₹20,000.

    A lender offers to lend him the remaining ₹30,000.

    Alex can buy the laptop today, but he must repay the borrowed
    money according to the agreed terms.

    **Alex is now a borrower.**
    """)

    st.subheader("1. What is borrowing?")

    st.write("""
    Borrowing means receiving money or resources now with an obligation
    to repay according to an agreement.

    - **Borrower:** The person or organization receiving the loan.
    - **Lender:** The person or organization providing the loan.
    - **Principal:** The original amount borrowed.
    - **Interest:** The cost of borrowing, when charged.
    - **Term:** The period over which the loan is repaid.
    - **Repayment:** Returning the borrowed money and applicable costs.
    """)

    st.subheader("2. Why do people borrow?")

    st.write("""
    Borrowing can help people pay for expenses or purchases before
    they have enough money available.

    Common examples:
    - Education.
    - Housing.
    - Business.
    - Vehicles.
    - Emergencies.

    Borrowing can be useful, but it creates a future financial obligation.
    """)

    st.subheader("3. Secured vs unsecured loans")

    with st.expander("🏠 Secured loan"):
        st.write("""
        A secured loan is backed by collateral, such as a property or
        another asset, according to the loan agreement.

        If the borrower fails to meet obligations, the lender may have
        rights to the collateral under applicable law and contract terms.
        """)

    with st.expander("📝 Unsecured loan"):
        st.write("""
        An unsecured loan generally does not require specific collateral.

        Lenders may assess income, credit history, repayment capacity
        and other factors. Interest rates and eligibility vary.
        """)

    st.subheader("4. What does a lender consider?")

    st.write("""
    A lender may assess:
    - Income.
    - Existing debts.
    - Credit history.
    - Repayment ability.
    - Employment or business stability.
    - Collateral, where applicable.

    Lending decisions are not guarantees that the borrower can
    comfortably repay.
    """)

    st.subheader("5. Alex's borrowing decision")

    loan = st.number_input(
        "Amount Alex wants to borrow (₹)",
        min_value=0,
        value=30000,
        step=1000,
        key="l13_loan"
    )

    income = st.number_input(
        "Alex's monthly income (₹)",
        min_value=0,
        value=25000,
        step=1000,
        key="l13_income"
    )

    existing = st.number_input(
        "Existing monthly debt payments (₹)",
        min_value=0,
        value=4000,
        step=500,
        key="l13_existing"
    )

    proposed = st.number_input(
        "Proposed new monthly payment (₹)",
        min_value=0,
        value=3000,
        step=500,
        key="l13_proposed"
    )

    if income > 0:
        ratio = (existing + proposed) / income * 100
        st.metric("Debt payments relative to income", f"{ratio:.1f}%")
    else:
        ratio = 0
        st.warning("Enter income above zero to calculate.")

    st.write("""
    This is a simple comparison of monthly debt payments to income,
    not a universal affordability threshold. Actual affordability
    depends on essential expenses, income stability, other obligations
    and loan terms.
    """)

    decision = st.radio(
        "Should Alex borrow without reviewing his finances?",
        [
            "Borrow immediately because the lender approved it.",
            "Review the repayment terms and affordability first.",
            "Borrow the maximum amount available."
        ],
        index=None,
        key="l13_decision"
    )

    if decision:
        if decision == "Review the repayment terms and affordability first.":
            st.success("Good decision. Approval does not automatically mean affordability.")
        else:
            st.warning("Approval is not proof that the loan is affordable. "
                       "Alex should examine repayment, fees and financial risks.")

    st.subheader("6. What happens when a loan isn't repaid?")

    st.write("""
    Depending on the agreement and applicable law, missed payments may
    lead to fees, collection activity, credit-report consequences,
    legal proceedings or loss of collateral for a secured loan.

    The consequences depend on the type of debt, lender, agreement
    and local legal rules.
    """)

    debt_quiz(
        "l13",
        [
            {
                "q": "What is principal?",
                "options": [
                    "The original amount borrowed.",
                    "The borrower's monthly income.",
                    "A late-payment fee."
                ],
                "correct": 0,
                "explanation": "Principal is the original amount of money borrowed, "
                              "before interest and other costs."
            },
            {
                "q": "What makes a loan secured?",
                "options": [
                    "It has no repayment obligation.",
                    "It is backed by collateral under the agreement.",
                    "It always has zero interest."
                ],
                "correct": 1,
                "explanation": "A secured loan is backed by collateral. The lender may "
                              "have rights to that asset if obligations are not met."
            },
            {
                "q": "Does loan approval prove that a loan is affordable?",
                "options": [
                    "Yes, always.",
                    "No, the borrower must evaluate their own financial situation.",
                    "Yes, if the loan is advertised."
                ],
                "correct": 1,
                "explanation": "A lender's approval does not guarantee that repayment fits "
                              "the borrower's budget and responsibilities."
            }
        ]
    )

    st.info("Next: Why does borrowing money cost more than the amount borrowed?")


# =========================================================
# LESSON 14 — INTEREST
# =========================================================

def lesson14():
    st.header("📈 Lesson 14: Interest — The Cost of Borrowing")

    st.markdown("""
    ### Alex borrows ₹30,000

    Alex receives ₹30,000.

    But the lender doesn't necessarily expect only ₹30,000 back.

    The lender charges interest. Alex must understand how that cost
    changes with rates and time.
    """)

    st.subheader("1. What is interest?")

    st.write("""
    Interest is the cost of borrowing money, expressed in money
    or as a rate.

    If Alex borrows ₹10,000 and pays ₹1,000 in interest,
    his interest cost is ₹1,000, excluding other fees.
    """)

    st.subheader("2. Simple interest")

    st.write("""
    Simple interest is calculated on the original principal.

    **Simple interest = Principal × Rate × Time**

    For this calculation, time must be expressed in the appropriate
    units, such as years when the rate is annual.
    """)

    principal = st.number_input(
        "Principal (₹)",
        min_value=0,
        value=10000,
        step=1000,
        key="l14_simple_p"
    )

    rate = st.slider(
        "Annual simple interest rate (%)",
        min_value=0.0,
        max_value=50.0,
        value=10.0,
        step=0.5,
        key="l14_simple_rate"
    )

    years = st.slider(
        "Years",
        min_value=1,
        max_value=20,
        value=3,
        key="l14_simple_years"
    )

    simple_interest = principal * (rate / 100) * years
    simple_total = principal + simple_interest

    st.metric("Interest", f"₹{simple_interest:,.2f}")
    st.metric("Total repayment", f"₹{simple_total:,.2f}")

    st.subheader("3. Compound interest")

    st.write("""
    Compound interest is calculated on the principal and accumulated
    interest, when interest is compounded.

    The amount grows according to the compounding frequency and rate.
    """)

    cp = st.number_input(
        "Compound-interest principal (₹)",
        min_value=0,
        value=10000,
        step=1000,
        key="l14_compound_p"
    )

    cr = st.slider(
        "Annual rate (%)",
        min_value=0.0,
        max_value=50.0,
        value=10.0,
        step=0.5,
        key="l14_compound_rate"
    )

    cy = st.slider(
        "Years",
        min_value=1,
        max_value=20,
        value=3,
        key="l14_compound_years"
    )

    compound_total = cp * (1 + cr / 100) ** cy
    compound_interest = compound_total - cp

    st.metric("Compound interest", f"₹{compound_interest:,.2f}")
    st.metric("Total amount", f"₹{compound_total:,.2f}")

    st.write("""
    This simplified model assumes annual compounding and no payments
    during the period. Actual loans may use different calculations.
    """)

    st.subheader("4. Compare simple and compound interest")

    compare_p = 10000
    compare_rate = 10
    compare_years = 5

    si = compare_p * (compare_rate / 100) * compare_years
    ci = compare_p * ((1 + compare_rate / 100) ** compare_years - 1)

    st.write("Example: ₹10,000 at 10% for 5 years.")

    st.metric("Simple interest", f"₹{si:,.2f}")
    st.metric("Compound interest", f"₹{ci:,.2f}")

    st.write("""
    In this example, compound interest is higher because interest
    accumulates on previously accumulated interest.
    """)

    st.subheader("5. Why rate and time matter")

    st.write("""
    A higher rate generally increases borrowing costs.

    A longer repayment period may reduce each scheduled payment
    but can increase total interest, depending on the loan structure.

    Always compare the total repayment, fees and the actual terms,
    not only the monthly payment.
    """)

    debt_quiz(
        "l14",
        [
            {
                "q": "What is simple interest calculated on?",
                "options": [
                    "Only the original principal.",
                    "The accumulated interest only.",
                    "The borrower's income."
                ],
                "correct": 0,
                "explanation": "Simple interest is calculated on the original principal "
                              "under the simple-interest formula."
            },
            {
                "q": "Why can compound interest increase the cost?",
                "options": [
                    "Interest can accumulate on previously accumulated interest.",
                    "The loan principal automatically disappears.",
                    "The interest rate must always be zero."
                ],
                "correct": 0,
                "explanation": "Compound interest adds interest to the balance, so future "
                              "interest can be calculated on a larger amount."
            },
            {
                "q": "What should a borrower compare?",
                "options": [
                    "Only the advertised monthly payment.",
                    "Only the lender's logo.",
                    "Rate, fees, total repayment and loan terms."
                ],
                "correct": 2,
                "explanation": "The full cost and repayment terms matter. A small payment "
                              "may hide a long repayment period or other costs."
            }
        ]
    )

    st.info("Next: How do credit cards and EMIs turn borrowing into everyday spending?")


# =========================================================
# LESSON 15 — CREDIT CARDS, LOANS & EMI
# =========================================================

def lesson15():
    st.header("💳 Lesson 15: Credit Cards, Loans & EMI Traps")

    st.markdown("""
    ### Alex gets a credit card

    Alex is offered a credit card with a ₹50,000 limit.

    He thinks the limit means he has ₹50,000 of extra money.

    **It doesn't.**

    A credit limit is the maximum amount the issuer allows him
    to borrow under the card's terms.
    """)

    st.subheader("1. How credit cards work")

    st.write("""
    A credit card allows the cardholder to borrow for purchases
    under the issuer's terms.

    - Purchases create a balance owed.
    - A statement summarizes charges and payments.
    - A due date specifies when payment is required.
    - Paying the full statement balance on time may avoid interest
      on eligible purchases, subject to the card terms.
    - Carrying a balance may lead to interest and other charges.
    """)

    st.subheader("2. The minimum payment trap")

    st.write("""
    The minimum payment is the smallest amount the issuer requires
    by the due date to avoid being treated as a missed payment
    under the terms.

    Paying only the minimum can leave a large balance outstanding.
    Interest and the repayment duration may increase substantially.
    """)

    balance = st.number_input(
        "Credit card balance (₹)",
        min_value=0,
        value=30000,
        step=1000,
        key="l15_balance"
    )

    monthly_rate = st.slider(
        "Illustrative monthly interest rate (%)",
        min_value=0.0,
        max_value=5.0,
        value=3.0,
        step=0.1,
        key="l15_rate"
    )

    payment = st.number_input(
        "Monthly payment (₹)",
        min_value=0,
        value=1500,
        step=100,
        key="l15_payment"
    )

    monthly_interest = balance * monthly_rate / 100

    st.metric("Illustrative monthly interest", f"₹{monthly_interest:,.2f}")

    if payment <= monthly_interest and balance > 0:
        st.warning("This payment does not exceed the calculated monthly interest. "
                   "The balance may not decline under this simplified calculation.")
    elif payment > monthly_interest and balance > 0:
        st.info(f"About ₹{payment - monthly_interest:,.2f} of this payment "
                "would go toward reducing the balance in this simplified example.")
    elif balance == 0:
        st.success("No balance.")
    else:
        st.info("Enter a payment to compare it with interest.")

    st.caption("Illustration only. Actual card interest calculations, fees and payments vary.")

    st.subheader("3. What is EMI?")

    st.write("""
    EMI stands for Equated Monthly Installment.

    It is a scheduled monthly payment used in many loans. It typically
    includes principal and interest.

    A fixed-rate amortizing loan generally has a calculated payment
    that stays the same during the agreed period, assuming terms
    remain unchanged.
    """)

    loan = st.number_input(
        "Loan amount (₹)",
        min_value=0,
        value=50000,
        step=5000,
        key="l15_emi_loan"
    )

    annual = st.slider(
        "Annual interest rate (%)",
        min_value=0.0,
        max_value=40.0,
        value=12.0,
        step=0.5,
        key="l15_emi_rate"
    )

    duration = st.slider(
        "Loan duration (months)",
        min_value=1,
        max_value=120,
        value=24,
        key="l15_emi_duration"
    )

    monthly_rate = annual / 12 / 100

    if loan == 0:
        emi = 0
    elif monthly_rate == 0:
        emi = loan / duration
    else:
        emi = (
            loan * monthly_rate * (1 + monthly_rate) ** duration
            / ((1 + monthly_rate) ** duration - 1)
        )

    total_payment = emi * duration
    total_interest = total_payment - loan

    st.metric("Estimated monthly EMI", f"₹{emi:,.2f}")
    st.metric("Total repayment", f"₹{total_payment:,.2f}")
    st.metric("Total interest", f"₹{total_interest:,.2f}")

    st.write("""
    This is an illustrative amortizing-loan calculation that excludes
    additional fees and assumes the stated rate and duration.
    """)

    st.subheader("4. EMI decision")

    st.write("""
    A low EMI may look affordable, but consider:

    - Total repayment.
    - Loan duration.
    - Interest rate.
    - Fees.
    - Whether income is stable.
    - Other debt obligations.
    - Whether the purchase is necessary.
    """)

    st.subheader("5. Buy Now, Pay Later")

    st.write("""
    Buy Now, Pay Later (BNPL) products allow customers to purchase
    now and pay later, often through scheduled installments.

    Depending on the provider and product, missed payments,
    fees, credit reporting and other consequences may apply.

    Read the terms before using one.
    """)

    st.subheader("6. Alex's purchase decision")

    decision = st.radio(
        "Alex wants a ₹40,000 phone. Which choice is more thoughtful?",
        [
            "Take any EMI because the monthly payment looks small.",
            "Compare total costs and check whether the payment fits his plan.",
            "Use multiple loans to avoid paying today."
        ],
        index=None,
        key="l15_decision"
    )

    if decision:
        if decision == "Compare total costs and check whether the payment fits his plan.":
            st.success("Correct approach. Alex should compare costs and affordability.")
        else:
            st.warning("Small payments can hide high total costs or multiple obligations. "
                       "Alex should evaluate the full terms.")

    debt_quiz(
        "l15",
        [
            {
                "q": "What is a credit limit?",
                "options": [
                    "Free money.",
                    "The maximum borrowing amount allowed under the card's terms.",
                    "A guaranteed income."
                ],
                "correct": 1,
                "explanation": "A credit limit is a borrowing limit, not free money or income."
            },
            {
                "q": "Why can minimum card payments be risky?",
                "options": [
                    "They always clear the entire balance.",
                    "They may leave a large balance and interest accumulating.",
                    "They eliminate fees."
                ],
                "correct": 1,
                "explanation": "Minimum payments may only cover part of the balance. "
                              "Remaining balances may incur interest and take longer to repay."
            },
            {
                "q": "What does EMI usually include?",
                "options": [
                    "Principal and interest.",
                    "Only the original principal in every loan.",
                    "Only a fee."
                ],
                "correct": 0,
                "explanation": "EMIs in many amortizing loans include both principal repayment "
                              "and interest."
            }
        ]
    )

    st.info("Next: If Alex already has debt, how can he systematically repay it?")


# =========================================================
# LESSON 16 — MANAGING & ESCAPING DEBT
# =========================================================

def lesson16():
    st.header("🧭 Lesson 16: Managing & Escaping Debt")

    st.markdown("""
    ### Alex has three debts

    Alex has:
    - A credit card balance.
    - A personal loan.
    - A small borrowed amount from a friend.

    He is confused about which one to repay first.

    He needs a strategy.
    """)

    st.subheader("1. Know your debt")

    st.write("""
    Before creating a repayment plan, list each debt.

    Include:
    - Outstanding balance.
    - Interest rate.
    - Minimum payment.
    - Due date.
    - Fees.
    - Any special repayment terms.
    """)

    st.subheader("2. Debt avalanche")

    st.write("""
    The debt avalanche method prioritizes the debt with the highest
    interest rate while continuing required payments on other debts.

    When the highest-rate debt is paid, the extra repayment is
    redirected to the next highest-rate debt.

    This approach can reduce interest costs compared with strategies
    that prioritize lower-rate debts, depending on the balances,
    rates, fees and payment structure.
    """)

    st.subheader("3. Debt snowball")

    st.write("""
    The debt snowball method prioritizes the smallest outstanding
    balance while continuing required payments on other debts.

    Paying off smaller debts first may provide visible progress
    and motivation, though it may cost more interest than the avalanche.
    """)

    st.subheader("4. Compare repayment strategies")

    st.write("Enter Alex's debts.")

    debt_names = ["Credit Card", "Personal Loan", "Friend"]

    debts = []

    for i, name in enumerate(debt_names):
        with st.expander(name, expanded=True):
            amount = st.number_input(
                f"{name} balance (₹)",
                min_value=0,
                value=[15000, 40000, 5000][i],
                step=1000,
                key=f"l16_balance_{i}"
            )

            interest = st.number_input(
                f"{name} annual rate (%)",
                min_value=0.0,
                max_value=100.0,
                value=[36.0, 14.0, 0.0][i],
                step=0.5,
                key=f"l16_interest_{i}"
            )

            minimum = st.number_input(
                f"{name} minimum payment (₹)",
                min_value=0,
                value=[1000, 2000, 500][i],
                step=100,
                key=f"l16_minimum_{i}"
            )

            debts.append({
                "name": name,
                "balance": amount,
                "rate": interest,
                "minimum": minimum,
            })

    extra = st.number_input(
        "Extra money available each month for debt repayment (₹)",
        min_value=0,
        value=3000,
        step=500,
        key="l16_extra"
    )

    total_minimum = sum(d["minimum"] for d in debts)
    total_balance = sum(d["balance"] for d in debts)

    st.metric("Total debt", f"₹{total_balance:,.2f}")
    st.metric("Total listed minimum payments", f"₹{total_minimum:,.2f}")

    if extra > 0:
        st.metric("Extra repayment available", f"₹{extra:,.2f}")

    st.subheader("5. Which strategy would Alex use?")

    strategy = st.radio(
        "Choose a repayment strategy",
        [
            "Debt Avalanche — highest interest first",
            "Debt Snowball — smallest balance first"
        ],
        index=None,
        key="l16_strategy"
    )

    if strategy:
        if strategy.startswith("Debt Avalanche"):
            ordered = sorted(debts, key=lambda d: d["rate"], reverse=True)
            st.write("**Priority order (highest listed interest rate first):**")
        else:
            ordered = sorted(debts, key=lambda d: d["balance"])
            st.write("**Priority order (smallest listed balance first):**")

        for d in ordered:
            st.write(f"- {d['name']}: ₹{d['balance']:,.2f} — {d['rate']:.1f}%")

        if strategy.startswith("Debt Avalanche"):
            st.info("The avalanche prioritizes high-rate debt and may reduce interest cost.")
        else:
            st.info("The snowball prioritizes smaller balances and may help motivation.")

    st.subheader("6. What should Alex do first?")

    st.write("""
    - Avoid missing required payments where possible.
    - Stop or reduce unnecessary new borrowing.
    - Prioritize debts based on rates, consequences and circumstances.
    - Contact creditors early if payments are becoming difficult.
    - Review fees and contractual terms.
    - Consider reputable professional assistance when debt is overwhelming.

    Depending on the circumstances, some obligations may need special
    priority due to legal consequences or essential services.
    """)

    st.subheader("7. Alex's debt crisis")

    situation = st.selectbox(
        "Alex cannot afford all his debt payments this month. What should he do?",
        [
            "Ignore the lenders.",
            "Borrow from another expensive lender without checking terms.",
            "Review his budget, contact lenders and seek trustworthy help."
        ],
        key="l16_crisis"
    )

    if situation == "Review his budget, contact lenders and seek trustworthy help.":
        st.success("A thoughtful response. Early communication and a realistic plan can help.")
    elif situation:
        st.warning("Ignoring payments or taking expensive new debt may worsen the problem. "
                   "Alex should assess his options early.")

    debt_quiz(
        "l16",
        [
            {
                "q": "How does the debt avalanche prioritize repayment?",
                "options": [
                    "Highest interest rate first.",
                    "Smallest balance first.",
                    "Newest debt first."
                ],
                "correct": 0,
                "explanation": "The avalanche prioritizes the highest interest rate "
                              "while required payments continue on other debts."
            },
            {
                "q": "How does the debt snowball prioritize repayment?",
                "options": [
                    "Highest interest rate first.",
                    "Smallest balance first.",
                    "Largest payment first."
                ],
                "correct": 1,
                "explanation": "The snowball prioritizes the smallest balance, which can "
                              "provide visible progress and motivation."
            },
            {
                "q": "What should someone do if they cannot afford debt payments?",
                "options": [
                    "Ignore all lenders.",
                    "Take expensive new debt automatically.",
                    "Review their finances, contact creditors and consider reliable assistance."
                ],
                "correct": 2,
                "explanation": "Early communication, reviewing the budget and exploring "
                              "reliable assistance may help prevent the situation worsening."
            },
            {
                "q": "Which method is always best for every borrower?",
                "options": [
                    "Avalanche for everyone.",
                    "Snowball for everyone.",
                    "Neither is universally best; circumstances and motivation matter."
                ],
                "correct": 2,
                "explanation": "Avalanche and snowball have different trade-offs. "
                              "The best strategy depends on the debt, rates, circumstances and behavior."
            }
        ]
    )

    st.markdown("""
    ### 🎉 Chapter 4 completed!

    Alex now understands:

    - How borrowing works.
    - Secured and unsecured debt.
    - Interest and compound interest.
    - Credit cards and minimum payments.
    - EMI calculations.
    - Debt avalanche.
    - Debt snowball.
    - Practical debt management.

    **Next: Chapter 5 — The Investing World.**
    """)


# =========================================================
# REUSABLE QUIZ
# =========================================================

def debt_quiz(quiz_id, questions):
    st.divider()
    st.header("🧠 Knowledge Check")

    answers = []

    for i, q in enumerate(questions):
        st.markdown(f"**Question {i + 1}: {q['q']}**")

        choice = st.radio(
            "Choose your answer:",
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

        st.divider()
        st.subheader(f"Your score: {score}/{len(questions)}")

        if score == len(questions):
            st.success("Excellent! You understood the concepts.")
        elif score >= len(questions) / 2:
            st.info("Good progress. Review the explanations for the questions you missed.")
        else:
            st.warning("Review this lesson and try again to strengthen your understanding.")
