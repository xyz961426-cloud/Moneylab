
import streamlit as st
import plotly.graph_objects as go

st.set_page_config(layout="wide")


def scene(title, dialogue, color="#17324d"):
    st.markdown(f"""
    <style>
    @keyframes floatMoney {{
        0%,100% {{ transform:translateY(0px); }}
        50% {{ transform:translateY(-12px); }}
    }}
    @keyframes slideMoney {{
        0% {{ transform:translateX(-20px);opacity:0.2; }}
        100% {{ transform:translateX(0px);opacity:1; }}
    }}
    @keyframes glow {{
        0%,100% {{ box-shadow:0 0 5px rgba(60,180,255,0.1); }}
        50% {{ box-shadow:0 0 22px rgba(60,180,255,0.4); }}
    }}
    @keyframes growBar {{
        from {{ transform:scaleY(0); }}
        to {{ transform:scaleY(1); }}
    }}
    .moneylab-scene {{
        background:linear-gradient(135deg,{color},#101827);
        border-radius:22px;
        padding:28px;
        color:white;
        animation:slideMoney 0.7s ease;
        margin-bottom:15px;
    }}
    .moneylab-character {{
        font-size:65px;
        animation:floatMoney 3s ease-in-out infinite;
        text-align:center;
    }}
    .moneylab-dialogue {{
        font-size:19px;
        line-height:1.7;
        padding:14px;
        background:rgba(255,255,255,0.08);
        border-radius:15px;
        margin-top:12px;
    }}
    .moneylab-flow {{
        display:flex;
        align-items:center;
        justify-content:space-around;
        gap:10px;
        flex-wrap:wrap;
        font-size:25px;
        text-align:center;
        margin:20px 0;
    }}
    .moneylab-box {{
        padding:18px;
        border:1px solid rgba(255,255,255,0.2);
        border-radius:16px;
        animation:glow 3s infinite;
        min-width:120px;
    }}
    .moneylab-arrow {{
        animation:floatMoney 1.5s infinite;
    }}
    </style>

    <div class="moneylab-scene">
        <div class="moneylab-character">🧑‍💼</div>
        <h2 style="text-align:center;">{title}</h2>
        <div class="moneylab-dialogue">{dialogue}</div>
    </div>
    """, unsafe_allow_html=True)


def flow(left, middle, right):
    st.markdown(f"""
    <div class="moneylab-flow">
        <div class="moneylab-box">{left}</div>
        <div class="moneylab-arrow">➡️💰➡️</div>
        <div class="moneylab-box">{middle}</div>
        <div class="moneylab-arrow">➡️</div>
        <div class="moneylab-box">{right}</div>
    </div>
    """, unsafe_allow_html=True)


def quiz(key, question, options, answer, explanation):
    if key not in st.session_state:
        st.session_state[key] = False

    choice = st.radio(
        question,
        options,
        index=None,
        key=key + "_choice"
    )

    if st.button("Check answer", key=key + "_check"):
        st.session_state[key] = True
        st.session_state[key + "_submitted"] = choice

    if st.session_state.get(key + "_submitted") is not None:
        submitted = st.session_state[key + "_submitted"]

        if submitted == answer:
            st.success("Correct! " + explanation)
        else:
            st.error("Not quite. Your answer: " + str(submitted))
            st.info("Correct answer: " + answer)
            st.write(explanation)


