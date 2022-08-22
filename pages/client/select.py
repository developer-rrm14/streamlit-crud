import streamlit as st;
import controllers.ClientController as clientController
import pandas as pd


def list():
    st.title("List Client")
    columns = st.columns((1, 3, 1, 2, 1, 1))
    header = ['Code', 'Name', 'Age', 'Occupation', 'Remove', 'Edit']
    for col, field_name in zip(columns, header):
        col.write(field_name)

    for item in clientController.selectAll():
        col1, col2, col3, col4, col5, col6 = st.columns((1, 3, 1, 2, 1, 1))
        col1.write(item.id)
        col2.write(item.name)
        col3.write(item.age)
        col4.write(item.occupation)
        button_delete = col5.empty()
        on_click_delete = button_delete.button('Remove', 'btn_remove' + str(item.id))
        button_edit = col6.empty()
        on_click_edit = button_edit.button('Edit', 'btn_edit' + str(item.id))

        if on_click_delete:
            clientController.delete(item.id)
