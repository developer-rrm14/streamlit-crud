import streamlit as st;

st.title("Create Client")

with st.form(key="include_client"):
    input_name = st.text_input(label="Insert your name")
    input_age = st.number_input(label="Insert your age", format="%i", step=1)
    input_occupation = st.selectbox(label="Select your occupation", options=("Developer", "Designer", "DBA", "Scrum Master"))
    input_button_submit = st.form_submit_button("Submit")


if input_button_submit:
    st.write(f'Name: {input_name}')
    st.write(f'Age: {input_age}')
    st.write(f'Occupation: {input_occupation}')