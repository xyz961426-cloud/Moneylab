import streamlit as st


def show_chapter5():
    st.title("📈 Chapter 5: The Investing World")
    st.caption("MoneyLab • Lessons 17–20")

    lessons = {
        "Lesson 17 — What Is the Stock Market?": 17,
        "Lesson 18 — Why Companies Sell Shares": 18,
        "Lesson 19 — How Investors Make and Lose Money": 19,
        "Lesson 20 — Stock Market Participants": 20,
    }

    selected = st.selectbox("📚 Chapter 5", list(lessons.keys()))
    number = lessons[selected]

    st.progress((number - 16) / 4)

    if number == 17:
        lesson17()
    elif number == 18:
        lesson18()
    elif number == 19:
        lesson19()
    elif number == 20:
        lesson20()


# =========================================================
# LESSON 17 — WHAT IS THE STOCK MARKET?
# =========================================================

def lesson17():
    st.header("📈 Lesson 17: What Is the Stock Market?")

    st.markdown("""
    ### Alex discovers the stock market

    Alex has learned how to manage money and debt.

    One day, he hears that people can buy ownership in companies.

    He wonders:

    **"If I buy a share, what exactly do I own?"**
    """)

    st.subheader("1. What is a company?")

    st.write("""
    A company is an organization that carries out activities such
    as selling products, providing services or developing technology.

    Companies may need money to:
    - Expand their operations.
    - Hire employees.
    - Build factories.
    - Develop products.
    - Enter new markets.
    - Research new technologies.
    """)

    st.subheader("2. What is a share?")

    st.write("""
    A share represents a unit of ownership in a company.

    If a company has 1,000 shares and you own 100 shares,
    you own 10% of its outstanding shares, assuming the share
    count is the relevant total and there are no other ownership
    arrangements affecting that calculation.

    Ownership can provide certain rights, depending on the type
    of share and the company's rules.
    """)

    st.markdown("""
    <div style="padding:16px;border-radius:12px;background:#e9f5ff;color:#102a43;">
    <b>Owning shares is not the same as lending money.</b>

    A shareholder owns an interest in the company. A lender has
    a claim based on a lending agreement. Their rights and risks differ.
    </div>
    """, unsafe_allow_html=True)

    st.subheader("3. Ownership simulator")

    total_shares = st.number_input(
        "Total company shares",
        min_value=1,
        value=1000,
        step=100,
        key="l17_total"
    )

    owned = st.number_input(
        "Shares Alex owns",
        min_value=0,
        value=100,
        step=10,
        key="l17_owned"
    )

    if owned <= total_shares:
        percentage = owned / total_shares * 100
        st.metric("Alex's ownership", f"{percentage:.2f}%")
    else:
        st.warning("Alex's shares cannot exceed the entered total in this example.")

    st.subheader("4. What is the stock market?")

    st.write("""
    A stock market is a system in which shares and other securities
    can be bought and sold.

    Stock markets bring buyers and sellers together through exchanges
    and other trading infrastructure.

    Markets help:
    - Connect buyers and sellers.
    - Facilitate trading.
    - Provide price information.
    - Allow investors to transfer ownership.
    - Support capital formation through securities markets.
    """)

    st.subheader("5. How does a trade happen?")

    st.write("""
    Imagine Alex wants to buy one share.

    A seller wants to sell one share.

    Both sides must have compatible orders. The trading system can
    match their orders according to the exchange's rules.
    """)

    buyer_price = st.number_input(
        "Alex's maximum buying price (₹)",
        min_value=0.0,
        value=100.0,
        step=1.0,
        key="l17_buyer"
    )

    seller_price = st.number_input(
        "Seller's minimum selling price (₹)",
        min_value=0.0,
        value=98.0,
        step=1.0,
        key="l17_seller"
    )

    if buyer_price >= seller_price:
        st.success(
            "The prices are compatible in this simplified example. "
            "A trade may occur depending on order priority and market rules."
        )
    else:
        st.info("The prices are not compatible yet. The buyer and seller may not trade.")

    st.subheader("6. Why does a share price change?")

    st.write("""
    Share prices can change as buyers and sellers place orders
    and as market conditions evolve.

    Participants may react to:
    - Company earnings.
    - Economic data.
    - Interest rates.
    - News.
    - Expectations about the future.
    - Risk.
    - Supply and demand for shares.

    A price change does not necessarily mean the company itself
    changed by the same amount in value.
    """)

    st.subheader("7. What is a stock exchange?")

    st.write("""
    A stock exchange is an organized marketplace with rules and
    systems for trading securities.

    Examples include:
    - NSE (National Stock Exchange of India).
    - BSE (BSE Ltd., formerly Bombay Stock Exchange).
    - NYSE (New York Stock Exchange).
    - Nasdaq.

    Exchanges are part of a larger financial market ecosystem
    that includes brokers, clearing systems and regulators.
    """)

    market_quiz(
        "l17",
        [
            {
                "q": "What does a share generally represent?",
                "options": [
                    "A unit of ownership in a company.",
                    "A guaranteed loan repayment.",
                    "A guaranteed profit."
                ],
                "correct": 0,
                "explanation": "A share generally represents an ownership interest in a company. "
                              "Its rights depend on the share class and company rules."
            },
            {
                "q": "What does a stock market help facilitate?",
                "options": [
                    "Only guaranteed profits.",
                    "Trading between buyers and sellers.",
                    "Eliminating all investment risks."
                ],
                "correct": 1,
                "explanation": "Markets provide systems and rules that help buyers and sellers "
                              "trade securities."
            },
            {
                "q": "Why can share prices change?",
                "options": [
                    "Prices never change.",
                    "Only the company founder changes them.",
                    "Orders, expectations, information and market conditions can change."
                ],
                "correct": 2,
                "explanation": "Prices can move as participants react to information, "
                              "expectations, supply, demand and other conditions."
            }
        ]
    )

    st.info("Next: Why would a company give ownership shares to other people?")


