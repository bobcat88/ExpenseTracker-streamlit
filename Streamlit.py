import streamlit as st
st.image("Budg€t logo.svg")

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