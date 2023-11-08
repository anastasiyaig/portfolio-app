import streamlit as st
import pandas

st.set_page_config(layout="wide")

column1, column2 = st.columns(2)

with column1:
    st.image("images/camphoto.jpeg", width=300)

with (column2):
    st.title("Anastasiya S")
    content = """Hi, I am Anastasiya and everyone calls me Nastya. I am open-minded and very friendly team player, 
    enjoying making a process of software development easier and understandable for all the participants. Bringing 
    awareness of what and why QA are doing on the project, enthusiastic to establish testing processes from scratch 
    and mentoring newcomers. Truly believe in Quality Assurance (not "testing" :) ), very communicative and straight 
    forward person, open to any opportunity to share knowledge and gain some where possible. I do have a various 
    experience of QA with mobile, desktop and web applications for more than 10 years in total now. I am good in 
    manual testing, variety of non-testing activities such as clarifying requirements, designs, talking to people and 
    making things clear, as well as in automation with Python. Interested in finance and banking industry, blockchain 
    technology and crypto adoption and my true passion is vehicles and related software (hope to get a dream job at 
    Honda some day :))"""
    st.info(content)

content_more = \
    """
Below you can find some of the apps I have built in Python. Feel free to contact me!
    """

st.caption(content_more)


column3, column4 = st.columns(2)

dataframe = pandas.read_csv("data.csv", sep=";")

with column3:
    for index, row in dataframe[:10].iterrows():
        st.header(row["title"])

with column4:
    for index, row in dataframe[10:].iterrows():
        st.header(row["title"])