# =========================================================
# LESSON 18 — WHY COMPANIES SELL SHARES
# =========================================================

def lesson18():
    st.header("🏢 Lesson 18: Why Companies Sell Shares")

    st.markdown("""
    ### Alex meets a company founder

    A fictional company called NovaTech wants to build a new factory.

    The founder needs ₹10 crore.

    The company considers raising money by selling shares.

    **Why would a founder share ownership with other investors?**
    """)

    st.subheader("1. Why companies need capital")

    st.write("""
    Businesses may need capital for:
    - Expansion.
    - Equipment.
    - Research and development.
    - Hiring.
    - Acquisitions.
    - Infrastructure.
    - Working capital.

    Capital can come from different sources, including retained profits,
    borrowing and issuing equity.
    """)

    st.subheader("2. Equity vs borrowing")

    with st.expander("📊 Equity financing"):
        st.write("""
        Equity financing involves raising money by issuing ownership
        interests in a company.

        The company generally does not have a contractual obligation
        to repay equity investors the amount they invested in the way
        a loan is repaid.

        Existing ownership can be diluted when additional shares are issued.
        """)

    with st.expander("🏦 Debt financing"):
        st.write("""
        Debt financing involves borrowing money.

        Borrowing generally creates repayment obligations, which may
        include interest and other terms.

        Debt does not generally grant the lender ownership of the company,
        although loan agreements may contain additional rights and conditions.
        """)

    st.subheader("3. Ownership simulator")

    st.write("NovaTech starts with 1,000 shares.")

    founders = st.number_input(
        "Shares owned by founders",
        min_value=1,
        value=1000,
        step=100,
        key="l18_founders"
    )

    new_shares = st.number_input(
        "New shares issued to investors",
        min_value=0,
        value=500,
        step=100,
        key="l18_newshares"
    )

    total = founders + new_shares

    founder_percent = founders / total * 100 if total else 0
    investor_percent = new_shares / total * 100 if total else 0

    st.metric("Total shares after issuance", f"{total:,}")
    st.metric("Founders' ownership after issuance", f"{founder_percent:.2f}%")
    st.metric("New investors' ownership", f"{investor_percent:.2f}%")

    st.write("""
    If the company issues additional shares, existing shareholders
    may own a smaller percentage of the company.

    This is called dilution.

    Dilution of percentage ownership does not automatically mean
    that the economic value of an existing shareholder's holding
    has decreased. The value received by the company and other
    factors also matter.
    """)

    st.subheader("4. What is an IPO?")

    st.write("""
    IPO stands for Initial Public Offering.

    It is the process in which a company offers shares to the public
    for the first time through a public offering, subject to the
    applicable process and regulations.

    An IPO can help a company raise capital and may allow certain
    existing shareholders to sell shares, depending on the offering.
    """)

    st.subheader("5. Primary market vs secondary market")

    with st.expander("🏭 Primary market"):
        st.write("""
        In the primary market, securities are issued and sold to
        investors as part of an offering.

        In an equity offering, the proceeds from newly issued shares
        generally go to the issuing company, subject to the transaction.
        """)

    with st.expander("🔄 Secondary market"):
        st.write("""
        In the secondary market, investors generally trade securities
        with other investors.

        When Alex buys an existing share from another investor,
        the company generally does not receive the money from that trade.
        """)

    st.subheader("6. Follow the money")

    transaction = st.radio(
        "Alex buys an existing share from another investor. Where does the purchase money generally go?",
        [
            "Directly to the company.",
            "To the seller of the share, through the trading and settlement process.",
            "To the company's employees."
        ],
        index=None,
        key="l18_transaction"
    )

    if transaction:
        if transaction == "To the seller of the share, through the trading and settlement process.":
            st.success("Correct. In an ordinary secondary-market trade, Alex pays the seller.")
        else:
            st.warning("In a secondary-market trade, the seller generally receives the sale proceeds, "
                       "not the company.")

    st.subheader("7. Why would a founder sell ownership?")

    st.write("""
    A founder may want capital to grow the business.

    Selling ownership can help fund expansion, but it means sharing
    ownership and potentially some control or influence.

    The founder must weigh the benefits of capital against dilution
    and other considerations.
    """)

    market_quiz(
        "l18",
        [
            {
                "q": "Why might a company issue new shares?",
                "options": [
                    "To raise equity capital.",
                    "To guarantee future profits.",
                    "To eliminate every risk."
                ],
                "correct": 0,
                "explanation": "Issuing shares can help a company raise equity capital "
                              "to fund business activities."
            },
            {
                "q": "What is dilution?",
                "options": [
                    "A guaranteed increase in share price.",
                    "A reduction in existing ownership percentage when the share count increases.",
                    "A loan payment."
                ],
                "correct": 1,
                "explanation": "Issuing additional shares can reduce an existing shareholder's "
                              "percentage ownership of the company."
            },
            {
                "q": "In an ordinary secondary-market trade, who generally receives the proceeds?",
                "options": [
                    "The company.",
                    "The seller.",
                    "The stock exchange's employees."
                ],
                "correct": 1,
                "explanation": "The buyer generally pays the selling shareholder. "
                              "The company is not ordinarily receiving proceeds from that trade."
            }
        ]
    )

    st.info("Next: How can Alex actually earn or lose money by owning shares?")


