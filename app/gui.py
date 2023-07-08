import functions
import PySimpleGUI as sg
import time
import os

if not os.path.exists('files/todo.txt'):
    with open('files/todo.txt', 'w') as file:
        pass

sg.theme('Black')
clock = sg.Text('', key='clock')
label = sg.Text("Write a to-do")
input_box = sg.InputText(tooltip="Enter to-do", key='todo', size=35)
add_button = sg.Button(size=5,
                       image_source='files/add.png',
                       mouseover_colors='LightBlue2',
                       tooltip='Add Todo', key='Add')
list_box = sg.Listbox(values=functions.get_todos(), key='todos',
                      enable_events=True,
                      size=(35, 10))
edit_button = sg.Button("Edit")

complete_button = sg.Button(size=5,
                            image_source='files/complete.png',
                            mouseover_colors='LightBlue2',
                            key="Complete")

exit_button = sg.Button('Exit')

col_1 = sg.Column([[clock], [label], [input_box], [list_box], [exit_button]])
col_2 = sg.Column([[add_button], [edit_button], [complete_button]])

# window = sg.Window("StepByStep: Goal and Task Organizer",
#                    layout=[[clock],
#                            [label], [input_box, add_button],
#                            [list_box, edit_button, complete_button],
#                            [exit_button]],
#                    font=("Helvetica", 20))

window = sg.Window("StepByStep: Goal and Task Organizer",
                   layout=[[col_1, col_2]],
                   font=("Helvetica", 20))

while True:
    event, values = window.read(timeout=200)
    window['clock'].update(value=time.strftime("%b %d, %Y %H:%M:%S"))

    match event:

        case 'Add':
            todos = functions.get_todos()
            new_todo = values['todo'].capitalize() + '\n'
            todos.append(new_todo)
            print(new_todo)
            functions.write_todos(todos)
            window['todos'].update(values=todos)
        case 'Edit':
            try:
                todo_to_edit = values['todos'][0]
                new_todo = values['todo'].capitalize() + '\n'
                todos = functions.get_todos()
                index = todos.index(todo_to_edit)
                todos[index] = new_todo
                functions.write_todos(todos)
                window['todos'].update(values=todos)
            except Exception as ex:
                sg.popup('Please select an item first!', font=("Helvetica", 20))
                print(ex)
        case 'Complete':
            try:
                todo_to_complete = values['todos'][0]
                todos = functions.get_todos()
                todos.remove(todo_to_complete)
                functions.write_todos(todos)
                window['todos'].update(values=todos)
            except Exception as ex:
                sg.popup('Please select an item first!', font=("Helvetica", 20))
                print(ex)
        case 'todos':
            window['todo'].update(value=values['todos'][0])
        case 'Exit':
            break
        case sg.WINDOW_CLOSED:
            break

window.close()
