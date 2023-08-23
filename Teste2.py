import PySimpleGUI as sg

# Definindo tema
sg.theme('DarkPurple')

# Definindo layout
layout = [
    [sg.Image(filename='satélite.png', size=(600, 400))],
    [sg.Push(), sg.Text('Olá! Este é um texto de demonstração', font='Times 16 italic bold overstrike', text_color='Green'), sg.Push()],
    [sg.Text('É possível inserir informações em caixas como ao lado -->', font= 'Comic 14', text_color='Blue'),sg.Input(key='Entrada')],
    [sg.Push(), sg.Button('Botão 1', key='Botão 1', button_color='Brown'), sg.Push(), sg.Button('Botão 2', key='Botão 2', button_color='Purple'), sg.Push()],
]

# Definindo janela
window = sg.Window('Janela de teste', layout)

# Definindo laço de eventos
while True:
    evento, valores = window.read()
    if evento == 'Botão 1' or evento == sg.WINDOW_CLOSED:
        break
    else:
        print(valores)

window.close()