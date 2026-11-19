import streamlit as st

def lesson2():
    st.title("🏦 Alex and the Bank")
    st.caption("Chapter 1 • How Money Is Created")

    st.markdown("""
    <style>
    @keyframes bounce {
        0%,100% {transform:translateY(0);}
        50% {transform:translateY(-12px);}
    }
    .alex {
        font-size:100px;
        text-align:center;
        animation:bounce 2s infinite;
    }
    .bank {
        font-size:65px;
        text-align:center;
    }
    .money {
        background:#123524;
        padding:18px;
        border-radius:15px;
        text-align:center;
        color:#86efac;
        font-size:25px;
        font-weight:bold;
    }
    </style>
    """, unsafe_allow_html=True)

    st.markdown('<div class="bank">🏦</div>', unsafe_allow_html=True)
    st.markdown('<div class="alex">🧑</div>', unsafe_allow_html=True)

    st.markdown("### Meet Alex")
    st.write("Alex wants ₹10,000. The bank offers him a loan.")

    st.markdown("""
    <div class="money">
    Bank offer: ₹10,000
    </div>
    """, unsafe_allow_html=True)

    st.write("But this money is borrowed. Alex must repay it with interest.")

    choice = st.radio(
        "What should Alex do?",
        ["Accept the loan", "Reject the loan"],
        key="alex_decision"
    )

    if st.button("Make Decision", key="alex_button"):

        st.session_state.alex_result = choice

    if "alex_result" in st.session_state:

        result = st.session_state.alex_result

        st.markdown("---")

        if result == "Accept the loan":

            st.success("Alex accepted the loan!")

            st.markdown("""
            <div class="money">
            Bank Balance: +₹10,000
            </div>
            """, unsafe_allow_html=True)

            st.markdown("""
            <div style="background:#451a1a;padding:18px;
            border-radius:15px;text-align:center;color:#fca5a5;
            font-size:24px;font-weight:bold;">
            Loan Debt: ₹10,000 + Interest
            </div>
            """, unsafe_allow_html=True)

            st.markdown('<div class="alex">😃</div>', unsafe_allow_html=True)

            st.write("""
            Alex received money, but he also created a debt.

            A bank loan generally creates a new deposit
            in the borrower's account.
            """)

        else:

            st.info("Alex rejected the loan.")

            st.markdown("""
            <div class="money">
            New Loan: ₹0
            </div>
            """, unsafe_allow_html=True)

            st.markdown('<div class="alex">🙂</div>', unsafe_allow_html=True)

            st.write("""
            Alex didn't borrow money.

            His balance didn't increase, but he also
            didn't take on a new loan debt.
            """)

        st.markdown("---")
        st.markdown("### 🧠 What did you learn?")

        st.write("""
        When a commercial bank lends money, it generally
        creates a deposit and a corresponding loan.

        Borrowed money is not free money.
        """)

        if st.button("Try Another Decision", key="alex_reset"):
            del st.session_state.alex_result
            st.rerun()

    st.caption("MoneyLab • Learn Money by Living It")