# =========================================================
# LESSON 19 — HOW INVESTORS MAKE AND LOSE MONEY
# =========================================================

def lesson19():
    st.header("💰 Lesson 19: How Investors Make and Lose Money")

    st.markdown("""
    ### Alex buys shares

    Alex buys 10 shares of a fictional company at ₹100 each.

    His investment is ₹1,000 before fees.

    A year later, the share price changes.

    **Did Alex make money or lose money?**
    """)

    st.subheader("1. Capital gain and capital loss")

    st.write("""
    A capital gain occurs when an investment is sold for more
    than its purchase cost, before accounting for applicable
    fees and taxes.

    A capital loss occurs when an investment is sold for less
    than its purchase cost.

    A price increase or decrease before selling may represent
    an unrealized gain or loss.
    """)

    st.subheader("2. Stock investment simulator")

    quantity = st.number_input(
        "Shares purchased",
        min_value=1,
        value=10,
        step=1,
        key="l19_quantity"
    )

    buy_price = st.number_input(
        "Purchase price per share (₹)",
        min_value=0.0,
        value=100.0,
        step=1.0,
        key="l19_buy"
    )

    current_price = st.number_input(
        "Current or selling price per share (₹)",
        min_value=0.0,
        value=120.0,
        step=1.0,
        key="l19_current"
    )

    dividend_per_share = st.number_input(
        "Dividend per share (₹)",
        min_value=0.0,
        value=2.0,
        step=0.5,
        key="l19_dividend"
    )

    invested = quantity * buy_price
    current_value = quantity * current_price
    price_change = current_value - invested
    dividends = quantity * dividend_per_share
    total_return = price_change + dividends

    st.metric("Initial investment", f"₹{invested:,.2f}")
    st.metric("Current share value", f"₹{current_value:,.2f}")
    st.metric("Price gain / loss", f"₹{price_change:,.2f}")
    st.metric("Illustrative dividends", f"₹{dividends:,.2f}")
    st.metric("Total return before costs and taxes", f"₹{total_return:,.2f}")

    if invested > 0:
        return_percent = total_return / invested * 100
        st.metric("Illustrative total return (%)", f"{return_percent:.2f}%")

    st.caption("This simulation excludes fees, taxes and timing differences.")

    st.subheader("3. Unrealized vs realized")

    with st.expander("📈 Unrealized gain or loss"):
        st.write("""
        An unrealized gain or loss reflects the current value of
        an investment compared with its cost, while it is still held.

        The amount can change as prices move.
        """)

    with st.expander("💵 Realized gain or loss"):
        st.write("""
        A realized gain or loss occurs when the investment is sold,
        based on the sale proceeds and cost basis, with adjustments
        as applicable.
        """)

    st.subheader("4. Dividends")

    st.write("""
    A dividend is a distribution of company profits or other funds
    to shareholders, when declared and paid according to the
    company's policy and applicable rules.

    Dividends are not guaranteed.

    A company may:
    - Pay a dividend.
    - Reduce a dividend.
    - Increase a dividend.
    - Suspend or omit a dividend.

    Dividend payments can also affect the share price and total
    return. A dividend is not free money.
    """)

    st.subheader("5. Why can investors lose money?")

    st.write("""
    Share prices may decline because of:
    - Poor company performance.
    - Lower expected earnings.
    - Competition.
    - Economic changes.
    - Market-wide declines.
    - Changes in interest rates.
    - Investor sentiment.
    - Unexpected events.

    Investors may lose some or all of their investment in an individual
    company, depending on circumstances.
    """)

    st.subheader("6. A price decline simulation")

    st.write("Alex owns shares worth ₹10,000.")

    decline = st.slider(
        "Price decline (%)",
        min_value=0,
        max_value=100,
        value=30,
        step=5,
        key="l19_decline"
    )

    value_after = 10000 * (1 - decline / 100)

    st.metric("Value after decline", f"₹{value_after:,.2f}")
    st.metric("Loss in value", f"₹{10000 - value_after:,.2f}")

    st.write("""
    A decline in price reduces the value of the investment.
    Recovering from a loss requires a percentage gain that is
    larger than the percentage decline.
    """)

    loss = decline

    if loss > 0:
        recovery = loss / (100 - loss) * 100 if loss < 100 else None

        if recovery is not None:
            st.metric("Gain required to recover", f"{recovery:.2f}%")

    st.subheader("7. Investment return is not guaranteed")

    st.write("""
    Historical returns do not guarantee future returns.

    A share can increase or decrease in value, and dividends
    may change or stop.
    """)

    market_quiz(
        "l19",
        [
            {
                "q": "When is a capital gain generally realized?",
                "options": [
                    "When the share price rises but is never sold.",
                    "When the investment is sold for more than its cost, before applicable adjustments.",
                    "When a loan is taken."
                ],
                "correct": 1,
                "explanation": "A realized capital gain generally occurs when an investment "
                              "is sold for more than its cost, subject to relevant adjustments."
            },
            {
                "q": "Are dividends guaranteed?",
                "options": [
                    "Yes, every company must pay them.",
                    "No, dividends depend on company decisions and circumstances.",
                    "Yes, regardless of company performance."
                ],
                "correct": 1,
                "explanation": "Dividends are not guaranteed. A company may change, suspend "
                              "or omit distributions."
            },
            {
                "q": "What is an unrealized gain?",
                "options": [
                    "A gain reflected in the value of an investment that is still held.",
                    "A loan repayment.",
                    "A guaranteed dividend."
                ],
                "correct": 0,
                "explanation": "An unrealized gain reflects a change in investment value "
                              "while the investment is still held."
            }
        ]
    )

    st.info("Next: Who actually makes the stock market operate?")


