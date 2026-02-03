import streamlit as st
from bank import Bank

bank = Bank()

st.title("🏦 Simple Bank System")
st.write("Welcome to your banking app!")

menu = st.sidebar.selectbox("Menu", [
    "Create Account",
    "Deposit Money",
    "Withdraw Money",
    "Show Details",
    "Update Details",
    "Delete Account"
])

# ---------------- CREATE ACCOUNT ----------------
if menu == "Create Account":
    st.header("Create New Account")

    name = st.text_input("Name")
    age = st.number_input("Age", min_value=1, max_value=120)
    email = st.text_input("Email")
    pin = st.text_input("4-digit PIN", type="password")

    if st.button("Create Account"):
        success, result = bank.create_account(name, age, email, pin)
        if success:
            st.success("Account Created!")
            st.json(result)
        else:
            st.error(result)

# ---------------- DEPOSIT ----------------
elif menu == "Deposit Money":
    st.header("Deposit Money")
    acc = st.text_input("Account Number")
    pin = st.text_input("PIN", type="password")
    amount = st.number_input("Amount", min_value=1)

    if st.button("Deposit"):
        success, msg = bank.deposit(acc, pin, amount)
        if success:
            st.success(f"New Balance: ₹{msg}")
        else:
            st.error(msg)

# ---------------- WITHDRAW ----------------
elif menu == "Withdraw Money":
    st.header("Withdraw Money")
    acc = st.text_input("Account Number")
    pin = st.text_input("PIN", type="password")
    amount = st.number_input("Amount", min_value=1)

    if st.button("Withdraw"):
        success, msg = bank.withdraw(acc, pin, amount)
        if success:
            st.success(f"Remaining Balance: ₹{msg}")
        else:
            st.error(msg)

# ---------------- SHOW DETAILS ----------------
elif menu == "Show Details":
    st.header("Account Details")
    acc = st.text_input("Account Number")
    pin = st.text_input("PIN", type="password")

    if st.button("Show"):
        user = bank.find_user(acc, pin)
        if user:
            st.json(user)
        else:
            st.error("Invalid account or PIN")

# ---------------- UPDATE ----------------
elif menu == "Update Details":
    st.header("Update Account")
    acc = st.text_input("Account Number")
    pin = st.text_input("Current PIN", type="password")

    name = st.text_input("New Name (optional)")
    email = st.text_input("New Email (optional)")
    new_pin = st.text_input("New PIN (optional)", type="password")

    if st.button("Update"):
        success, msg = bank.update_details(acc, pin, name, email, new_pin)
        if success:
            st.success("Details Updated")
            st.json(msg)
        else:
            st.error(msg)

# ---------------- DELETE ----------------
elif menu == "Delete Account":
    st.header("Delete Account")
    acc = st.text_input("Account Number")
    pin = st.text_input("PIN", type="password")

    if st.button("Delete"):
        success, msg = bank.delete_account(acc, pin)
        if success:
            st.success(msg)
        else:
            st.error(msg)
