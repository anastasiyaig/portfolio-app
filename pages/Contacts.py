import streamlit as st

st.header("Contact Me")

with st.form(key="contact_form"):
    visitor_email = st.text_input(
        "Please, provide your email",
        placeholder='johndoe@hotmail.com')
    visitor_message = st.text_area(
        label="Please, enter your message",
        label_visibility='visible',
        placeholder='Enter your message here',
        max_chars=1000)
    submit_button = st.form_submit_button(
        label="Send"
    )
    if submit_button:
        email_content = visitor_email + visitor_message
        pass
