import streamlit as st
import pandas


st.set_page_config(layout="wide")
st.header("The Best Company")
st.write("""
A company profile serves multiple purposes, 
but two of its primary goals are to connect with customers 
and attract investors for funding opportunities.""")
st.subheader("Our Team")

col1, col2, col3 = st.columns(3)

df = pandas.read_csv("data2.csv")

with (col1):
    for index, row in df[:4].iterrows():
        st.subheader(f'{row["first name"].title()}{row["last name"].title()}')
        st.write(row['role'])
        st.image("BC/" + row["image"])

with (col2):
    for index, row in df[4:8].iterrows():
        st.subheader(f'{row["first name"].title()}{row["last name"].title()}')
        st.write(row['role'])
        st.image("BC/" + row["image"])

with (col3):
    for index, row in df[8:].iterrows():
        st.subheader(f'{row["first name"].title()}{row["last name"].title()}')
        st.write(row['role'])
        st.image("BC/" + row["image"])
