import streamlit as st

st.title("Welcome to the Band Name Generator")


with st.form("my Form"):
    col1, col2 = st.columns(2)
    with col1:
        name = st.text_input("Which city did you grow up in?")
    with col2:
        pet = st.text_input("What is the name of a pet?")
    submitted = st.form_submit_button("Submit")
    if submitted:
        st.write("Your band name could be " + name + " " + pet)
