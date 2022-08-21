import streamlit as st;
import models.Client as client
import controllers.ClientController as clientController
import pandas as pd


st.sidebar.title('Menu')
method = st.sidebar.selectbox('Client', ['Insert', 'Update', 'Delete', 'Select'])

if method == 'Select':
    st.title("List Client")
    clientList = []

    for item in clientController.selectAll():
        clientList.append([item.name, item.age, item.occupation])

    df = pd.DataFrame(clientList,
                      columns=['Name', 'Age', 'Occupation']
                      )
    st.table(df)

if method == 'Insert':
    st.title("Create Client")
    with st.form(key="include_client"):
        input_name = st.text_input(label="Insert your name")
        input_age = st.number_input(label="Insert your age", format="%i", step=1)
        input_occupation = st.selectbox(label="Select your occupation", options=("Developer", "Designer", "DBA", "Scrum Master"))
        input_button_submit = st.form_submit_button("Submit")

    if input_button_submit:
        client.name = input_name
        client.age = input_age
        client.occupation = input_occupation

        clientController.insert(client)
        st.success("Client Successfully Created!")


