
import streamlit as st

def lesson1():
    st.title("📚 Chapter 1 — How Money Works")
    st.markdown("## Lesson 1: What Is Money?")

    st.write("""
    Money is a tool that allows people to exchange value.

    Instead of directly exchanging goods with other people,
    we use money to buy goods and services.
    """)

    st.markdown("### The 3 functions of money")

    with st.expander("1. Medium of Exchange"):
        st.write("""
        Money makes buying and selling easier.

        Example: You give ₹100 to a shopkeeper and receive food.
        You don't need to exchange another product.
        """)

    with st.expander("2. Store of Value"):
        st.write("""
        Money allows you to save purchasing power for the future.

        However, inflation may reduce that purchasing power over time.
        """)

    with st.expander("3. Unit of Account"):
        st.write("""
        Money provides a common way to measure and compare prices.

        Example:
        A book costs ₹500 and a pen costs ₹20.
        Money helps us compare their prices.
        """)

    st.markdown("---")
    st.markdown("### 🧠 Knowledge Check")

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
            st.success("Correct! Money makes exchanging goods and services easier.")
        else:
            st.error("Not quite. Think about how money helps people buy and sell goods.")

    st.markdown("---")
    st.caption("Chapter 1 • Lesson 1")
