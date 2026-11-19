import streamlit as st
import time
from money_animation import money_transfer

def lesson3():
    st.title("🏦 The Bank's Busy Day")
    st.caption("Chapter 1 • Lesson 3")

    st.markdown("""
    <style>
    @keyframes bounce {
        0%,100% {transform:translateY(0);}
        50% {transform:translateY(-10px);}
    }
    @keyframes appear {
        from {opacity:0;transform:translateY(15px);}
        to {opacity:1;transform:translateY(0);}
    }
    .character {
        text-align:center;
        font-size:85px;
        animation:bounce 2s infinite;
    }
    .scene {
        background:linear-gradient(135deg,#172554,#312e81);
        padding:22px;
        border-radius:18px;
        color:white;
        animation:appear 0.8s ease;
    }
    .moneybox {
        background:#123524;
        padding:16px;
        border-radius:14px;
        text-align:center;
        color:#86efac;
        font-size:24px;
        font-weight:bold;
    }
    </style>
    """, unsafe_allow_html=True)

    if "bank_scene" not in st.session_state:
        st.session_state.bank_scene = 0

    scene = st.session_state.bank_scene

    if scene == 0:
        st.markdown("""
        <div class="scene">
        <h3>🌅 Morning at the Bank</h3>
        The bank opens. Customers are arriving.
        </div>
        """, unsafe_allow_html=True)

        st.markdown('<div class="character">👨‍💼</div>',
                    unsafe_allow_html=True)

        st.write("Bank Manager: Good morning! Let's see what happens today.")

        if st.button("Start the Day ▶️"):
            st.session_state.bank_scene = 1
            st.rerun()

    elif scene == 1:
        st.markdown("""
        <div class="scene">
        <h3>💰 Scene 1 — A Deposit</h3>
        Sarah walks into the bank.
        </div>
        """, unsafe_allow_html=True)

        st.markdown('<div class="character">👩‍💼</div>',
                    unsafe_allow_html=True)

        st.write("Sarah deposits ₹20,000 into her bank account.")

        money_transfer(20000, "Sarah's Money Deposited")

        st.write("The bank now owes Sarah ₹20,000.")

        if st.button("Next Scene ▶️"):
            st.session_state.bank_scene = 2
            st.rerun()

    elif scene == 2:
        st.markdown("""
        <div class="scene">
        <h3>🏦 Scene 2 — A Loan</h3>
        Rahul needs money to start a small business.
        </div>
        """, unsafe_allow_html=True)

        st.markdown('<div class="character">🧑‍🔧</div>',
                    unsafe_allow_html=True)

        st.write("The bank approves Rahul's ₹12,000 loan.")

        money_transfer(12000, "Rahul's Loan Deposit")

        st.write("""
        The loan creates a new deposit.

        Rahul also owes the bank ₹12,000 plus interest.
        """)

        if st.button("Next Scene ▶️"):
            st.session_state.bank_scene = 3
            st.rerun()

    elif scene == 3:
        st.markdown("""
        <div class="scene">
        <h3>⚠️ Scene 3 — A Difficult Moment</h3>
        Several customers want to withdraw their money.
        </div>
        """, unsafe_allow_html=True)

        st.markdown('<div class="character">😟</div>',
                    unsafe_allow_html=True)

        st.write("""
        Bank Manager: We need enough available cash and
        funding to meet withdrawals and payments.
        """)

        st.write("""
        Banks cannot simply lend everything without
        managing liquidity, risk and funding.
        """)

        st.markdown("### What should the manager do?")

        choice = st.radio(
            "Choose the bank's action:",
            [
                "Manage available liquidity and arrange funding",
                "Ignore the withdrawals"
            ],
            key="bank_choice"
        )

        if st.button("Make Decision"):
            st.session_state.bank_decision = choice
            st.session_state.bank_scene = 4
            st.rerun()

    elif scene == 4:
        choice = st.session_state.bank_decision

        st.markdown("""
        <div class="scene">
        <h3>🎬 The Outcome</h3>
        </div>
        """, unsafe_allow_html=True)

        if choice == "Manage available liquidity and arrange funding":
            st.markdown('<div class="character">😌</div>',
                        unsafe_allow_html=True)

            st.success("The bank manager takes action.")

            st.write("""
            The bank manages its cash, liquid assets and funding
            to meet payment demands.

            Managing liquidity helps, but it does not guarantee
            that a bank will always survive.
            """)

        else:
            st.markdown('<div class="character">😰</div>',
                        unsafe_allow_html=True)

            st.error("The bank ignores the problem.")

            st.write("""
            Customers may lose confidence.

            If the bank cannot meet its payment obligations,
            it may face serious liquidity problems and potentially
            fail, depending on the circumstances.
            """)

        st.markdown("---")
        st.markdown("### 🧠 What did you learn?")

        st.write("""
        Banks accept deposits, provide loans and manage
        liquidity, credit risk and funding.

        A bank's assets and liabilities are different.
        Deposits are generally liabilities for the bank,
        while loans are generally assets.
        """)

        if st.button("Replay Episode 🔄"):
            st.session_state.bank_scene = 0
            st.session_state.pop("bank_decision", None)
            st.rerun()

    st.markdown("---")
    st.caption("MoneyLab • Learn Money by Living It")
