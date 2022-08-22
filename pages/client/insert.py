import streamlit as st;
import models.Client as client
import controllers.ClientController as clientController


def create():
    update_id = st.experimental_get_query_params()
    st.experimental_set_query_params()
    if update_id.get("id") != None:
        update_id = update_id.get("id")[0]
        st.title("Edit Client")
        st.write(update_id)
    else:
        st.title("Create Client")

    with st.form(key="include_client"):
        input_name = st.text_input(label="Insert your name")
        input_age = st.number_input(label="Insert your age", format="%i", step=1)
        input_occupation = st.selectbox(label="Select your occupation",
                                        options=("Developer", "Designer", "DBA", "Scrum Master"))
        input_button_submit = st.form_submit_button("Submit")

    if input_button_submit:
        client.name = input_name
        client.age = input_age
        client.occupation = input_occupation

        clientController.insert(client)
        st.success("Client Successfully Created!")