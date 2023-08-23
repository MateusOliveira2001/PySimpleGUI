# Exemplo 2: Criar uma lista de tarefas com a capacidade de adicionar, editar e excluir itens.

import PySimpleGUI as sg

sg.theme('GrayGrayGray')

# Definindo layout
layout = [
    [sg.Push(), sg.Text('Lista de tarefas', font='Arial 16 bold', justification='c'), sg.Push()],
    [sg.Push(), sg.Text('Tarefa'), sg.Input(key='-TAREFA-'), sg.Push()],
    [sg.Table(values='', headings=['Índice', 'Tarefa'], key='-TABELA-', enable_events=True,
              size=(500,10), auto_size_columns=False,col_widths=[5,30], 
              vertical_scroll_only=False, justification='l', font='None 15')],
    [sg.Button('Adicionar'), sg.Button('Excluir'), sg.Button('Editar')]
]

# Definindo janela
janela = sg.Window('Lista de tarefas', layout)

# Definindo loop de eventos
contador = 1
tarefas = []
while True:
    evento, valores = janela.read()
    if evento == sg.WINDOW_CLOSED:
        break
    elif evento == 'Adicionar':
        tarefa = [[contador,valores['-TAREFA-']]]
        tarefas += tarefa
        janela['-TABELA-'].update(tarefas)
        janela['-TAREFA-'].update('')
        contador += 1
    elif evento == 'Excluir':
        if valores['-TABELA-']:
            index = valores['-TABELA-'][0]
            del tarefas[index]
            janela['-TABELA-'].update(tarefas)
    elif evento == 'Editar':
        if valores['-TABELA-']:
            index = valores['-TABELA-'][0]
            tarefa = tarefas[index][1]
            janela_editar = sg.Window('Edite a tarefa', layout=[
                [sg.Push(),sg.Text(f'Tarefa atual "{tarefa}" '),sg.Push()],
                [sg.Push(),sg.Text('Atualize a tarefa'),sg.Input(), sg.Push()],
                [sg.Push(),sg.Button('Atualizar', key='Atualizar'),sg.Push()]
            ])
            event, value = janela_editar.read()
            if event == 'Atualizar':
                tarefas[index][1] = value[0]
                janela_editar.close()
                janela['-TABELA-'].update(tarefas)

janela.read()