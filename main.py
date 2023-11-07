import streamlit as st

st.set_page_config(layout="wide")

column1, column2 = st.columns(2)

with column1:
    st.image("images/photo.png")

with (column2):
    st.title("Anastasiya S")
    content = """
    Hi, I am Anastasiya and everyone calls me Nastya
    """
    st.info(content)

content_more = \
    """
Below you can find some of the apps I have built in Python. Feel free to contact me!
    """

st.write(content_more)
