import PySimpleGUI as sg

window1 = sg.Window('Janela de demonstrção', layout=[
    [sg.Text('Apenas um botão é o correto. Selecione com atenção.')],
    [sg.Push(),sg.Text('Linha 1'), sg.Push(), sg.Button('Botão 1', key= 'Botão 1'), sg.Push()],
    [sg.Push(), sg.Text('Linha 2'), sg.Push(), sg.Button('Botão 2', key='Botão 2'), sg.Push()]
    ])


while True:
    evento_1, valor_1 = window1.read()

    if evento_1 == 'Botão 2':
        sg.popup_ok('Que pena! Tentar novamente?')
    elif evento_1 == 'Botão 1':
        sg.popup_ok('Parabéns! Você acertou o botão corretamente.')
        break
    elif evento_1 == sg.WINDOW_CLOSED:
        break

window1.close()
        