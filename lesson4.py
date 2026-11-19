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

    st.title("💼 Your First Salary")
    st.caption("MoneyLab | Learn Money by Living It")

    # SCENE 1 - ANIMATED PAYDAY
    if scene == 0:

        components.html("""
        <style>
        * {box-sizing:border-box;}
        body {margin:0;}

        .stage {
            height:370px;
            overflow:hidden;
            position:relative;
            border-radius:20px;
            background:linear-gradient(180deg,#10213e,#244e72);
            color:white;
            font-family:Arial,sans-serif;
        }

        .stars {
            position:absolute;
            width:100%;
            height:100%;
            background-image:
            radial-gradient(white 1px,transparent 1px),
            radial-gradient(#9fd8ff 1px,transparent 1px);
            background-size:45px 45px,80px 80px;
            animation:stars 12s linear infinite;
            opacity:.5;
        }

        .moon {
            position:absolute;
            right:35px;
            top:25px;
            width:55px;
            height:55px;
            background:#fff2c2;
            border-radius:50%;
            box-shadow:0 0 40px #fff2c2;
        }

        .office {
            position:absolute;
            bottom:0;
            width:100%;
            height:100px;
            background:#13243c;
            border-top:4px solid #4d7394;
        }

        .window {
            position:absolute;
            bottom:100px;
            left:15%;
            width:70%;
            height:125px;
            background:linear-gradient(135deg,#274d70,#16314d);
            border:5px solid #6687a3;
            border-radius:8px;
        }

        .window:before {
            content:"";
            position:absolute;
            height:100%;
            width:4px;
            background:#6687a3;
            left:50%;
        }

        .window:after {
            content:"";
            position:absolute;
            height:4px;
            width:100%;
            background:#6687a3;
            top:50%;
        }

        .person {
            position:absolute;
            bottom:15px;
            left:-70px;
            font-size:60px;
            animation:walk 5s forwards;
            z-index:5;
        }

        .phone {
            position:absolute;
            top:85px;
            left:50%;
            transform:translateX(-50%) scale(.5);
            opacity:0;
            width:85%;
            max-width:320px;
            background:white;
            color:#17283d;
            padding:18px;
            border-radius:18px;
            box-shadow:0 15px 45px #0007;
            animation:notification 1s ease-out 3s forwards;
            z-index:10;
        }

        .phonehead {
            font-size:13px;
            color:#4c657d;
        }

        .amount {
            font-size:26px;
            font-weight:bold;
            color:#16a66a;
            margin-top:10px;
        }

        .money {
            position:absolute;
            top:-50px;
            font-size:25px;
            animation:fall 4s linear infinite;
        }

        .m1 {left:15%;animation-delay:0s;}
        .m2 {left:35%;animation-delay:1s;}
        .m3 {left:65%;animation-delay:2s;}
        .m4 {left:85%;animation-delay:1.5s;}

        .title {
            position:absolute;
            top:18px;
            left:15px;
            font-size:19px;
            font-weight:bold;
            z-index:4;
        }

        @keyframes walk {
            0% {left:-70px;}
            65% {left:40%;}
            100% {left:40%;}
        }

        @keyframes notification {
            0% {opacity:0;transform:translateX(-50%) scale(.5);}
            70% {opacity:1;transform:translateX(-50%) scale(1.1);}
            100% {opacity:1;transform:translateX(-50%) scale(1);}
        }

        @keyframes fall {
            0% {top:-50px;opacity:0;}
            20% {opacity:1;}
            100% {top:370px;opacity:0;}
        }

        @keyframes stars {
            from {background-position:0 0,0 0;}
            to {background-position:100px 100px,-100px 100px;}
        }
        </style>

        <div class="stage">
            <div class="stars"></div>
            <div class="moon"></div>
            <div class="title">6:02 PM — PAYDAY</div>
            <div class="window"></div>
            <div class="office"></div>
            <div class="person">🧑‍💼</div>

            <div class="money m1">💵</div>
            <div class="money m2">💰</div>
            <div class="money m3">💵</div>
            <div class="money m4">💰</div>

            <div class="phone">
                <div class="phonehead">📱 BANK NOTIFICATION</div>
                <div style="margin-top:8px;">
                    Salary credited successfully!
                </div>
                <div class="amount">+ ₹30,000</div>
                <div style="font-size:13px;margin-top:8px;">
                    Your first salary has arrived.
                </div>
            </div>
        </div>
        """, height=370)

        st.markdown("""
        ### 🎬 The Payday

        The office lights are slowly turning off.

        You have just finished your first month at your new job.
        Your phone vibrates.

        **Bank notification:** Salary credited successfully.

        You stare at your phone. This is the first money you earned yourself.
        """)

        if st.button("Continue →", use_container_width=True):
            st.session_state.l4_story_scene = 1
            st.rerun()

    # SCENE 2 - WEEKEND CHOICE
    elif scene == 1:

        components.html("""
        <div style="
        background:linear-gradient(135deg,#42245f,#814e9e);
        padding:25px;border-radius:20px;color:white;
        ">
        <div style="font-size:60px;text-align:center;">
        📱 🎉
        </div>
        <h2 style="text-align:center;color:white;">
        7:15 PM — The Invitation
        </h2>
        <p style="font-size:17px;">
        Your friend calls you.
        </p>
        <div style="
        background:#ffffff18;padding:15px;border-radius:15px;
        ">
        <b>Friend:</b><br>
        "Hey! Your salary arrived? Let's go out this weekend.
        We've planned a great evening!"
        </div>
        <p>
        You want to enjoy your first salary.
        But you know the weekend could cost money.
        </p>
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

    # SCENE 3 - ESSENTIAL BILLS
    elif scene == 2:

        components.html("""
        <div style="
        background:linear-gradient(135deg,#173d52,#287a83);
        padding:25px;border-radius:20px;color:white;
        ">
        <div style="font-size:60px;text-align:center;">
        🏠
        </div>
        <h2 style="text-align:center;color:white;">
        Monday — Reality Arrives
        </h2>
        <p>
        The weekend is over.
        </p>
        <p>
        You sit at your desk and open your banking app.
        Four payments are waiting.
        </p>
        </div>
        """, height=250)

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

    # SCENE 4 - EMERGENCY
    elif scene == 3:

        components.html("""
        <div style="
        background:linear-gradient(135deg,#692d38,#a54a51);
        padding:25px;border-radius:20px;color:white;
        ">
        <div style="font-size:60px;text-align:center;">
        📱💥
        </div>
        <h2 style="text-align:center;color:white;">
        Thursday — Unexpected Trouble
        </h2>
        <p>
        Your phone falls on the floor.
        </p>
        <p>
        The screen is completely broken.
        </p>
        <div style="
        background:#ffffff18;padding:15px;border-radius:15px;
        ">
        <b>Repair shop:</b><br>
        "The repair will cost ₹2,000."
        </div>
        <p>
        You weren't planning for this expense.
        </p>
        </div>
        """, height=300)

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

    # SCENE 5 - END OF MONTH
    elif scene == 4:

        components.html("""
        <div style="
        background:linear-gradient(135deg,#142c45,#356d88);
        padding:25px;border-radius:20px;color:white;
        ">
        <div style="font-size:60px;text-align:center;">
        🌙
        </div>
        <h2 style="text-align:center;color:white;">
        The End of the Month
        </h2>
        <p>
        It's the last day of the month.
        </p>
        <p>
        You open your bank account and look at what remains.
        </p>
        <p>
        One month ago, you had no experience managing a salary.
        Now you have made real financial decisions.
        </p>
        </div>
        """, height=270)

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

        st.write(f"**Weekend decision:** {st.session_state.l4_story_weekend}")

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
