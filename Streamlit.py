import streamlit as st

st.image("Budget app logo.svg")

# Title
st.title("Budg€t")

# Header
st.header("Your personal expense tracker")

# sub header
st.subheader("")

# information
st.info("first release")

# warning
st.warning("this version might have bugs and things not working as intended")

# error prompt
# st.error (".")
# success prompt
# st.success(".")

# write
st.write("Coded by Bobcat88")

# Widgets

# pick list
st.selectbox("pick from list", ["A", "B", "C"])

# Multi select from list
st.multiselect("select all applicable tag", ["1", "2", "3"])

# button
st.button("I\'m just a button ")

# Text Input
st.text_input("Enter your email address")

# number Input
st.number_input("Amount spent", 0, 20000)

#date input
st.date_input("When did this expense happened ?")

#file upload (csv or picture)
st.file_uploader("upload your file")

#Progress bar
st.progress(60)

#SIDEBAR
st.sidebar.title("Budget manager app")

#sidebar login

login_email = st.sidebar.text_input("email address")
login_password = st.sidebar.text_input("your password")

st.sidebar.button("Login")

#DataVisualisation//if needed import panda/numpy

#st.title("spending this month")
#data = panda.DataFrame(numpy.random.randint(30,1),columns=["Days", "spendings"])
#st.bar_chart(data)
