import streamlit as st;
import pages.client.insert as pageInsert
import pages.client.select as pageSelect

st.sidebar.title('Menu')
method = st.sidebar.selectbox('Client', ['Insert', 'Update', 'Delete', 'Select'])

if method == 'Select':
    pageSelect.list()

if method == 'Insert':
    pageInsert.create()
