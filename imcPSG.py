import PySimpleGUI as sg



class Imc:
    def __init__(self):
        #layout
        layout = [[sg.Text('Peso/Kg:', size=7), sg.Input(size=(10), key='peso')],
                  [sg.Text('Altura: ', size=7), sg.Input(size=(10), key='altura')],
                  [sg.Button('Calcular IMC')],
                  [sg.Output(size=(30,5))]

        ]

        #janela
        self.window = sg.Window('Calculadora IMC').layout(layout)
        #calculo

    def Iniciar(self):
        while True:
            self.button, self.values = self.window.read()
            peso = float(self.values['peso'])
            altura = float(self.values['altura'])
            imc = peso / (altura**2)
            print(f'IMC: {imc:.2f}')


imc = Imc()
imc.Iniciar()