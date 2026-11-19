import streamlit as st
import streamlit.components.v1 as components

def show_lesson4():

    if "l4_story_scene" not in st.session_state:
        st.session_state.l4_story_scene = 0
        st.session_state.l4_story_cash = 30000
        st.session_state.l4_story_savings = 0
        st.session_state.l4_story_spent = 0
        st.session_state.l4_story_weekend = None
        st.session_state.l4_story_paid = set()
        st.session_state.l4_story_emergency = None

    cash = st.session_state.l4_story_cash
    savings = st.session_state.l4_story_savings
    scene = st.session_state.l4_story_scene

    st.markdown("""
    <style>
    .storybox {
        background: linear-gradient(135deg,#101d35,#203d65,#28577a);
        padding:25px;
        border-radius:20px;
        color:white;
        animation: fadein 1.2s ease-in-out;
        border:1px solid #42698b;
        margin-bottom:15px;
    }
    .character {
        font-size:60px;
        text-align:center;
        animation: float 2s infinite ease-in-out;
    }
    .dialogue {
        background:rgba(255,255,255,0.08);
        padding:16px;
        border-radius:14px;
        font-size:17px;
        margin-top:15px;
        line-height:1.7;
    }
    @keyframes float {
        0%,100% {transform:translateY(0);}
        50% {transform:translateY(-10px);}
    }
    @keyframes fadein {
        from {opacity:0;transform:translateY(20px);}
        to {opacity:1;transform:translateY(0);}
    }
    @keyframes pulse {
        0%,100% {opacity:1;}
        50% {opacity:0.6;}
    }
    .money {
        color:#7df0bb;
        font-size:28px;
        font-weight:bold;
        text-align:center;
        animation:pulse 2s infinite;
    }
    </style>
    """, unsafe_allow_html=True)

    st.title("💼 Your First Salary")
    st.caption("MoneyLab presents: A month that changes everything")

    st.markdown(
        f"### 💳 Cash: ₹{cash:,}  |  🏦 Savings: ₹{savings:,}"
    )

    # SCENE 1
    if scene == 0:

        components.html("""
        <div class="storybox">
        <div class="character">🏢</div>
        <h2 style="text-align:center;color:white;">6:02 PM — Payday</h2>
        <div class="dialogue">
        The office lights are slowly turning off.<br><br>
        You have just finished your first month at your new job.
        Your phone vibrates.
        </div>
        <div class="money">+ ₹30,000</div>
        <div class="dialogue">
        <b>Bank notification:</b><br>
        Salary credited successfully.<br><br>
        You stare at your phone. This is the first money
        you earned yourself.
        </div>
        </div>
        """, height=370)

        st.write("Your financial journey begins now.")

        if st.button("Continue →", use_container_width=True):
            st.session_state.l4_story_scene = 1
            st.rerun()

    # SCENE 2
    elif scene == 1:

        components.html("""
        <div class="storybox">
        <div class="character">📱</div>
        <h2 style="color:white;">7:15 PM — The Invitation</h2>
        <div class="dialogue">
        Your friend calls you.<br><br>
        <b>Friend:</b> "Hey! Your salary arrived?
        Let's go out this weekend.
        We've planned a great evening!"
        </div>
        <div class="dialogue">
        You know this weekend could cost money.
        But you also want to enjoy your first salary.
        </div>
        </div>
        """, height=300)

        st.markdown("### What do you decide?")

        col1, col2, col3 = st.columns(3)

        with col1:
            st.markdown("**Luxury**")
            st.caption("Expensive dinner + shopping")
            if st.button("Spend ₹4,000", use_container_width=True):
                if cash >= 4000:
                    st.session_state.l4_story_cash -= 4000
                    st.session_state.l4_story_spent += 4000
                    st.session_state.l4_story_weekend = "Luxury"
                    st.session_state.l4_story_scene = 2
                    st.rerun()

        with col2:
            st.markdown("**Balanced**")
            st.caption("Enjoy, but set a limit")
            if st.button("Spend ₹1,500", use_container_width=True):
                if cash >= 1500:
                    st.session_state.l4_story_cash -= 1500
                    st.session_state.l4_story_spent += 1500
                    st.session_state.l4_story_weekend = "Balanced"
                    st.session_state.l4_story_scene = 2
                    st.rerun()

        with col3:
            st.markdown("**Stay Home**")
            st.caption("Keep your money")
            if st.button("Spend ₹0", use_container_width=True):
                st.session_state.l4_story_weekend = "Stay Home"
                st.session_state.l4_story_scene = 2
                st.rerun()

    # SCENE 3
    elif scene == 2:

        components.html("""
        <div class="storybox">
        <div class="character">🏠</div>
        <h2 style="color:white;">Monday — Reality Arrives</h2>
        <div class="dialogue">
        The weekend is over.<br><br>
        You sit at your desk and open your banking app.
        Four payments are waiting for you.
        </div>
        <div class="dialogue">
        <b>Your monthly essentials:</b><br>
        Rent, food, transportation and utilities.
        </div>
        </div>
        """, height=300)

        st.markdown("### Pay your essential expenses")

        expenses = {
            "🏠 Rent": 8000,
            "🍲 Food": 4000,
            "🚌 Transport": 2000,
            "💡 Utilities": 1500
        }

        for name, amount in expenses.items():

            if name in st.session_state.l4_story_paid:
                st.success(f"{name} — ₹{amount:,} PAID")

            else:
                if st.button(
                    f"Pay {name} — ₹{amount:,}",
                    key=f"story_pay_{name}",
                    use_container_width=True
                ):

                    if cash >= amount:
                        st.session_state.l4_story_cash -= amount
                        st.session_state.l4_story_spent += amount
                        st.session_state.l4_story_paid.add(name)
                        st.rerun()
                    else:
                        st.error("Not enough cash!")

        if len(st.session_state.l4_story_paid) == 4:

            st.success("All essential bills have been paid.")

            if st.button("Continue →", use_container_width=True):
                st.session_state.l4_story_scene = 3
                st.rerun()

    # SCENE 4
    elif scene == 3:

        components.html("""
        <div class="storybox">
        <div class="character">📱💥</div>
        <h2 style="color:white;">Thursday — Unexpected Trouble</h2>
        <div class="dialogue">
        Your phone falls on the floor.<br><br>
        The screen is completely broken.
        </div>
        <div class="dialogue">
        <b>Repair shop:</b><br>
        "The repair will cost ₹2,000."
        </div>
        <div class="dialogue">
        You weren't planning for this expense.
        What will you do?
        </div>
        </div>
        """, height=330)

        if st.session_state.l4_story_emergency is None:

            col1, col2 = st.columns(2)

            with col1:
                if st.button("Pay ₹2,000", use_container_width=True):
                    if cash >= 2000:
                        st.session_state.l4_story_cash -= 2000
                        st.session_state.l4_story_spent += 2000
                        st.session_state.l4_story_emergency = "Repaired"
                        st.rerun()
                    else:
                        st.error("You don't have enough cash.")

            with col2:
                if st.button("Delay Repair", use_container_width=True):
                    st.session_state.l4_story_emergency = "Delayed"
                    st.rerun()

        else:

            if st.session_state.l4_story_emergency == "Repaired":
                st.success("Your phone is repaired.")

            else:
                st.warning("You delayed the repair.")

            if st.button("Continue →", use_container_width=True):
                st.session_state.l4_story_scene = 4
                st.rerun()

    # SCENE 5
    elif scene == 4:

        components.html("""
        <div class="storybox">
        <div class="character">🌙</div>
        <h2 style="color:white;">The End of the Month</h2>
        <div class="dialogue">
        It's the last day of the month.<br><br>
        You open your bank account and look at
        what remains.
        </div>
        <div class="dialogue">
        One month ago, you had no experience
        managing a salary.<br><br>
        Now you have made real financial decisions.
        </div>
        </div>
        """, height=300)

        st.markdown("### 💰 Protect Your Remaining Money")

        if cash > 0:

            save = st.number_input(
                "Move money into savings",
                min_value=0,
                max_value=cash,
                step=500,
                key="story_final_save"
            )

            if st.button("Transfer to Savings", use_container_width=True):

                st.session_state.l4_story_cash -= save
                st.session_state.l4_story_savings += save
                st.rerun()

        st.markdown("---")

        st.markdown("### 📊 Your Month")

        col1, col2 = st.columns(2)

        col1.metric("Cash Remaining", f"₹{cash:,}")
        col2.metric("Savings", f"₹{savings:,}")

        st.metric("Total Wealth", f"₹{cash + savings:,}")

        weekend = st.session_state.l4_story_weekend
        st.write(f"**Weekend decision:** {weekend}")

        st.write(
            f"**Essential bills paid:** "
            f"{len(st.session_state.l4_story_paid)}/4"
        )

        st.write(
            f"**Phone emergency:** "
            f"{st.session_state.l4_story_emergency}"
        )

        st.markdown("### 🧠 The Lesson")

        st.markdown("""
        - Your salary is a resource, not unlimited money.
        - Every purchase has an opportunity cost.
        - Essential expenses need planning.
        - Emergencies can happen at any time.
        - Saving means keeping money for future needs.
        - A budget gives you control, not restriction.
        """)

        if cash + savings >= 15000:
            st.success(
                "You protected a strong portion of your salary. "
                "Your decisions helped you build financial security."
            )

        elif cash + savings >= 5000:
            st.info(
                "You managed some money well. "
                "Next month, try planning your expenses earlier."
            )

        else:
            st.warning(
                "Most of your salary has been used. "
                "Try building a budget before spending next month."
            )

        if st.button("🔄 Play the Story Again", use_container_width=True):

            for key in [
                "l4_story_scene",
                "l4_story_cash",
                "l4_story_savings",
                "l4_story_spent",
                "l4_story_weekend",
                "l4_story_paid",
                "l4_story_emergency"
            ]:
                del st.session_state[key]

            st.rerun()
