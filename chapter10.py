
import streamlit as st
import plotly.graph_objects as go


def tax_quiz(key, question, options, correct, explanation):
    choice = st.radio(question, options, key=key)

    if st.button("Check Answer", key=key + "_btn"):
        if choice == correct:
            st.success("Correct! " + explanation)
        else:
            st.error(f"Incorrect. Correct answer: {correct}")
            st.info(explanation)


def show_chapter10():
    st.title("🏛️ Chapter 10: Taxes & Personal Finance")
    st.caption("MoneyLab • Lessons 37–40")

    st.markdown("""
    ### Alex's next challenge

    Alex has started understanding saving, investing, banking and
    building wealth. But there is one important thing he still doesn't
    fully understand:

    **Why does the government take a portion of people's income,
    and how can people understand and manage their taxes?**
    """)

    lesson = st.selectbox(
        "Choose your lesson",
        [
            "Lesson 37 — Why Governments Collect Taxes",
            "Lesson 38 — Understanding Income Tax",
            "Lesson 39 — The Real Cost of Taxes",
            "Lesson 40 — Tax Planning & Smart Decisions"
        ]
    )

    # LESSON 37
    if lesson.startswith("Lesson 37"):
        st.header("🌍 Why Governments Collect Taxes")

        st.markdown("""
        Alex walks through his city and notices roads, hospitals,
        schools, public transport and emergency services.

        He asks:

        *"Who pays for all these services?"*

        Many of these services are financed partly through taxes.

        ### What is a tax?

        A tax is a compulsory payment imposed by a government
        under its legal authority to finance public expenditure
        and other government functions.
        """)

        st.subheader("Where can government money go?")

        categories = [
            "Healthcare",
            "Education",
            "Infrastructure",
            "Defence",
            "Social Programs"
        ]

        values = [20, 20, 25, 15, 20]

        fig = go.Figure(
            go.Pie(
                labels=categories,
                values=values,
                hole=0.45
            )
        )

        fig.update_layout(
            title="Illustrative government spending allocation"
        )

        st.plotly_chart(fig, use_container_width=True)

        st.caption(
            "Illustration only. This is not an actual government "
            "budget or allocation."
        )

        st.subheader("Different types of taxes")

        st.markdown("""
        - **Income tax:** Tax on qualifying income.
        - **Consumption taxes:** Taxes on purchases of goods or services,
          such as GST in India.
        - **Corporate taxes:** Taxes on qualifying corporate profits.
        - **Property taxes:** Taxes on certain property ownership,
          depending on jurisdiction.
        - **Capital gains taxes:** Taxes on qualifying profits from
          the sale of investments or assets.
        """)

        st.info(
            "Taxes are not all calculated in the same way. "
            "Different taxes have different rules, rates and exemptions."
        )

        tax_quiz(
            "q37",
            "Why do governments collect taxes?",
            [
                "To fund public services and government functions",
                "To guarantee profits for businesses",
                "To eliminate all personal expenses",
                "To make every citizen equally wealthy"
            ],
            "To fund public services and government functions",
            "Taxes help finance public services, infrastructure and "
            "other government responsibilities."
        )

    # LESSON 38
    elif lesson.startswith("Lesson 38"):
        st.header("💰 Understanding Income Tax")

        st.markdown("""
        Alex gets a job and earns money. He assumes that if he earns
        ₹10 lakh, he will necessarily pay the same tax rate on all
        ₹10 lakh.

        But many tax systems use **progressive tax brackets**.

        In a progressive tax system, different portions of income
        can be taxed at different rates.

        ### Example of a fictional tax system

        | Taxable income portion | Rate |
        |---|---:|
        | ₹0–₹3 lakh | 0% |
        | ₹3–₹6 lakh | 5% |
        | ₹6–₹10 lakh | 10% |
        | Above ₹10 lakh | 20% |

        These rates are fictional and are used only to explain
        marginal taxation.
        """)

        income = st.slider(
            "Alex's annual taxable income (₹)",
            min_value=0,
            max_value=2000000,
            step=50000,
            value=1200000
        )

        def calculate_tax(income):
            tax = 0

            tax += min(income, 300000) * 0

            tax += max(
                min(income, 600000) - 300000,
                0
            ) * 0.05

            tax += max(
                min(income, 1000000) - 600000,
                0
            ) * 0.10

            tax += max(
                income - 1000000,
                0
            ) * 0.20

            return tax

        tax = calculate_tax(income)
        net = income - tax

        col1, col2, col3 = st.columns(3)

        col1.metric("Taxable income", f"₹{income:,.0f}")
        col2.metric("Illustrative tax", f"₹{tax:,.0f}")
        col3.metric("After this tax", f"₹{net:,.0f}")

        st.subheader("How the tax is calculated")

        brackets = [
            ("First ₹3 lakh", min(income, 300000), 0),
            (
                "₹3–6 lakh",
                max(min(income, 600000) - 300000, 0),
                0.05
            ),
            (
                "₹6–10 lakh",
                max(min(income, 1000000) - 600000, 0),
                0.10
            ),
            (
                "Above ₹10 lakh",
                max(income - 1000000, 0),
                0.20
            )
        ]

        for name, amount, rate in brackets:
            st.write(
                f"**{name}:** ₹{amount:,.0f} "
                f"× {rate*100:.0f}% = ₹{amount*rate:,.0f}"
            )

        st.markdown("""
        ### Marginal tax rate vs effective tax rate

        - **Marginal rate:** The rate applied to the next unit
          of taxable income within the relevant bracket.
        - **Effective rate:** Total tax divided by total taxable income
          in this simplified example.
        """)

        effective = (tax / income * 100) if income > 0 else 0

        st.metric(
            "Illustrative effective tax rate",
            f"{effective:.2f}%"
        )

        st.info(
            "Moving into a higher tax bracket generally does not mean "
            "all your income is taxed at that higher rate in a "
            "progressive marginal system."
        )

        tax_quiz(
            "q38",
            "In this fictional progressive tax system, "
            "what happens when income enters the 20% bracket?",
            [
                "All income is automatically taxed at 20%",
                "Only the portion in that bracket is taxed at 20%",
                "Tax becomes zero",
                "The previous brackets are ignored"
            ],
            "Only the portion in that bracket is taxed at 20%",
            "In a marginal system, each portion is taxed according "
            "to its applicable bracket."
        )

    # LESSON 39
    elif lesson.startswith("Lesson 39"):
        st.header("📊 The Real Cost of Taxes")

        st.markdown("""
        Alex receives a job offer.

        His employer tells him that his salary is ₹12 lakh a year.

        Alex thinks he will receive ₹1 lakh every month.

        But gross salary and take-home pay can be different.

        Other deductions may include income tax, provident fund,
        insurance or other payroll deductions depending on the job,
        jurisdiction and applicable rules.
        """)

        st.subheader("Salary calculator")

        salary = st.slider(
            "Annual gross salary (₹)",
            min_value=100000,
            max_value=5000000,
            step=100000,
            value=1200000
        )

        annual_tax = st.slider(
            "Estimated annual income tax (₹)",
            min_value=0,
            max_value=1000000,
            step=10000,
            value=100000
        )

        other_deductions = st.slider(
            "Other annual deductions (₹)",
            min_value=0,
            max_value=500000,
            step=10000,
            value=60000
        )

        takehome = salary - annual_tax - other_deductions

        if takehome < 0:
            st.warning(
                "The deductions entered exceed the gross salary."
            )
        else:
            monthly = takehome / 12

            col1, col2 = st.columns(2)

            col1.metric(
                "Annual take-home",
                f"₹{takehome:,.0f}"
            )

            col2.metric(
                "Monthly take-home",
                f"₹{monthly:,.0f}"
            )

            fig = go.Figure(
                go.Bar(
                    x=["Gross Salary", "Tax", "Other Deductions", "Take-home"],
                    y=[
                        salary,
                        annual_tax,
                        other_deductions,
                        takehome
                    ]
                )
            )

            fig.update_layout(
                title="Illustrative salary breakdown",
                yaxis_title="Amount (₹)"
            )

            st.plotly_chart(
                fig,
                use_container_width=True
            )

        st.markdown("""
        ### Why take-home pay matters

        Financial decisions should be based on the money you can
        realistically use, not just the headline salary.

        Your monthly budget, rent, savings, debt payments and
        investments should be planned around actual cash flow.

        ### Gross salary vs net salary

        - **Gross salary:** Salary before applicable deductions.
        - **Net salary:** Amount received after relevant deductions.
        - **Cash flow:** Money coming in and going out over time.
        """)

        tax_quiz(
            "q39",
            "Which figure is generally most useful when planning "
            "your monthly spending?",
            [
                "Gross salary alone",
                "Net take-home income",
                "The company's revenue",
                "The highest possible salary"
            ],
            "Net take-home income",
            "Net income is closer to the amount available for "
            "spending, saving and investing."
        )

    # LESSON 40
    elif lesson.startswith("Lesson 40"):
        st.header("🧠 Tax Planning & Smart Decisions")

        st.markdown("""
        Alex learns that tax planning isn't about hiding income
        or making dishonest claims.

        **Legal tax planning** means understanding the rules,
        organising your financial records and making informed
        decisions that comply with the law.

        ### Alex's tax-smart habits

        1. Keep income records.
        2. Save receipts and relevant financial documents.
        3. Understand deductions and exemptions.
        4. Check the applicable tax regime.
        5. Plan investments with taxes in mind.
        6. Avoid false claims and tax evasion.
        """)

        st.subheader("Tax planning scenario")

        st.markdown("""
        Alex has two choices:

        - Option A: Make a financial decision only because
          he thinks it will reduce tax.
        - Option B: Compare the total financial benefit,
          risks, fees, liquidity and tax consequences before deciding.
        """)

        st.success(
            "Option B is the better decision-making process. "
            "Tax savings alone do not make a financial decision worthwhile."
        )

        st.subheader("Illustrative tax-saving comparison")

        investment = st.slider(
            "Illustrative eligible deduction (₹)",
            min_value=0,
            max_value=200000,
            step=10000,
            value=100000
        )

        marginal_rate = st.slider(
            "Assumed marginal tax rate (%)",
            min_value=0,
            max_value=40,
            step=1,
            value=20
        )

        potential_saving = investment * marginal_rate / 100

        st.metric(
            "Illustrative tax reduction",
            f"₹{potential_saving:,.0f}"
        )

        st.caption(
            "Simplified example assuming the entire amount is eligible "
            "for deduction and tax reduction at the selected rate. "
            "Real tax treatment depends on laws, eligibility, limits, "
            "tax regime and other factors. This is not actual tax advice."
        )

        st.markdown("""
        ### Tax evasion vs legal tax planning

        | Legal tax planning | Tax evasion |
        |---|---|
        | Uses lawful deductions | Conceals income |
        | Maintains accurate records | Uses false documents |
        | Complies with tax rules | Deliberately violates tax law |
        | Makes informed decisions | Attempts illegal avoidance of tax obligations |

        ### Alex's final lesson

        Understanding taxes helps you make better financial decisions.

        It doesn't mean every tax-saving opportunity is good.
        A financial decision should make sense even after considering
        its costs, risks and restrictions.
        """)

        tax_quiz(
            "q40",
            "Which is an example of responsible tax planning?",
            [
                "Hiding income",
                "Creating fake receipts",
                "Keeping records and using eligible legal deductions",
                "Ignoring tax laws"
            ],
            "Keeping records and using eligible legal deductions",
            "Responsible tax planning follows the law, uses accurate "
            "records and claims only eligible deductions."
        )

    st.divider()

    st.markdown("""
    ### 🏆 Chapter 10 Complete

    Alex now understands why taxes exist, how marginal tax brackets
    work, the difference between gross and net salary, and how
    responsible tax planning supports financial decisions.

    **Next chapter: Financial Markets & Trading**
    """)
