import streamlit as st
import streamlit.components.v1 as components

def show_lesson4():

    st.title("💰 Lesson 4: The Payday Story")
    st.caption("Learn Money by Living It")

    # Story state
    if "l4_story_scene" not in st.session_state:
        st.session_state.l4_story_scene = 0

    if "l4_story_weekend" not in st.session_state:
        st.session_state.l4_story_weekend = None

    if "l4_story_emergency" not in st.session_state:
        st.session_state.l4_story_emergency = None

    scene = st.session_state.l4_story_scene

    # Back button
    if scene > 0:
        if st.button("← Back"):
            st.session_state.l4_story_scene -= 1
            st.rerun()

    # SCENE 1 - PAYDAY
    if scene == 0:

        components.html("""
        <div style="height:300px;background:linear-gradient(#10162e,#253b70);
        border-radius:20px;position:relative;overflow:hidden;color:white;
        font-family:sans-serif;text-align:center;">

        <div style="font-size:60px;padding-top:20px;
        animation:moon 3s infinite alternate;">🌙</div>

        <div style="font-size:25px;margin-top:10px;">
        Payday has arrived!
        </div>

        <div style="font-size:50px;animation:money 2s infinite;">
        💸
        </div>

        <div style="font-size:30px;color:#7CFFB2;">
        + ₹30,000
        </div>

        <div style="margin-top:15px;">
        Your salary is in your bank account.
        </div>

        <style>
        @keyframes money {
          0% {transform:translateY(-10px);}
          50% {transform:translateY(15px);}
          100% {transform:translateY(-10px);}
        }
        @keyframes moon {
          from {transform:scale(0.9);}
          to {transform:scale(1.1);}
        }
        </style>
        </div>
        """, height=320)

        st.write("You received your salary. What will you do with your money this month?")

        if st.button("Start My Financial Journey →"):
            st.session_state.l4_story_scene = 1
            st.rerun()

    # SCENE 2 - WEEKEND
    elif scene == 1:

        st.subheader("🛍️ Scene 2: The Weekend")

        st.write("Your friends invite you to go shopping and have fun.")

        st.markdown("### Choose your weekend plan")

        col1, col2, col3 = st.columns(3)

        with col1:
            st.markdown("### 🛒")
            st.write("Luxury")
            st.write("Spend ₹4,000")
            if st.button("Luxury"):
                st.session_state.l4_story_weekend = 4000
                st.session_state.l4_story_scene = 2
                st.rerun()

        with col2:
            st.markdown("### 🍕")
            st.write("Balanced")
            st.write("Spend ₹1,500")
            if st.button("Balanced"):
                st.session_state.l4_story_weekend = 1500
                st.session_state.l4_story_scene = 2
                st.rerun()

        with col3:
            st.markdown("### 🏠")
            st.write("Stay Home")
            st.write("Spend ₹0")
            if st.button("Stay Home"):
                st.session_state.l4_story_weekend = 0
                st.session_state.l4_story_scene = 2
                st.rerun()

    # SCENE 3 - EXPENSES
    elif scene == 2:

        st.subheader("🏠 Scene 3: Your Monthly Bills")

        components.html("""
        <div style="background:linear-gradient(120deg,#172554,#1e40af);
        padding:20px;border-radius:15px;color:white;font-family:sans-serif;">
        <div style="font-size:28px;text-align:center;">📃 Monthly Expenses</div>
        <div style="font-size:20px;margin-top:15px;line-height:2;">
        🏠 Rent: ₹8,000<br>
        🍲 Food: ₹4,000<br>
        🚌 Transport: ₹2,000<br>
        💡 Utilities: ₹1,500
        </div>
        </div>
        """, height=280)

        st.write("These expenses are necessary. You must pay them.")

        if st.button("Pay Bills & Continue →"):
            st.session_state.l4_story_scene = 3
            st.rerun()

    # SCENE 4 - EMERGENCY
    elif scene == 3:

        st.subheader("📱 Scene 4: Unexpected Problem!")

        components.html("""
        <div style="background:linear-gradient(135deg,#7f1d1d,#b91c1c);
        color:white;padding:25px;border-radius:20px;text-align:center;
        font-family:sans-serif;">
        <div style="font-size:65px;animation:shake 1s infinite;">📱</div>
        <h2>Your phone is broken!</h2>
        <p>A repair will cost ₹2,000.</p>
        <style>
        @keyframes shake {
          0% {transform:rotate(0deg);}
          25% {transform:rotate(8deg);}
          50% {transform:rotate(-8deg);}
          75% {transform:rotate(8deg);}
          100% {transform:rotate(0deg);}
        }
        </style>
        </div>
        """, height=250)

        st.write("You have two options.")

        col1, col2 = st.columns(2)

        with col1:
            if st.button("🔧 Repair Now (₹2,000)"):
                st.session_state.l4_story_emergency = 2000
                st.session_state.l4_story_scene = 4
                st.rerun()

        with col2:
            if st.button("⏳ Delay Repair (₹0)"):
                st.session_state.l4_story_emergency = 0
                st.session_state.l4_story_scene = 4
                st.rerun()

    # SCENE 5 - RESULTS
    elif scene == 4:

        st.subheader("📊 Scene 5: Your Financial Results")

        salary = 30000
        weekend = st.session_state.l4_story_weekend or 0
        bills = 15500
        emergency = st.session_state.l4_story_emergency or 0

        remaining = salary - weekend - bills - emergency

        st.markdown("### 💳 Money Breakdown")

        st.write(f"💰 Salary: ₹{salary:,}")
        st.write(f"🛍️ Weekend spending: ₹{weekend:,}")
        st.write(f"🏠 Monthly bills: ₹{bills:,}")
        st.write(f"📱 Phone repair: ₹{emergency:,}")

        st.divider()

        st.markdown(f"### <span style='color:green'>Remaining: ₹{remaining:,}</span>",
                    unsafe_allow_html=True)

        components.html("""
        <div style="text-align:center;background:linear-gradient(135deg,#064e3b,#059669);
        padding:25px;border-radius:20px;color:white;font-family:sans-serif;">
        <div style="font-size:60px;animation:grow 2s infinite alternate;">🌱</div>
        <h2>Every financial decision matters!</h2>
        <style>
        @keyframes grow {
          from {transform:scale(0.8);}
          to {transform:scale(1.2);}
        }
        </style>
        </div>
        """, height=220)

        st.markdown("### 🧠 What did you learn?")
        st.write("""
        - Spending decisions affect your remaining money.
        - Essential expenses should be planned first.
        - Unexpected expenses can happen at any time.
        - Saving money gives you financial security.
        """)

        if st.button("🔄 Restart Story"):
            st.session_state.l4_story_scene = 0
            st.session_state.l4_story_weekend = None
            st.session_state.l4_story_emergency = None
            st.rerun()

    st.divider()
    st.caption("MoneyLab | Learn Money by Living It")
