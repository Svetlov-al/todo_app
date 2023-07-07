import functions
import PySimpleGUI as sg


label = sg.Text("Write a to-do")
input_box = sg.InputText(tooltip="Enter to-do")
add_button = sg.Button("Add")


window = sg.Window("StepByStep: Goal and Task Organizer", layout=[[label], [input_box, add_button]])
window.read()
window.close()





