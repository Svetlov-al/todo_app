import streamlit as st
import functions
todos = functions.get_todos()


def add_todo():
    to_do = st.session_state['new_todo']
    todos.append(to_do + '\n')
    functions.write_todos(todos)


st.title('ToDo App')
st.subheader('This is your ToDos')
st.write('This app is to increase your productivity!')


for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[todo]
        st.experimental_rerun()


st.text_input(label=' ', placeholder='Add new todo...',
              on_change=add_todo, key='new_todo')