import FreeSimpleGUI as sg


feet_label = sg.Text("Enter feet:")
feet_input = sg.InputText()

inches_label = sg.Text("Enter inches:")
inches_input = sg.InputText()

button = sg.Button("Convert")

window = sg.Window("Convertor", layout=[[feet_label, feet_input],
                                        [inches_label, inches_input],
                                        [button]])
window.read()
window.close()

