
import streamlit as st
import streamlit.components.v1 as components

def lesson1():

    st.title("📚 Chapter 1 — How Money Works")
    st.subheader("Lesson 1: What Is Money?")

    if "l1_step" not in st.session_state:
        st.session_state.l1_step = 0

    step = st.session_state.l1_step

    def animation(html):
        components.html(html, height=270)

    def next_step():
        st.session_state.l1_step += 1
        st.rerun()

    def back_step():
        st.session_state.l1_step -= 1
        st.rerun()

    # ---------------- SCENE 0 ----------------

    if step == 0:

        animation("""
        <div style="height:250px;background:linear-gradient(135deg,#10243e,#2563eb);
        border-radius:20px;display:flex;align-items:center;justify-content:center;
        flex-direction:column;color:white;font-family:sans-serif;overflow:hidden">

        <div style="font-size:70px;animation:float 2s infinite ease-in-out">💰</div>
        <h2>Money moves the world!</h2>
        <p>But what exactly is money?</p>

        <style>
        @keyframes float {
        0%,100% {transform:translateY(0)}
        50% {transform:translateY(-18px)}
        }
        </style>
        </div>
        """)

        st.write("""
        Imagine waking up tomorrow in a world where money doesn't exist.

        How would you buy food, clothes or a phone?

        Let's discover why money exists and how it works.
        """)

        if st.button("🚀 Start Learning", key="l1_start"):
            next_step()

    # ---------------- SCENE 1 ----------------

    elif step == 1:

        st.header("🧺 Before money: The barter system")

        animation("""
        <div style="height:250px;background:#fef3c7;border-radius:20px;
        display:flex;align-items:center;justify-content:space-around;
        font-family:sans-serif">

        <div style="text-align:center;animation:float 2s infinite">
        <div style="font-size:70px">🍎</div>
        <b>Apple seller</b>
        </div>

        <div style="font-size:45px;animation:pulse 1s infinite">↔️</div>

        <div style="text-align:center;animation:float 2s infinite">
        <div style="font-size:70px">🥖</div>
        <b>Bread seller</b>
        </div>

        <style>
        @keyframes float {
        0%,100% {transform:translateY(0)}
        50% {transform:translateY(-10px)}
        }
        @keyframes pulse {
        0%,100% {transform:scale(1)}
        50% {transform:scale(1.2)}
        }
        </style>
        </div>
        """)

        st.write("""
        Long ago, people often exchanged goods directly.

        This was called **barter**.
        """)

        st.markdown("""
        - A farmer could exchange wheat for clothes.
        - A fisherman could exchange fish for vegetables.
        """)

        st.warning("""
        The problem: Both people had to want what the other person had.

        Imagine you have apples but want bread. The baker may not want apples!
        """)

        st.markdown("### 🤔 Why was barter difficult?")

        answer = st.radio(
            "Choose the biggest problem:",
            [
                "People could not produce goods",
                "Both people needed to agree on what to exchange",
                "Goods had no value"
            ],
            key="l1_barter"
        )

        if st.button("Check", key="l1_barter_check"):
            if answer == "Both people needed to agree on what to exchange":
                st.success("Correct! This problem made trading difficult.")
            else:
                st.error("Think about what happens if the baker doesn't want your apples.")

        if st.button("Next ➡️", key="l1_next1"):
            next_step()

    # ---------------- SCENE 2 ----------------

    elif step == 2:

        st.header("💵 Money solves the problem")

        animation("""
        <div style="height:250px;background:linear-gradient(135deg,#dcfce7,#bbf7d0);
        border-radius:20px;display:flex;align-items:center;
        justify-content:center;font-family:sans-serif">

        <div style="text-align:center">
        <div style="font-size:80px;animation:float 2s infinite">💵</div>
        <h2 style="color:#166534">Money!</h2>
        <p>Buy what you need without barter.</p>
        </div>

        <style>
        @keyframes float {
        0%,100% {transform:translateY(0)}
        50% {transform:translateY(-15px)}
        }
        </style>
        </div>
        """)

        st.write("""
        Money makes exchange easier.

        You can sell something, receive money, and use that money
        to buy something from someone else.
        """)

        st.markdown("""
        **Example:**

        1. A farmer sells vegetables and receives ₹500.
        2. The farmer uses ₹500 to buy shoes.
        3. The shoe seller can use that money to buy something else.
        """)

        st.info("Money connects buyers and sellers.")

        if st.button("Next ➡️", key="l1_next2"):
            next_step()

    # ---------------- SCENE 3 ----------------

    elif step == 3:

        st.header("1️⃣ Medium of Exchange")

        animation("""
        <div style="height:250px;background:#dbeafe;border-radius:20px;
        display:flex;align-items:center;justify-content:space-around;
        font-family:sans-serif">

        <div style="text-align:center">
        <div style="font-size:65px">🧑</div>
        <p>Customer</p>
        </div>

        <div style="text-align:center;animation:pulse 1.5s infinite">
        <div style="font-size:55px">💵➡️</div>
        </div>

        <div style="text-align:center">
        <div style="font-size:65px">🏪</div>
        <p>Shop</p>
        </div>

        <style>
        @keyframes pulse {
        0%,100% {transform:scale(1)}
        50% {transform:scale(1.15)}
        }
        </style>
        </div>
        """)

        st.write("""
        Money is used to buy and sell goods and services.

        It makes exchange easier because sellers generally accept money
        instead of needing a specific product from you.
        """)

        st.success("Example: You pay ₹100 for a meal.")

        if st.button("Next ➡️", key="l1_next3"):
            next_step()

    # ---------------- SCENE 4 ----------------

    elif step == 4:

        st.header("2️⃣ Store of Value")

        animation("""
        <div style="height:250px;background:#fef9c3;border-radius:20px;
        display:flex;align-items:center;justify-content:center;
        flex-direction:column">

        <div style="font-size:65px;animation:float 2s infinite">🐷</div>
        <div style="font-size:45px">🪙 🪙 🪙</div>
        <h3>Save money for the future!</h3>

        <style>
        @keyframes float {
        0%,100% {transform:translateY(0)}
        50% {transform:translateY(-12px)}
        }
        </style>
        </div>
        """)

        st.write("""
        Money allows you to save purchasing power for future use.

        You don't have to spend all your money today.
        You can save some for tomorrow.
        """)

        st.markdown("### 💡 Example")

        st.write("""
        You save ₹1,000 today.

        Later, you can use that money to buy something you need.
        """)

        st.warning("""
        But inflation can reduce what your money can buy over time.
        Money is not a perfect store of value.
        """)

        if st.button("Next ➡️", key="l1_next4"):
            next_step()

    # ---------------- SCENE 5 ----------------

    elif step == 5:

        st.header("3️⃣ Unit of Account")

        animation("""
        <div style="height:250px;background:#ede9fe;border-radius:20px;
        display:flex;align-items:center;justify-content:space-around;
        font-family:sans-serif">

        <div style="text-align:center">
        <div style="font-size:65px">📕</div>
        <b>Book</b>
        <h3>₹500</h3>
        </div>

        <div style="font-size:40px">VS</div>

        <div style="text-align:center">
        <div style="font-size:65px">🖊️</div>
        <b>Pen</b>
        <h3>₹20</h3>
        </div>
        </div>
        """)

        st.write("""
        Money gives us a common unit for measuring the value of goods
        and services.

        It helps us compare prices.
        """)

        st.info("""
        A book costs ₹500.

        A pen costs ₹20.

        Because both prices are measured in rupees, we can compare them.
        """)

        if st.button("Next ➡️", key="l1_next5"):
            next_step()

    # ---------------- SCENE 6 ----------------

    elif step == 6:

        st.header("🎮 Try it yourself!")

        st.write("Imagine you have ₹1,000.")

        st.markdown("### What would you do with your money?")

        choice = st.radio(
            "Choose:",
            [
                "Spend all ₹1,000 today",
                "Save ₹500 and spend ₹500",
                "Save all ₹1,000"
            ],
            key="l1_decision"
        )

        if st.button("See My Decision", key="l1_decision_check"):

            if choice == "Spend all ₹1,000 today":
                st.warning("""
                You enjoyed spending today, but you have nothing left
                for future expenses or emergencies.
                """)

            elif choice == "Save ₹500 and spend ₹500":
                st.success("""
                Balanced decision! You enjoyed some spending while keeping
                money for future needs.
                """)

            else:
                st.info("""
                You kept all your money for the future.
                Saving is useful, but spending on necessary things is also
                part of a healthy financial life.
                """)

        if st.button("Next ➡️", key="l1_next6"):
            next_step()

    # ---------------- SCENE 7 ----------------

    elif step == 7:

        st.header("📈 Inflation: Why money can lose purchasing power")

        animation("""
        <div style="height:250px;background:#ffedd5;border-radius:20px;
        display:flex;align-items:center;justify-content:center;
        flex-direction:column;font-family:sans-serif">

        <div style="font-size:65px;animation:pulse 2s infinite">🛒</div>
        <h3>Prices can rise over time!</h3>
        <p>Same money • Fewer goods</p>

        <style>
        @keyframes pulse {
        0%,100% {transform:scale(1)}
        50% {transform:scale(1.1)}
        }
        </style>
        </div>
        """)

        st.write("""
        Inflation means the general price level of goods and services rises
        over time.

        If prices rise, the same amount of money may buy fewer things.
        """)

        price = st.slider(
            "Imagine a product costs this much today:",
            100, 1000, 100, 100,
            key="l1_price"
        )

        inflation = st.slider(
            "Illustrative yearly inflation:",
            0, 20, 5,
            key="l1_inflation"
        )

        years = st.slider(
            "Years in the future:",
            1, 20, 5,
            key="l1_years"
        )

        future_price = price * (1 + inflation / 100) ** years

        st.metric(
            "Illustrative future price",
            f"₹{future_price:,.2f}"
        )

        st.caption("This is a mathematical illustration, not a forecast.")

        if st.button("Next ➡️", key="l1_next7"):
            next_step()

    # ---------------- SCENE 8 ----------------

    elif step == 8:

        st.header("🧠 Knowledge Check")

        animation("""
        <div style="height:200px;background:linear-gradient(135deg,#d1fae5,#a7f3d0);
        border-radius:20px;display:flex;align-items:center;
        justify-content:center;flex-direction:column">

        <div style="font-size:70px;animation:float 2s infinite">🧠</div>
        <h2>Test your knowledge!</h2>

        <style>
        @keyframes float {
        0%,100% {transform:translateY(0)}
        50% {transform:translateY(-10px)}
        }
        </style>
        </div>
        """)

        question = st.radio(
            "Which is one of the main functions of money?",
            [
                "Money automatically creates wealth",
                "Money acts as a medium of exchange",
                "Money eliminates all financial risk",
                "Money guarantees profits"
            ],
            key="lesson1_question"
        )

        if st.button("Check Answer", key="lesson1_check"):

            if question == "Money acts as a medium of exchange":
                st.session_state.l1_passed = True
                st.success("🎉 Correct! Money makes exchanging goods and services easier.")
            else:
                st.session_state.l1_passed = False
                st.error("Not quite! Think about how money helps people buy and sell.")

        if st.session_state.get("l1_passed", False):

            st.markdown("---")
            st.success("You passed the knowledge check!")

            if st.button("🏁 Complete Lesson 1", key="l1_complete"):
                st.session_state.l1_step = 9
                st.rerun()

    # ---------------- COMPLETION ----------------

    elif step == 9:

        st.balloons()

        animation("""
        <div style="height:250px;background:linear-gradient(135deg,#14532d,#16a34a);
        border-radius:20px;display:flex;align-items:center;
        justify-content:center;flex-direction:column;color:white">

        <div style="font-size:85px;animation:float 2s infinite">🎓</div>
        <h1>Lesson Completed!</h1>
        <p>You understand the basics of money.</p>

        <style>
        @keyframes float {
        0%,100% {transform:translateY(0)}
        50% {transform:translateY(-12px)}
        }
        </style>
        </div>
        """)

        st.markdown("## 🎉 Congratulations!")

        st.write("""
        You learned:

        - Why barter was difficult.
        - Why money exists.
        - Medium of exchange.
        - Store of value.
        - Unit of account.
        - How inflation affects purchasing power.
        """)

        st.markdown("---")

        st.markdown("## 🔓 Next Lesson")

        st.markdown("""
        ### Lesson 2 — Your next step

        Continue your journey and learn the next financial concept.
        """)

        if st.button("➡️ Continue to Lesson 2", key="l1_to_l2"):

            st.session_state.l1_step = 0

            if "page" in st.session_state:
                st.session_state.page = "Lesson 2"

            st.success("Select Lesson 2 if the app doesn't navigate automatically.")

            st.rerun()

    # ---------------- NAVIGATION ----------------

    if step > 0 and step < 9:

        st.markdown("---")

        if st.button("⬅️ Previous", key=f"l1_back_{step}"):
            back_step()

    st.caption("MoneyLab • Chapter 1 • Lesson 1")
