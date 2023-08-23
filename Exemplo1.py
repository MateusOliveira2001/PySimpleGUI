#Exemplo 1: Criar um formulário de cadastro com campos de entrada e um botão de envio.

import PySimpleGUI as sg

# Definindo lógica interna
cadastrados = {}

def login(valores):
    global cadastrados
    if valores['-EMAIL-'] not in cadastrados:
        sg.popup('Este email não está cadastrado', font='Arial 16 bold', text_color='Red')
    else:
        if valores['-SENHA-'] == '':
            sg.popup('Insira uma senha', font='Arial 16 bold', text_color='Red')
        elif valores['-SENHA-'] != cadastrados[valores['-EMAIL-']]:
            sg.popup('Senha incorreta', font='Arial 16 bold', text_color='Red')
        else:
            sg.popup('Login realizado com sucesso', font='Arial 16 bold', text_color='Green')
            return janela.close()

def cadastrar(valores):
    global cadastrados
    if valores['-EMAIL-'] not in cadastrados:
        if valores['-SENHA-'] == '':
            return sg.popup('Insira uma senha', font='Arial 16 bold', text_color='Red')
        cadastrados[valores['-EMAIL-']] = valores['-SENHA-']
        sg.popup('Email e senha cadastrados', font='Arial 16 bold', text_color='Blue')
    elif valores['-EMAIL-'] in cadastrados:
        sg.popup('Email já cadastrado', font='Arial 16 bold', text_color='Red')
    elif valores['-SENHA-'] == '':
        sg.popup('Insira uma senha', font='Arial 16 bold', text_color='Red')

# Definindo tema
sg.theme('GrayGrayGray')


# Definindo layout
layout = [
    [sg.Text('Sistema de cadastro', font='Arial 16 bold', justification='c')],
    [sg.Push(), sg.Text('Email', font='Arial 12'), sg.Push(), sg.Input(key='-EMAIL-'), sg.Push()],
    [sg.Push(), sg.Text('Senha', font='Arial 12'), sg.Push(), sg.Input(password_char='*', key='-SENHA-'), sg.Push()],
    [sg.Push(), sg.Button('Login', button_color='Green', key='-LOGIN-'),
     sg.Push(), sg.Button('Cadastrar', button_color='Blue', key='-CADASTRAR-'),
     sg.Push()]
]

# Definindo janela
janela = sg.Window('Sistema de cadastro', layout)


# Loop de eventos
while True:
    evento, valores = janela.read()
    print(evento)
    print(valores)
    if '@' not in valores['-EMAIL-'] and '.com' not in valores['-EMAIL-']:
        sg.popup('Email inválido', font='Arial 16 bold', text_color='Red')

    elif evento == sg.WINDOW_CLOSED:
        break
    elif evento == '-LOGIN-':
        login(valores)
    elif evento == '-CADASTRAR-':
        cadastrar(valores)



janela.close()