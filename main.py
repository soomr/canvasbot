import keyboard
import PySimpleGUI as sg
import time
def answer(x):
    ans_to_int = ['A','B','C','D','E']
    ans = ans_to_int.index(x)
    time.sleep(.5)
    keyboard.send('tab')
    time.sleep(.5)
    keyboard.send('space')
    if ans != 0:
        for i in range(0,ans):
            time.sleep(.5)
            keyboard.send('down')

# All the stuff inside your window.
layout = [
            [sg.Text('Answers:'), sg.InputText()],
            [sg.Text('Log:',key = '-OUT-')],
            [sg.Button('Ok'), sg.Button('Cancel'), sg.Button('Start')] ]

# Create the Window
ans_to_int = ['A','B','C','D','E']
window = sg.Window('Canvas Bot', layout)
clean_list = []
# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Cancel': # if user closes window or clicks cancel
        break
    if event == 'Start':
        window.close()
        time.sleep(3)
        for i in clean_list:
            keyboard.send('tab')
            answer(str(i))
        break
    value_list = values[0].split('\n')
    for x in value_list:
        for i in x:
            i = i.capitalize()
            if i in ans_to_int:
                clean_list.append(i)
    print(clean_list)
    if not clean_list:
        sg.popup_ok('No suitable answers')
window.close()

