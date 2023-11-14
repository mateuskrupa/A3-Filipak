import PySimpleGUI as sg

from main import verificar_cartao

sg.theme('DarkBlue')
layout = [  [sg.Text('Digite o número do cartão:'), sg.InputText()],
            [sg.Button('Verificar'), sg.Button('Fechar'), sg.Text('NÚMERO SEM ESPAÇOS OU PONTOS   '), sg.Text('', key="texto")]]


window = sg.Window('Verificador de Cartão de Crédito', layout)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Fechar':
        break

    if event == "Verificar":
        n = values[0]
        print('You entered ', values[0])

        verificar = verificar_cartao(n)

        window["texto"].update(f"{verificar}")

window.close()

