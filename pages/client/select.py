import streamlit as st;
import controllers.ClientController as clientController
import pandas as pd


def list():
    st.title("List Client")
    clientList = []

    for item in clientController.selectAll():
        clientList.append([item.name, item.age, item.occupation])

    df = pd.DataFrame(clientList,
                      columns=['Name', 'Age', 'Occupation']
                      )
    st.table(df)