# =========================================================
# LESSON 20 — STOCK MARKET PARTICIPANTS
# =========================================================

def lesson20():
    st.header("🌐 Lesson 20: Stock Market Participants")

    st.markdown("""
    ### Alex places an order

    Alex decides to buy a share.

    But he doesn't directly call the company's founder.

    His order travels through a system involving several participants.

    **Let's understand the market ecosystem.**
    """)

    st.subheader("1. Retail investors")

    st.write("""
    Retail investors are individuals who invest or trade
    generally for their own accounts.

    They may invest through brokerage platforms and use
    different investment strategies.
    """)

    st.subheader("2. Institutional investors")

    st.write("""
    Institutional investors are organizations that invest
    money on behalf of themselves or clients.

    Examples may include:
    - Mutual funds.
    - Pension funds.
    - Insurance companies.
    - Investment firms.

    They may manage large pools of money and follow
    different investment mandates.
    """)

    st.subheader("3. Brokers")

    st.write("""
    Brokers provide access to trading markets.

    Depending on their services and regulatory framework,
    they may offer:
    - Order placement.
    - Trading platforms.
    - Research.
    - Account services.
    - Other financial services.

    A broker is not the same as the stock exchange.
    """)

    st.subheader("4. Exchanges")

    st.write("""
    Exchanges provide organized trading systems and rules.

    They may provide:
    - Order matching.
    - Market data.
    - Trading rules.
    - Market monitoring.
    - Systems for orderly trading.

    Actual trading and settlement involve multiple entities
    and infrastructure beyond the exchange alone.
    """)

    st.subheader("5. Market makers")

    st.write("""
    Market makers may quote buy and sell prices and provide
    liquidity in certain securities or markets.

    Their activities, obligations and role vary by market
    and instrument.

    Not every stock has an active market maker.
    """)

    st.subheader("6. Regulators")

    st.write("""
    Regulators oversee financial markets and market participants
    within their jurisdiction.

    Their responsibilities may include:
    - Investor protection.
    - Rules and compliance.
    - Market integrity.
    - Investigations.
    - Enforcement.

    In India, SEBI is the principal securities-market regulator.
    """)

    st.subheader("7. Clearing and settlement")

    st.write("""
    After a trade is matched, clearing and settlement systems
    help determine obligations and complete the transfer of
    securities and funds.

    These systems reduce operational risk and support the
    completion of transactions.
    """)

    st.subheader("8. Follow Alex's trade")

    stages = [
        ("1️⃣", "Alex", "Decides to buy shares."),
        ("2️⃣", "Broker", "Receives and routes his order according to the platform and market rules."),
        ("3️⃣", "Exchange / trading system", "Matches compatible orders, subject to rules and priority."),
        ("4️⃣", "Clearing system", "Determines and processes clearing obligations."),
        ("5️⃣", "Settlement system", "Completes the transfer of securities and funds under applicable rules."),
    ]

    for emoji, name, description in stages:
        with st.expander(f"{emoji} {name}"):
            st.write(description)

    st.subheader("9. Ecosystem simulator")

    st.write("""
    Select the participant responsible for each activity.
    """)

    questions = [
        {
            "q": "Who typically provides a platform through which an individual places a trade?",
            "options": ["Broker", "Company founder", "Taxpayer"],
            "correct": 0,
            "explanation": "A broker generally provides market access and receives or routes orders."
        },
        {
            "q": "Who oversees securities markets in India?",
            "options": ["SEBI", "A random investor", "A company customer"],
            "correct": 0,
            "explanation": "SEBI is India's principal securities-market regulator."
        },
        {
            "q": "What does a clearing and settlement system help do?",
            "options": [
                "Guarantee profits.",
                "Process obligations and complete the transfer of funds and securities.",
                "Choose every investor's stock."
            ],
            "correct": 1,
            "explanation": "Clearing and settlement infrastructure helps process obligations "
                          "and complete securities and funds transfers."
        }
    ]

    market_quiz("l20", questions)

    st.markdown("""
    ### 🎉 Chapter 5 completed!

    Alex now understands:

    - What the stock market is.
    - What a share represents.
    - Why companies issue shares.
    - IPOs and primary markets.
    - Secondary markets.
    - Capital gains and losses.
    - Dividends.
    - Retail and institutional investors.
    - Brokers and exchanges.
    - Market makers.
    - Regulators.
    - Clearing and settlement.

    **Next: Chapter 6 — Exploring Investments.**
    """)


# =========================================================
# REUSABLE QUIZ
# =========================================================

def market_quiz(quiz_id, questions):
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
