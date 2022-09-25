import streamlit as st
# Using the "with" syntax
crimes_compliance = ['Assedio moral', 'Assedio sexual', 'Corrupção']
with st.form(key='my_form'):
    select_box = st.selectbox(
    'Crime',
    crimes_compliance)
    text_input = st.text_input(label='Relato')

    submit_button = st.form_submit_button(label='Submit')

