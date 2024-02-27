import streamlit as st
import functions

todos = functions.get_todos()
def add_todo():
    todo = st.session_state['add_todo'] + "\n"
    todos.append(todo)
    functions.write_todos(todos)

st.title("My Todo App")
# Path to the directory containing the file
directory_path = r"dist"

# Get the list of files in the directory
files = os.listdir(directory_path)

# Display a download button for each file
for file_name in files:
    file_path = os.path.join(directory_path, file_name)
    if st.download_button(label=f"Download Desktop APP", data=open(file_path, 'rb'), file_name=file_name):
        pass  # Optional: You can add any additional actions here after the file is downloaded
st.subheader("This is my todo app.")
st.write("This app is to increase your productivity.")


for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[todo]
        st.experimental_rerun()

st.text_input(label="Enter you todo", placeholder="Add new todo....",
              on_change=add_todo, key='add_todo')