def show_chapter6():

    st.title("🏦 Chapter 6: The World of Bonds")
    st.caption("MoneyLab • Learn Money by Living It")

    lessons = [
        "21 • Discover Bonds",
        "22 • Earn Interest",
        "23 • Bond Price Mystery",
        "24 • Bond Risk Challenge"
    ]

    if "chapter6_lesson" not in st.session_state:
        st.session_state.chapter6_lesson = 0

    if "chapter6_completed" not in st.session_state:
        st.session_state.chapter6_completed = []

    current = st.session_state.chapter6_lesson

    st.progress((current + 1) / 4)
    st.caption(f"Lesson {current + 1} of 4")

    selected = st.selectbox(
        "Your journey",
        lessons,
        index=current,
        key="chapter6_navigation"
    )

    selected_index = lessons.index(selected)

    if selected_index != current:
        st.session_state.chapter6_lesson = selected_index
        st.rerun()

    st.divider()

    # LESSON 21

    if current == 0:

        scene(
            "Alex discovers a new way to invest",
            "Alex has learned about stocks. But a friend "
            "introduces Alex to another idea: lending money "
            "to governments or companies in exchange for "
            "payments under a bond agreement."
        )

        st.markdown("### 🎬 What happens when Alex buys a bond?")

        flow("👤 Alex<br>Lender", "💰 Money", "🏢 Company<br>Borrower")

        st.markdown("""
        <div style="padding:16px;border-radius:12px;background:#102b3f;color:white;">
        <b>The deal:</b> Alex lends money. The issuer agrees
        to make payments under the bond's terms and repay
        the principal at maturity, subject to its ability to pay.
        </div>
        """, unsafe_allow_html=True)

        st.markdown("### 🧠 Learn the five important words")

        with st.expander("💵 Principal"):
            st.write("The amount lent or the amount specified for repayment.")

        with st.expander("🏢 Issuer"):
            st.write("The government or company that borrows money.")

        with st.expander("👤 Bondholder"):
            st.write("The investor who owns the bond.")

        with st.expander("💰 Coupon"):
            st.write("The interest payment specified by the bond terms.")

        with st.expander("📅 Maturity"):
            st.write("The scheduled date when principal is due.")

        st.markdown("### 🎮 Alex's lending decision")

        investment = st.slider(
            "How much should Alex lend?",
            1000, 100000, 10000, 1000,
            key="l21_investment"
        )

        st.metric("Amount lent", f"₹{investment:,}")

        st.markdown("""
        <div style="padding:16px;border-radius:12px;background:#142e46;color:white;">
        🏢 The company receives the money to finance its activities.

        👤 Alex becomes a bondholder, not a company owner.
        </div>
        """, unsafe_allow_html=True)

        quiz(
            "l21quiz",
            "When Alex buys a corporate bond, Alex becomes:",
            [
                "A company owner",
                "A lender to the company",
                "An employee",
                "A regulator"
            ],
            "A lender to the company",
            "A bond represents a debt obligation. The issuer borrows from investors."
        )

    # LESSON 22

    elif current == 1:

        scene(
            "Alex starts receiving payments",
            "Alex lent ₹10,000 to a company. The bond "
            "specifies an annual coupon rate of 8%. "
            "Alex wants to understand how the payments work."
        )

        st.markdown("### 🎬 Calculate the interest")

        principal = st.slider(
            "Bond face value (₹)",
            1000, 100000, 10000, 1000,
            key="l22_principal"
        )

        rate = st.slider(
            "Annual coupon rate (%)",
            1.0, 20.0, 8.0, 0.5,
            key="l22_rate"
        )

        years = st.slider(
            "Years",
            1, 30, 5,
            key="l22_years"
        )

        annual = principal * rate / 100
        total = annual * years

        st.metric("Annual coupon", f"₹{annual:,.2f}")
        st.metric("Total scheduled coupons over selected years", f"₹{total:,.2f}")

        st.markdown("### 💸 Watch the payments")

        fig = go.Figure()

        fig.add_trace(go.Bar(
            x=[f"Year {i}" for i in range(1, years + 1)],
            y=[annual] * years,
            name="Coupon payment"
        ))

        fig.update_layout(
            title="Illustrative coupon payments",
            xaxis_title="Year",
            yaxis_title="Payment (₹)",
            height=350
        )

        st.plotly_chart(fig, use_container_width=True)

        st.markdown("""
        <div style="padding:16px;background:#102b3f;border-radius:12px;color:white;">
        💡 Coupon payments are calculated using the face value
        and coupon rate, according to the bond's terms.
        </div>
        """, unsafe_allow_html=True)

        st.markdown("### 🔍 Coupon vs yield")

        with st.expander("Coupon rate"):
            st.write("The rate used to calculate scheduled interest payments on face value.")

        with st.expander("Yield"):
            st.write("A measure of return based on the bond's price and cash flows. Yield to maturity also incorporates scheduled remaining cash flows and repayment at maturity, subject to assumptions.")

        quiz(
            "l22quiz",
            "₹10,000 at an 8% annual coupon rate gives how much annual coupon?",
            ["₹80", "₹800", "₹8,000", "₹10,800"],
            "₹800",
            "₹10,000 × 0.08 = ₹800 per year, assuming annual coupon payments."
        )

    # LESSON 23

    elif current == 2:

        scene(
            "The bond price mystery",
            "Alex bought a bond paying 8%. Now new similar "
            "bonds offer 10%. Buyers may prefer the newer "
            "bonds. Alex discovers that bond prices can change."
        )

        st.markdown("### 🎮 Market interest rate experiment")

        face = st.slider(
            "Face value (₹)",
            1000, 100000, 10000, 1000,
            key="l23_face"
        )

        coupon_rate = st.slider(
            "Existing annual coupon (%)",
            1.0, 20.0, 8.0, 0.5,
            key="l23_coupon"
        )

        market_rate = st.slider(
            "New comparable market rate (%)",
            1.0, 20.0, 10.0, 0.5,
            key="l23_market"
        )

        annual_coupon = face * coupon_rate / 100

        price = None

        if market_rate > 0:
            price = annual_coupon / (market_rate / 100)

        st.metric("Existing annual coupon", f"₹{annual_coupon:,.2f}")

        st.metric(
            "Simplified illustrative price",
            f"₹{price:,.2f}"
        )

        st.caption(
            "This is a simplified perpetuity-like illustration. "
            "It excludes principal repayment at maturity and is not "
            "the valuation formula for a standard finite-maturity bond."
        )

        if market_rate > coupon_rate:
            st.warning("New comparable rates are higher than the existing coupon rate.")
        elif market_rate < coupon_rate:
            st.success("The existing coupon is higher than new comparable rates.")
        else:
            st.info("The coupon rate and comparable market rate are equal.")

        st.markdown("### 📉 The inverse relationship")

        fig = go.Figure()

        rates = list(range(2, 21))
        prices = [
            annual_coupon / (r / 100)
            for r in rates
        ]

        fig.add_trace(go.Scatter(
            x=rates,
            y=prices,
            mode="lines+markers",
            name="Illustrative price"
        ))

        fig.update_layout(
            title="Illustrative bond price vs market rate",
            xaxis_title="Market rate (%)",
            yaxis_title="Price (₹)",
            height=350
        )

        st.plotly_chart(fig, use_container_width=True)

        st.markdown("""
        <div style="padding:16px;border-radius:12px;background:#102b3f;color:white;">
        📈 Comparable market rates fall → Existing fixed-rate bond prices often rise.

        📉 Comparable market rates rise → Existing fixed-rate bond prices often fall.
        </div>
        """, unsafe_allow_html=True)

        quiz(
            "l23quiz",
            "When comparable interest rates rise, existing fixed-rate bond prices often:",
            [
                "Rise",
                "Fall",
                "Remain permanently fixed",
                "Become worthless automatically"
            ],
            "Fall",
            "Existing coupons become less competitive, so their market prices often fall."
        )

    # LESSON 24

    elif current == 3:

        scene(
            "Alex must choose a bond",
            "Alex has discovered that bonds are not all equally "
            "safe. Before investing, Alex compares the issuer "
            "and the risks."
        )

        st.markdown("### 🌍 Explore bond types")

        with st.expander("🏛️ Government bonds"):
            st.write("Issued by governments. They can still face interest-rate, inflation, credit and currency risks, depending on the issuer and bond.")

        with st.expander("🏢 Corporate bonds"):
            st.write("Issued by companies. Investors assess the company's financial health and ability to repay.")

        with st.expander("📉 High-yield bonds"):
            st.write("Generally rated below investment grade and often offer higher yields because credit risk is greater.")

        with st.expander("🌐 International bonds"):
            st.write("May involve currency risk, international market conditions and other risks.")

        st.markdown("### ⚠️ Risk explorer")

        risks = {
            "Interest-rate risk": "Bond prices can fall when comparable market rates rise.",
            "Credit risk": "The issuer may fail to pay interest or principal.",
            "Inflation risk": "Inflation may reduce the purchasing power of payments.",
            "Liquidity risk": "Selling a bond may be difficult or costly.",
            "Currency risk": "Exchange rates can affect foreign-currency investments."
        }

        selected_risk = st.selectbox(
            "Explore a risk",
            list(risks.keys())
        )

        st.warning(risks[selected_risk])

        st.markdown("### 🎮 Alex's decision challenge")

        choice = st.radio(
            "Alex wants higher yield. Which decision is more responsible?",
            [
                "Buy the highest-yield bond without research",
                "Compare credit risk, price, terms and financial goals",
                "Assume all bonds are guaranteed",
                "Invest all savings in one bond"
            ],
            index=None,
            key="l24decision"
        )

        if st.button("Submit decision", key="l24submit"):
            if choice == "Compare credit risk, price, terms and financial goals":
                st.success("Excellent decision! Yield alone does not determine whether a bond is suitable.")
            elif choice is not None:
                st.error("That decision overlooks important risks.")
                st.info("A bond should be evaluated using its issuer, terms, price, risk and how it fits your financial goals.")

        st.markdown("### 🧠 Final challenge")

        quiz(
            "l24quiz",
            "Can a government bond lose market value before maturity?",
            [
                "No, never",
                "Yes, its market price can change",
                "Only corporate bonds change",
                "Only zero-coupon bonds change"
            ],
            "Yes, its market price can change",
            "Government bonds can change in value due to interest rates, inflation expectations, credit conditions and other factors."
        )

        st.markdown("""
        <div style="padding:20px;border-radius:18px;background:linear-gradient(135deg,#123c53,#142433);color:white;">
        <h2>🏆 Chapter 6 Journey</h2>
        <p>Alex now understands the basics of bonds.</p>
        <p>Alex can explain lending, coupon payments, price changes
        and bond risks.</p>
        <h3>🚀 Next stop: Chapter 7 — Mutual Funds & ETFs</h3>
        </div>
        """, unsafe_allow_html=True)

    st.divider()

    col1, col2, col3 = st.columns(3)

    with col1:
        if current > 0:
            if st.button("⬅️ Previous lesson", use_container_width=True):
                st.session_state.chapter6_lesson -= 1
                st.rerun()

    with col2:
        st.write(f"Lesson {current + 1}/4")

    with col3:
        if current < 3:
            if st.button("Next lesson ➡️", use_container_width=True):
                st.session_state.chapter6_lesson += 1
                st.rerun()
        else:
            st.button("🏆 Chapter completed", disabled=True, use_container_width=True)
