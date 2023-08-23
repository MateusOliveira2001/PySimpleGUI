import PySimpleGUI as sg

#cria o layout
layout = [
    [sg.Text('Texto de demonstração')],
    [sg.Button(f'OK {num}') for num in range(1,6)]
]

#cria a janela
window= sg.Window('Demonstração', layout)

#cria um laço de enventos
while True:
    event, values = window.read()
    if event == 'OK' or event == sg.WINDOW_CLOSED:
        break

window.close()