import streamlit as st
# Using the "with" syntax
crimes_compliance = ['Assedio moral', 'Assedio sexual', 'Corrupção']
with st.form(key='my_form'):
    text_input = st.text_input(label='Relato')
    select_box = st.selectbox(
    'Crime',
    crimes_compliance)
    submit_button = st.form_submit_button(label='Submit')

