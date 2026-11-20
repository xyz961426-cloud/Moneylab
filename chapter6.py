
import streamlit as st
import plotly.graph_objects as go


def bond_quiz(key, questions):
    if key not in st.session_state:
        st.session_state[key] = {}

    for i, q in enumerate(questions):
        st.markdown(f"### Question {i+1}")
        st.write(q["question"])

        choice = st.radio(
            "Choose your answer:",
            q["options"],
            key=f"{key}_q{i}",
            index=None
        )

        if st.button("Check Answer", key=f"{key}_check{i}"):
            st.session_state[key][i] = choice

        if i in st.session_state[key]:
            answer = st.session_state[key][i]

            if answer == q["answer"]:
                st.success("Correct! " + q["explanation"])
            else:
                st.error(f"Not quite. Your answer: {answer}")
                st.info(
                    f"Correct answer: {q['answer']}\n\n"
                    f"Explanation: {q['explanation']}"
                )


def show_chapter6():

    st.title("🏦 Chapter 6: The World of Bonds")
    st.caption("MoneyLab • Learn Money by Living It")

    st.markdown("""
    <div style="padding:18px;border-radius:12px;background:#153448;color:white;">
    <h3>Alex's New Investment Journey</h3>
    <p>
    Alex has already learned about stocks. But one day, Alex discovers
    that investors can also lend money to governments and companies.
    </p>
    <p>
    Instead of becoming an owner, Alex can become a lender.
    This introduces a completely new investment world: bonds.
    </p>
    </div>
    """, unsafe_allow_html=True)

    lesson = st.selectbox(
        "Choose your lesson",
        [
            "Lesson 21 — What Is a Bond?",
            "Lesson 22 — How Bond Interest Works",
            "Lesson 23 — Why Bond Prices Change",
            "Lesson 24 — Bond Risks & Types"
        ]
    )

    # -------------------------------------------------
    # LESSON 21
    # -------------------------------------------------

    if lesson == "Lesson 21 — What Is a Bond?":

        st.header("📘 Lesson 21 — What Is a Bond?")

        st.markdown("""
        ### The story

        A company wants to build a new factory. It needs ₹10 crore.

        Instead of borrowing the entire amount from one bank,
        the company can raise money from many investors.

        The company issues bonds.

        When Alex buys a bond, Alex lends money to the company.

        In return, the company promises to:

        - Pay interest according to the bond terms.
        - Repay the principal according to the bond terms,
          assuming it does not default.
        """)

        st.markdown("### 🏗️ How a bond works")

        st.markdown("""
        <div style="display:flex;justify-content:center;
        align-items:center;gap:12px;flex-wrap:wrap;
        padding:20px;background:#102B3F;border-radius:15px;
        color:white;text-align:center;">

        <div style="padding:15px;background:#235789;border-radius:10px;">
        <h3>👤 Alex</h3>
        <p>Lends money</p>
        </div>

        <div style="font-size:25px;">➡️ 💰 ➡️</div>

        <div style="padding:15px;background:#238636;border-radius:10px;">
        <h3>🏢 Company</h3>
        <p>Receives money</p>
        </div>

        </div>
        """, unsafe_allow_html=True)

        st.markdown("""
        <div style="display:flex;justify-content:center;
        align-items:center;gap:12px;flex-wrap:wrap;
        padding:20px;background:#102B3F;border-radius:15px;
        color:white;text-align:center;margin-top:10px;">

        <div style="padding:15px;background:#238636;border-radius:10px;">
        <h3>🏢 Company</h3>
        <p>Interest + repayment</p>
        </div>

        <div style="font-size:25px;">➡️ 💰 ➡️</div>

        <div style="padding:15px;background:#235789;border-radius:10px;">
        <h3>👤 Alex</h3>
        <p>Receives payments</p>
        </div>

        </div>
        """, unsafe_allow_html=True)

        st.markdown("### 🧠 Understand the bond")

        st.write("**Principal:** The amount lent or the amount specified for repayment.")
        st.write("**Issuer:** The company or government borrowing money.")
        st.write("**Investor:** The person buying the bond.")
        st.write("**Coupon:** Interest payment specified in the bond terms.")
        st.write("**Maturity:** The scheduled date when the bond principal is due.")

        st.markdown("### 🎮 Bond ownership simulator")

        investment = st.slider(
            "How much money will Alex lend?",
            1000, 100000, 10000, 1000
        )

        st.metric("Alex's Bond Investment", f"₹{investment:,}")

        st.info(
            "Alex is lending this amount to the bond issuer. "
            "The investment is not a bank deposit, and repayment "
            "is not guaranteed."
        )

        st.markdown("### 📝 Quick quiz")

        bond_quiz("chapter6_l21", [
            {
                "question": "When Alex buys a corporate bond, what is Alex?",
                "options": [
                    "A company owner automatically",
                    "A lender to the company",
                    "The company's employee",
                    "The company's regulator"
                ],
                "answer": "A lender to the company",
                "explanation": "A bond represents debt. The issuer borrows money from bond investors."
            },
            {
                "question": "What is maturity?",
                "options": [
                    "The bond's scheduled repayment date",
                    "The day the bond is advertised",
                    "The investor's birthday",
                    "The day the company is founded"
                ],
                "answer": "The bond's scheduled repayment date",
                "explanation": "Maturity is the date the bond principal is due under its terms."
            }
        ])

    # -------------------------------------------------
    # LESSON 22
    # -------------------------------------------------

    elif lesson == "Lesson 22 — How Bond Interest Works":

        st.header("💰 Lesson 22 — How Bond Interest Works")

        st.markdown("""
        ### Alex buys a bond

        Alex buys a bond with:

        - Face value: ₹10,000
        - Annual coupon rate: 8%
        - Duration: 5 years

        The bond pays interest according to its terms.

        Let's calculate the coupon payments.
        """)

        principal = st.number_input(
            "Bond face value (₹)",
            min_value=1000,
            value=10000,
            step=1000
        )

        rate = st.slider(
            "Annual coupon rate (%)",
            1.0, 20.0, 8.0, 0.5
        )

        years = st.slider(
            "Years until maturity",
            1, 30, 5
        )

        annual_coupon = principal * rate / 100
        total_coupon = annual_coupon * years

        st.metric("Annual coupon", f"₹{annual_coupon:,.2f}")
        st.metric(
            "Total coupon payments over the years",
            f"₹{total_coupon:,.2f}"
        )

        st.metric(
            "Principal due at maturity",
            f"₹{principal:,.2f}"
        )

        st.warning(
            "These calculations assume the issuer pays all scheduled "
            "coupon payments and repays the principal. They do not "
            "account for taxes, reinvestment or inflation."
        )

        st.markdown("### 📊 Coupon payment visualization")

        fig = go.Figure()

        fig.add_trace(go.Bar(
            x=["Year 1", "Year 2", "Year 3", "Year 4", "Year 5"],
            y=[annual_coupon] * 5,
            name="Annual coupon"
        ))

        fig.update_layout(
            title="Illustrative annual coupon payments",
            yaxis_title="Payment (₹)",
            xaxis_title="Year"
        )

        st.plotly_chart(fig, use_container_width=True)

        st.markdown("""
        ### Coupon rate vs yield

        **Coupon rate:** The interest rate applied to the bond's face value
        to determine scheduled coupon payments.

        **Yield:** A measure of the return based on the bond's price
        and cash flows. Yield to maturity also considers the scheduled
        remaining cash flows and repayment at maturity, subject to
        assumptions.

        A bond's coupon rate and yield are not necessarily the same.
        """)

        st.markdown("### 📝 Quick quiz")

        bond_quiz("chapter6_l22", [
            {
                "question": "A ₹10,000 bond has an 8% annual coupon rate. What is its annual coupon?",
                "options": [
                    "₹80",
                    "₹800",
                    "₹8,000",
                    "₹10,800"
                ],
                "answer": "₹800",
                "explanation": "₹10,000 × 8% = ₹800 per year, assuming annual coupon payments."
            },
            {
                "question": "Is coupon rate always equal to yield?",
                "options": [
                    "Yes, always",
                    "No, they can differ",
                    "Only for stocks",
                    "Only for bank accounts"
                ],
                "answer": "No, they can differ",
                "explanation": "Yield depends on the bond's price and cash flows, not just its coupon rate."
            }
        ])

    # -------------------------------------------------
    # LESSON 23
    # -------------------------------------------------

    elif lesson == "Lesson 23 — Why Bond Prices Change":

        st.header("📈 Lesson 23 — Why Bond Prices Change")

        st.markdown("""
        ### The interest-rate puzzle

        Alex owns a bond that pays 8% interest.

        Suddenly, newly issued similar bonds offer 10%.

        Would investors want to pay the same price for Alex's
        old bond with an 8% coupon?

        Often, the old bond's market price falls to make it
        more competitive with newer bonds.
        """)

        st.markdown("""
        <div style="padding:20px;background:#182C44;
        border-radius:12px;color:white;text-align:center;">

        <h3>📉 Interest rates rise</h3>

        <p>⬇️</p>

        <h3>Existing bond prices often fall</h3>

        <p>Conversely, when comparable market rates fall,
        existing bond prices often rise.</p>

        </div>
        """, unsafe_allow_html=True)

        st.markdown("### 🎮 Price-change simulator")

        face_value = st.number_input(
            "Bond face value (₹)",
            min_value=1000,
            value=10000,
            step=1000,
            key="l23_face"
        )

        coupon_rate = st.number_input(
            "Bond coupon rate (%)",
            min_value=0.1,
            value=8.0,
            step=0.5,
            key="l23_coupon"
        )

        market_rate = st.slider(
            "Comparable market interest rate (%)",
            1.0, 20.0, 10.0, 0.5,
            key="l23_market"
        )

        original_coupon = face_value * coupon_rate / 100

        # Simplified illustration: perpetuity-like price approximation.
        # This is NOT an actual bond valuation formula.

        if market_rate > 0:
            simplified_price = original_coupon / (market_rate / 100)
        else:
            simplified_price = face_value

        st.metric(
            "Annual coupon payment",
            f"₹{original_coupon:,.2f}"
        )

        st.metric(
            "Simplified illustrative price",
            f"₹{simplified_price:,.2f}"
        )

        st.caption(
            "This simplified model treats the coupon as a perpetuity. "
            "It does not include repayment of principal at maturity, "
            "so it is not a realistic price for a standard finite-maturity "
            "bond. It is used only to illustrate how price and market "
            "rates can move in opposite directions."
        )

        st.markdown("### 📚 What else changes bond prices?")

        st.write("**Credit risk:** Investors may worry the issuer will not pay.")
        st.write("**Inflation:** Future money may buy less.")
        st.write("**Liquidity:** Some bonds are harder to sell.")
        st.write("**Time to maturity:** Longer-duration bonds can be more sensitive to rate changes.")
        st.write("**Supply and demand:** Buying and selling pressure can move prices.")

        st.markdown("### 📝 Quick quiz")

        bond_quiz("chapter6_l23", [
            {
                "question": "If comparable interest rates rise, what often happens to existing fixed-rate bond prices?",
                "options": [
                    "They often fall",
                    "They always double",
                    "They cannot change",
                    "They always rise"
                ],
                "answer": "They often fall",
                "explanation": "Existing fixed coupons become less attractive relative to new bonds, so prices often decline."
            },
            {
                "question": "Which risk can cause a bond issuer to fail to pay?",
                "options": [
                    "Credit risk",
                    "Animation risk",
                    "Screen risk",
                    "Keyboard risk"
                ],
                "answer": "Credit risk",
                "explanation": "Credit risk is the possibility that the issuer will not meet its payment obligations."
            }
        ])

    # -------------------------------------------------
    # LESSON 24
    # -------------------------------------------------

    elif lesson == "Lesson 24 — Bond Risks & Types":

        st.header("🛡️ Lesson 24 — Bond Risks & Types")

        st.markdown("""
        ### Alex discovers that not all bonds are the same

        Alex discovers bonds issued by governments, companies
        and other organizations.

        Each has different risks and payment terms.
        """)

        st.markdown("### 🌍 Different types of bonds")

        with st.expander("🏛️ Government bonds"):
            st.write("""
            Issued by governments to finance spending and manage
            their borrowing.

            Government bonds still carry risks, such as inflation,
            interest-rate risk and, depending on the issuer,
            credit or currency risk.
            """)

        with st.expander("🏢 Corporate bonds"):
            st.write("""
            Issued by companies to raise funds.

            They may offer higher yields than comparable government
            bonds, but the issuer's credit risk may also be higher.
            """)

        with st.expander("📉 High-yield bonds"):
            st.write("""
            Bonds rated below investment grade generally offer
            higher yields because investors face greater credit risk.
            """)

        with st.expander("🌐 International bonds"):
            st.write("""
            Bonds issued in or connected with foreign markets.

            Foreign-currency bonds can expose investors to currency
            exchange-rate risk.
            """)

        st.markdown("### ⚠️ The five major bond risks")

        st.write("1. **Interest-rate risk** — prices may fall as market rates rise.")
        st.write("2. **Credit risk** — the issuer may fail to pay.")
        st.write("3. **Inflation risk** — purchasing power may decline.")
        st.write("4. **Liquidity risk** — selling may be difficult or costly.")
        st.write("5. **Currency risk** — exchange rates may affect foreign investments.")

        st.markdown("### 🎮 Risk comparison")

        risk_options = {
            "Government bond (illustrative)": 2,
            "Investment-grade corporate bond (illustrative)": 4,
            "High-yield corporate bond (illustrative)": 8
        }

        selected = st.selectbox(
            "Choose a bond category",
            list(risk_options.keys())
        )

        st.progress(risk_options[selected] / 10)

        st.caption(
            "The displayed scale is a fictional teaching illustration, "
            "not a real risk rating or investment recommendation."
        )

        st.markdown("### 🧠 Final quiz")

        bond_quiz("chapter6_l24", [
            {
                "question": "Why might a high-yield bond offer a higher interest rate?",
                "options": [
                    "It always has zero risk",
                    "Investors may face greater credit risk",
                    "It is guaranteed by every government",
                    "It cannot lose value"
                ],
                "answer": "Investors may face greater credit risk",
                "explanation": "Higher yields can compensate investors for greater perceived credit risk, among other factors."
            },
            {
                "question": "What is inflation risk?",
                "options": [
                    "The risk of losing your password",
                    "The risk that purchasing power declines",
                    "The risk that a bond never has a coupon",
                    "The risk that an exchange closes every day"
                ],
                "answer": "The risk that purchasing power declines",
                "explanation": "Inflation can reduce the real value of future interest and principal payments."
            },
            {
                "question": "Can a government bond lose market value before maturity?",
                "options": [
                    "No, never",
                    "Yes, market prices can change",
                    "Only corporate bonds change",
                    "Only when coupon rates are zero"
                ],
                "answer": "Yes, market prices can change",
                "explanation": "Government bonds can lose market value due to interest-rate changes, inflation expectations and other factors."
            }
        ])

        st.markdown("""
        <div style="padding:20px;background:#153448;
        border-radius:12px;color:white;">

        <h3>🎓 Chapter 6 Complete!</h3>

        <p>Alex now understands the basics of bonds.</p>

        <p>Alex knows that bonds are loans to issuers,
        that coupons are defined by bond terms,
        that market rates can affect prices,
        and that bonds are not risk-free.</p>

        <h3>🚀 Next: Chapter 7</h3>

        </div>
        """, unsafe_allow_html=True)


</codeblock>

