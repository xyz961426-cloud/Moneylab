
import streamlit as st
import plotly.graph_objects as go


def market_quiz(key, question, options, correct, explanation):
    choice = st.radio(question, options, key=key)

    if st.button("Check Answer", key=key + "_check"):
        if choice == correct:
            st.success("Correct! " + explanation)
        else:
            st.error(f"Incorrect. Correct answer: {correct}")
            st.info(explanation)


def show_chapter11():
    st.title("📈 Chapter 11: Financial Markets & Trading")
    st.caption("MoneyLab • Lessons 41–44")

    st.markdown("""
    ### Alex enters the financial markets

    Alex has learned about saving, investing, companies, bonds,
    mutual funds, banking and taxes.

    One day, he opens a market platform.

    He sees prices changing every second. Buy and sell buttons.
    Candlesticks. Bid prices. Ask prices. Leverage.

    He asks:

    **"How does this entire system actually work?"**

    This chapter will help Alex understand the mechanics before
    he makes decisions involving real money.
    """)

    lesson = st.selectbox(
        "Choose your lesson",
        [
            "Lesson 41 — How Financial Markets Work",
            "Lesson 42 — How Trading Orders Work",
            "Lesson 43 — Why Market Prices Move",
            "Lesson 44 — Leverage, Margin & Risk"
        ]
    )

    # LESSON 41
    if lesson.startswith("Lesson 41"):
        st.header("🏛️ How Financial Markets Work")

        st.markdown("""
        A financial market is a system where financial assets
        are bought and sold.

        These assets may include:

        - Stocks
        - Bonds
        - Currencies
        - Commodities
        - Derivatives

        ### Alex's first trade

        Alex wants to buy a share of a company.

        Another investor wants to sell that share.

        A market system helps their orders interact, subject
        to market rules and available liquidity.

        ### The market ecosystem
        """)

        st.markdown("""
        **Investor / Trader**

        ↓ places an order

        **Broker**

        ↓ routes or executes the order

        **Exchange / Market / Liquidity providers**

        ↓ facilitate transactions

        **Buyer and Seller**
        """)

        st.info(
            "Not every market uses a central exchange. Some markets, "
            "such as many currency and OTC derivative markets, "
            "operate through decentralised dealer networks."
        )

        st.subheader("Different financial markets")

        market_data = {
            "Market": [
                "Stock Market",
                "Bond Market",
                "Forex Market",
                "Commodity Market",
                "Derivatives Market"
            ],
            "What is traded": [
                "Company shares",
                "Debt securities",
                "Currencies",
                "Raw materials",
                "Contracts based on underlying assets"
            ],
            "Example": [
                "Reliance shares",
                "Government bonds",
                "EUR/USD",
                "Gold",
                "Futures and options"
            ]
        }

        st.table(market_data)

        st.subheader("Who participates in markets?")

        participants = {
            "Participant": [
                "Retail traders",
                "Investors",
                "Institutions",
                "Market makers",
                "Hedgers"
            ],
            "Typical role": [
                "Trade with personal capital",
                "Build positions for goals",
                "Manage large pools of capital",
                "Provide liquidity in certain markets",
                "Reduce exposure to price risk"
            ]
        }

        st.table(participants)

        st.markdown("""
        ### Trading vs investing

        | Trading | Investing |
        |---|---|
        | Often shorter holding periods | Often longer holding periods |
        | May focus on price movement | Often focuses on long-term value or goals |
        | May involve frequent transactions | Often involves fewer transactions |
        | Higher transaction costs may accumulate | Costs still matter, but turnover may be lower |

        These are tendencies, not strict definitions.
        """)

        market_quiz(
            "m41",
            "What does a broker generally do?",
            [
                "Guarantees profits",
                "Facilitates or routes financial orders",
                "Controls every market price",
                "Guarantees that every order executes"
            ],
            "Facilitates or routes financial orders",
            "A broker provides access to markets and may route, "
            "execute or facilitate orders according to its system."
        )

    # LESSON 42
    elif lesson.startswith("Lesson 42"):
        st.header("📝 How Trading Orders Work")

        st.markdown("""
        Alex now understands that markets connect buyers and sellers.

        But how does he actually enter a trade?

        He discovers that traders can use different order types.

        ### 1. Market order

        A market order seeks immediate execution at the best
        available prices, but the execution price is not guaranteed.

        ### 2. Limit order

        A buy limit sets the maximum price the buyer is willing
        to pay. A sell limit sets the minimum price the seller
        is willing to accept.

        A limit order may not execute.

        ### 3. Stop order

        A stop order is triggered when its specified stop price
        is reached. Depending on the order type and venue, it
        may become a market order or another order.

        A stop price does not guarantee the execution price.
        """)

        st.subheader("Interactive order simulator")

        current_price = st.slider(
            "Illustrative market price",
            min_value=50.0,
            max_value=200.0,
            value=100.0,
            step=0.5
        )

        order_type = st.selectbox(
            "Choose order type",
            ["Market Buy", "Buy Limit", "Sell Limit", "Buy Stop", "Sell Stop"]
        )

        target = st.number_input(
            "Order price / stop price",
            min_value=0.0,
            value=95.0,
            step=0.5
        )

        st.metric("Illustrative market price", f"{current_price:.2f}")

        if order_type == "Market Buy":
            st.info(
                "This order seeks to buy immediately at the "
                "best available ask price. The final execution "
                "price may differ."
            )

        elif order_type == "Buy Limit":
            if target >= current_price:
                st.info(
                    "A buy limit at or above the current market "
                    "may be immediately executable, depending on "
                    "the available ask price and order rules."
                )
            else:
                st.warning(
                    "This buy limit is below the current market. "
                    "It may execute if sellers offer at your limit "
                    "price or better, but execution is not guaranteed."
                )

        elif order_type == "Sell Limit":
            if target <= current_price:
                st.info(
                    "A sell limit at or below the current market "
                    "may be immediately executable, depending on "
                    "the available bid price and order rules."
                )
            else:
                st.warning(
                    "This sell limit is above the current market. "
                    "It may execute if buyers bid at your limit "
                    "price or better."
                )

        elif order_type == "Buy Stop":
            st.info(
                "A buy stop is generally triggered when the "
                "market reaches the specified stop price, "
                "subject to order rules."
            )

        elif order_type == "Sell Stop":
            st.info(
                "A sell stop is generally triggered when the "
                "market reaches the specified stop price, "
                "subject to order rules."
            )

        fig = go.Figure()

        fig.add_trace(
            go.Scatter(
                x=[0, 10],
                y=[current_price, current_price],
                mode="lines",
                name="Illustrative market price"
            )
        )

        fig.add_trace(
            go.Scatter(
                x=[0, 10],
                y=[target, target],
                mode="lines",
                name="Order / stop level",
                line=dict(dash="dash")
            )
        )

        fig.update_layout(
            title="Market Price vs Order Level",
            xaxis_title="Illustrative time",
            yaxis_title="Price",
            xaxis=dict(showticklabels=False)
        )

        st.plotly_chart(fig, use_container_width=True)

        st.subheader("Bid, Ask & Spread")

        bid = st.number_input(
            "Bid price",
            value=99.90,
            step=0.01,
            format="%.2f"
        )

        ask = st.number_input(
            "Ask price",
            value=100.10,
            step=0.01,
            format="%.2f"
        )

        spread = ask - bid

        st.metric("Spread", f"{spread:.2f}")

        if ask < bid:
            st.error(
                "The entered ask is below the bid. "
                "This is an unusual quote and may indicate "
                "inconsistent input."
            )
        else:
            st.write(
                f"Bid: {bid:.2f} | Ask: {ask:.2f}"
            )

            st.info(
                "Buyers generally transact against the ask when "
                "buying immediately, and sellers against the bid "
                "when selling immediately. Actual execution depends "
                "on market structure and order handling."
            )

        st.markdown("""
        ### Why spread matters

        The spread is the difference between the bid and ask.

        A wider spread can increase the cost of entering and
        exiting a position, especially when trading frequently
        or during less liquid periods.
        """)

        market_quiz(
            "m42",
            "What is a major difference between a market order "
            "and a limit order?",
            [
                "Market orders guarantee a price",
                "Limit orders guarantee execution",
                "Market orders seek execution while limit orders "
                "specify a price constraint",
                "Both always execute immediately"
            ],
            "Market orders seek execution while limit orders specify a price constraint",
            "Market orders prioritise execution, while limit "
            "orders impose a price condition and may not execute."
        )

    # LESSON 43
    elif lesson.startswith("Lesson 43"):
        st.header("📊 Why Market Prices Move")

        st.markdown("""
        Alex notices that gold, stocks and currencies move
        even when he isn't trading.

        Why?

        Prices emerge from the interaction of orders,
        expectations, liquidity and market conditions.

        ### 1. Supply and demand

        Buyers and sellers submit orders at different prices.

        When aggressive buying consumes available sell orders,
        transactions may occur at progressively higher prices.

        When aggressive selling consumes available buy orders,
        transactions may occur at progressively lower prices.

        ### 2. Liquidity

        Liquidity refers to how easily an asset can be traded
        without causing a large price impact.

        ### 3. Volatility

        Volatility describes the degree of price variation
        over a period.

        ### 4. News and expectations

        Markets may react to:

        - Economic data
        - Interest rate decisions
        - Company earnings
        - Geopolitical events
        - Changes in expectations
        """)

        st.subheader("Order book illustration")

        buy_orders = st.slider(
            "Illustrative buy-side order quantity",
            1,
            100,
            50
        )

        sell_orders = st.slider(
            "Illustrative sell-side order quantity",
            1,
            100,
            40
        )

        fig = go.Figure()

        fig.add_trace(
            go.Bar(
                x=["Buy-side interest", "Sell-side interest"],
                y=[buy_orders, sell_orders]
            )
        )

        fig.update_layout(
            title="Illustrative order interest",
            yaxis_title="Quantity (arbitrary units)"
        )

        st.plotly_chart(fig, use_container_width=True)

        st.markdown("""
        This is only an illustration of displayed interest.

        **It does not predict price direction.**

        Actual price movements depend on available orders,
        cancellations, new orders, market participants and
        execution dynamics.
        """)

        st.subheader("Price movement simulation")

        start_price = st.number_input(
            "Starting price",
            min_value=1.0,
            value=100.0,
            step=1.0
        )

        buying_pressure = st.slider(
            "Illustrative buying pressure",
            -100,
            100,
            20
        )

        liquidity = st.slider(
            "Illustrative liquidity",
            1,
            100,
            50
        )

        simulated_change = buying_pressure / liquidity

        simulated_price = start_price + simulated_change

        st.metric(
            "Illustrative simulated price",
            f"{simulated_price:.2f}"
        )

        st.caption(
            "This is a fictional mathematical model, not a real "
            "market model. It does not forecast prices."
        )

        st.markdown("""
        In this simplified simulation, the same pressure creates
        a larger numerical change when the liquidity parameter
        is lower.

        Real markets are more complex, and this relationship
        cannot be used as a trading forecast.
        """)

        market_quiz(
            "m43",
            "Why can a relatively small order sometimes cause "
            "a larger price movement?",
            [
                "Liquidity may be limited at available prices",
                "All traders must buy at once",
                "Price movements are guaranteed",
                "Every order changes the price by the same amount"
            ],
            "Liquidity may be limited at available prices",
            "When available liquidity is limited, an order may "
            "consume several price levels and create a larger "
            "price impact."
        )

    # LESSON 44
    elif lesson.startswith("Lesson 44"):
        st.header("⚠️ Leverage, Margin & Risk")

        st.markdown("""
        Alex discovers that a broker may allow him to control
        a position larger than his deposited capital.

        This is called leverage.

        Leverage increases exposure relative to capital.

        It can magnify gains and losses.

        ### What is leverage?

        Leverage is the ratio between the total position exposure
        and the capital used to support that exposure.

        ### What is margin?

        Margin is collateral required to open or maintain
        certain leveraged positions.

        Margin is not a fee. It is capital that may be exposed
        to losses and is subject to broker rules.
        """)

        st.subheader("Leverage simulator")

        capital = st.slider(
            "Capital / margin (₹)",
            min_value=1000,
            max_value=1000000,
            step=1000,
            value=10000
        )

        leverage = st.slider(
            "Leverage",
            min_value=1,
            max_value=200,
            value=20
        )

        movement = st.slider(
            "Price movement (%)",
            min_value=-100,
            max_value=100,
            value=-2
        )

        exposure = capital * leverage

        pnl = exposure * movement / 100

        remaining = capital + pnl

        col1, col2, col3 = st.columns(3)

        col1.metric(
            "Position exposure",
            f"₹{exposure:,.0f}"
        )

        col2.metric(
            "Illustrative P/L",
            f"₹{pnl:,.0f}"
        )

        col3.metric(
            "Remaining capital",
            f"₹{remaining:,.0f}"
        )

        fig = go.Figure(
            go.Bar(
                x=["Initial capital", "P/L", "Remaining capital"],
                y=[capital, pnl, remaining]
            )
        )

        fig.update_layout(
            title="Illustrative leveraged trade",
            yaxis_title="Amount (₹)"
        )

        st.plotly_chart(fig, use_container_width=True)

        st.warning(
            "This simulation excludes fees, spread, slippage, "
            "financing, margin requirements, liquidation and "
            "broker-specific rules. Remaining capital can be "
            "negative in this mathematical model, but real "
            "accounts may be closed earlier and loss protections "
            "vary by broker and jurisdiction."
        )

        st.subheader("Understand the exposure")

        st.write(
            f"Capital: ₹{capital:,.0f}"
        )

        st.write(
            f"Leverage: {leverage}x"
        )

        st.write(
            f"Exposure: ₹{exposure:,.0f}"
        )

        st.write(
            f"Illustrative price move: {movement}%"
        )

        st.write(
            f"Illustrative P/L: ₹{pnl:,.0f}"
        )

        st.markdown("""
        ### Why leverage is dangerous

        - Small price changes can create large gains or losses
          relative to deposited capital.
        - Margin requirements may change.
        - Liquidation may occur before you expect.
        - Stop orders may execute at worse prices during
          fast markets or gaps.
        - Fees and financing can reduce returns.

        ### Risk management concepts

        - Position sizing
        - Stop-loss planning
        - Maximum account drawdown
        - Risk per trade
        - Exposure across multiple positions
        - Understanding liquidation rules
        """)

        market_quiz(
            "m44",
            "What happens when leverage increases while "
            "position exposure increases relative to capital?",
            [
                "Risk automatically disappears",
                "A given price movement can have a larger effect "
                "on capital",
                "The trade cannot lose money",
                "Margin is no longer required"
            ],
            "A given price movement can have a larger effect on capital",
            "Greater exposure relative to capital magnifies "
            "the effect of price changes on your capital."
        )

    st.divider()

    st.markdown("""
    ### 🏆 Chapter 11 Complete

    Alex now understands the structure of markets, order types,
    bid and ask prices, liquidity, price movement and leverage.

    He has learned that markets are not simply buttons to buy
    and sell. They are systems of orders, risk, execution
    and uncertainty.

    **Next chapter: Risk, Psychology & Decision-Making**
    """)
