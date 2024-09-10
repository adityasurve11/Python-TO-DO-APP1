import streamlit as st
import functions

todos = functions.get_todos()

st.title("My Todos App")
st.subheader("This is my todo app.")
st.write("This app is to remind me of tasks and increase productivity")

for todo in todos:
    st.checkbox(todo)

st.text_input(label = '', placeholder="Add new todo...")

print("Hello")

