import streamlit as st
from todos import access_todos

todos = access_todos("r")
# print(todos)

def add_todo():
    new_todo = st.session_state["new_todo"] + "\n"
    todos.append(new_todo)
    access_todos("w", payload=todos)

# st.subheader("Welcome to...")
st.header("Todos Web Application")
st.write("We build this app to increase your productivity!")

for index, todo in enumerate(todos):
    is_complete = st.checkbox(todo, key=todo)
    if is_complete:
        todos.pop(index)
        access_todos("w", payload=todos)
        del st.session_state[todo]
        st.rerun()

st.text_input(label="New Todo", placeholder="Enter a new todo here...", key="new_todo", on_change=add_todo)