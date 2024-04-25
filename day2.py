import streamlit as st

st.title("Welcome to the Tip Calculator")


with st.form("my Form"):

    total_bill = st.number_input("What was the total bill?")

    tip = st.number_input(
        "How much tip would you like to give? (in percentage)", step=1
    )

    person = st.number_input("How many people to split the bill?", step=1)
    submitted = st.form_submit_button("Submit")

if submitted:

    if total_bill and tip and person != 0:
        bill = total_bill + (total_bill * tip / 100)
        split = round(bill / person, 2)
        st.write(f"Each person should pay: ${split}")
    else:
        st.warning("Please fill all the data we need.")
