import streamlit as st
from PIL import Image
from todos import access_todos

st.set_page_config(page_title=None, page_icon=None, layout="centered", initial_sidebar_state="auto", menu_items=None)
st.subheader("Color to Grayscale Converter")

# Create a file uploader component allowing the user to upload a file
uploaded_image = st.file_uploader("Upload Image")

with st.expander("Start camera"):
    camera_image = st.camera_input("Camera")

if camera_image:
    # Supply camera_image to convert_image to get the grayscale version
    img = Image.open(camera_image)
    gray_camera_img = img.convert('L')
    st.image(gray_camera_img)

# Check if the image exists meaning the user has uploaded a file
if uploaded_image:
    # Open the user uploaded image with PIL
    img = Image.open(uploaded_image)
    # Convert the image to grayscale
    gray_uploaded_img = img.convert('L')
    # Display the grayscale image on the webpage
    st.image(gray_uploaded_img)

todos = access_todos("r")

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