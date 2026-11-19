
import streamlit as st
import streamlit.components.v1 as components

def show_lesson4():

    st.title("💰 Lesson 4: The Payday Story")
    st.caption("Learn Money by Living It")

    if "l4_scene" not in st.session_state:
        st.session_state.l4_scene = 0
    if "l4_weekend" not in st.session_state:
        st.session_state.l4_weekend = None
    if "l4_emergency" not in st.session_state:
        st.session_state.l4_emergency = None

    scene = st.session_state.l4_scene

    if scene > 0:
        if st.button("← Back"):
            st.session_state.l4_scene -= 1
            st.rerun()

    # SCENE 0: PAYDAY
    if scene == 0:

        components.html("""
        <div style="height:280px;background:linear-gradient(#10162e,#253b70);
        border-radius:20px;text-align:center;color:white;padding:20px;
        font-family:sans-serif;">
        <div style="font-size:65px;animation:moon 2s infinite alternate;">🌙</div>
        <h2>PAYDAY!</h2>
        <div style="font-size:55px;animation:money 2s infinite;">💸</div>
        <h1 style="color:#7CFFB2;">+ ₹30,000</h1>
        <p>Your salary has arrived!</p>
        <style>
        @keyframes money {
        0% {transform:translateY(-10px)}
        50% {transform:translateY(15px)}
        100% {transform:translateY(-10px)}
        }
        @keyframes moon {
        from {transform:scale(.9)}
        to {transform:scale(1.1)}
        }
        </style>
        </div>
        """, height=320)

        st.write("You have received ₹30,000. A new month begins.")

        if st.button("Start Story →"):
            st.session_state.l4_scene = 1
            st.rerun()

    # SCENE 1: CHOICE
    elif scene == 1:

        st.subheader("🛍️ The Weekend")

        st.write("Your friends invite you to spend the weekend together.")

        col1, col2, col3 = st.columns(3)

        with col1:
            st.markdown("### 🛒 Luxury")
            st.write("Spend ₹4,000")
            if st.button("Choose Luxury"):
                st.session_state.l4_weekend = 4000
                st.session_state.l4_scene = 2
                st.rerun()

        with col2:
            st.markdown("### 🍕 Balanced")
            st.write("Spend ₹1,500")
            if st.button("Choose Balanced"):
                st.session_state.l4_weekend = 1500
                st.session_state.l4_scene = 2
                st.rerun()

        with col3:
            st.markdown("### 🏠 Home")
            st.write("Spend ₹0")
            if st.button("Stay Home"):
                st.session_state.l4_weekend = 0
                st.session_state.l4_scene = 2
                st.rerun()

    # SCENE 2: UNIQUE CHOICE STORY
    elif scene == 2:

        choice = st.session_state.l4_weekend

        if choice == 4000:

            components.html("""
            <div style="background:linear-gradient(135deg,#7c2d12,#ea580c);
            padding:25px;border-radius:20px;text-align:center;color:white;
            font-family:sans-serif;">
            <div style="font-size:70px;animation:pop 1s infinite alternate;">🛍️</div>
            <h2>Luxury Weekend!</h2>
            <p>You bought new clothes, enjoyed a fancy dinner
            and had an amazing time.</p>
            <h2>Spent ₹4,000</h2>
            <style>
            @keyframes pop {
            from {transform:scale(.9)}
            to {transform:scale(1.1)}
            }
            </style>
            </div>
            """, height=280)

            st.write("Your friends had a great time. But you spent quite a lot.")
            st.info("Your fun came at a higher financial cost.")

        elif choice == 1500:

            components.html("""
            <div style="background:linear-gradient(135deg,#065f46,#10b981);
            padding:25px;border-radius:20px;text-align:center;color:white;
            font-family:sans-serif;">
            <div style="font-size:70px;animation:pop 1s infinite alternate;">🍕</div>
            <h2>Balanced Weekend!</h2>
            <p>You enjoyed food, movies and time with friends
            without overspending.</p>
            <h2>Spent ₹1,500</h2>
            <style>
            @keyframes pop {
            from {transform:scale(.9)}
            to {transform:scale(1.1)}
            }
            </style>
            </div>
            """, height=280)

            st.write("You enjoyed yourself and kept your spending under control.")
            st.success("Enjoyment and financial discipline can coexist.")

        else:

            components.html("""
            <div style="background:linear-gradient(135deg,#1e3a8a,#60a5fa);
            padding:25px;border-radius:20px;text-align:center;color:white;
            font-family:sans-serif;">
            <div style="font-size:70px;animation:pop 1s infinite alternate;">🏠</div>
            <h2>Quiet Weekend!</h2>
            <p>You stayed home, cooked food and watched a movie.</p>
            <h2>Spent ₹0</h2>
            <style>
            @keyframes pop {
            from {transform:scale(.9)}
            to {transform:scale(1.1)}
            }
            </style>
            </div>
            """, height=280)

            st.write("You enjoyed a peaceful weekend without spending money.")
            st.success("You kept all your weekend money.")

        if st.button("Continue to Monthly Bills →"):
            st.session_state.l4_scene = 3
            st.rerun()

    # SCENE 3: BILLS
    elif scene == 3:

        st.subheader("🏠 Monthly Bills")

        components.html("""
        <div style="background:linear-gradient(120deg,#172554,#1e40af);
        padding:25px;border-radius:20px;color:white;font-family:sans-serif;">
        <h2 style="text-align:center;">📃 Your Bills</h2>
        <div style="font-size:22px;line-height:2;">
        🏠 Rent: ₹8,000<br>
        🍲 Food: ₹4,000<br>
        🚌 Transport: ₹2,000<br>
        💡 Utilities: ₹1,500
        </div>
        </div>
        """, height=280)

        st.write("These expenses are necessary.")

        if st.button("Pay Bills →"):
            st.session_state.l4_scene = 4
            st.rerun()

    # SCENE 4: EMERGENCY
    elif scene == 4:

        st.subheader("📱 Unexpected Problem!")

        components.html("""
        <div style="background:linear-gradient(135deg,#7f1d1d,#b91c1c);
        padding:25px;border-radius:20px;color:white;text-align:center;
        font-family:sans-serif;">
        <div style="font-size:70px;animation:shake 1s infinite;">📱</div>
        <h2>Your phone is broken!</h2>
        <p>Repair cost: ₹2,000</p>
        <style>
        @keyframes shake {
        0% {transform:rotate(0)}
        25% {transform:rotate(8deg)}
        50% {transform:rotate(-8deg)}
        75% {transform:rotate(8deg)}
        100% {transform:rotate(0)}
        }
        </style>
        </div>
        """, height=250)

        st.write("Your phone suddenly stops working.")

        col1, col2 = st.columns(2)

        with col1:
            if st.button("🔧 Repair Phone"):
                st.session_state.l4_emergency = 2000
                st.session_state.l4_scene = 5
                st.rerun()

        with col2:
            if st.button("⏳ Delay Repair"):
                st.session_state.l4_emergency = 0
                st.session_state.l4_scene = 5
                st.rerun()

    # SCENE 5: RESULTS
    elif scene == 5:

        st.subheader("📊 Your Financial Results")

        salary = 30000
        weekend = st.session_state.l4_weekend
        bills = 15500
        emergency = st.session_state.l4_emergency

        remaining = salary - weekend - bills - emergency

        st.write(f"💰 Salary: ₹{salary:,}")
        st.write(f"🛍️ Weekend spending: ₹{weekend:,}")
        st.write(f"🏠 Bills: ₹{bills:,}")
        st.write(f"📱 Repair: ₹{emergency:,}")

        st.divider()

        st.markdown(f"## 💵 Remaining Money: ₹{remaining:,}")

        components.html("""
        <div style="background:linear-gradient(135deg,#064e3b,#059669);
        padding:25px;border-radius:20px;color:white;text-align:center;
        font-family:sans-serif;">
        <div style="font-size:70px;animation:grow 2s infinite alternate;">🌱</div>
        <h2>Your Financial Future</h2>
        <p>Every decision changes your financial situation.</p>
        <style>
        @keyframes grow {
        from {transform:scale(.8)}
        to {transform:scale(1.2)}
        }
        </style>
        </div>
        """, height=220)

        st.markdown("### 🧠 What You Learned")
        st.write("""
        - Spending choices affect your future.
        - Essential expenses must be planned.
        - Emergencies can happen anytime.
        - Saving money gives you security.
        """)

        if st.button("🔄 Play Again"):
            st.session_state.l4_scene = 0
            st.session_state.l4_weekend = None
            st.session_state.l4_emergency = None
            st.rerun()

    st.divider()
    st.caption("MoneyLab | Learn Money by Living It")
