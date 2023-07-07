import functions
import PySimpleGUI as sg


label = sg.Text("Write a to-do")
input_box = sg.InputText(tooltip="Enter to-do", key='todo')
add_button = sg.Button("Add")


window = sg.Window("StepByStep: Goal and Task Organizer",
                   layout=[[label], [input_box, add_button]],
                   font=("Helvetica", 20))

while True:
    event, values = window.read()

    match event:

        case 'Add':
            todos = functions.get_todos()
            new_todo = values['todo'].capitalize() + '\n'
            todos.append(new_todo)
            print(new_todo)
            functions.write_todos(todos)
        case sg.WINDOW_CLOSED:
            break

window.close()




