import PySimpleGUI as sg



class Imc:
    def __init__(self):
        #layout
        layout = [[sg.Text('Peso/Kg:', size=7), sg.Input(size=(10), key='peso')],
                  [sg.Text('Altura: ', size=7), sg.Input(size=(10), key='altura')],
                  [sg.Button('Calcular IMC')],
                  [sg.Output(size=(30,5),key= 'saida')]

        ]

        #janela
        self.window = sg.Window('Calculadora IMC').layout(layout)


    def Iniciar(self):
        while True:
            self.button, self.values = self.window.read()
            peso = float(self.values['peso'])
            altura = float(self.values['altura'])
            imc = peso / (altura**2)
            self.window.FindElement('saida').Update('')
            print(f'IMC: {imc:.2f}')

            if imc < 18.5:
                print('''Classificação: Magreza
Obesidade (grau) = 0''')
            elif imc >= 18.5 and imc <= 24.9:
                print('''Classificação: Normal
Obesidade (grau) = 0''')
            elif imc >= 25 and imc <= 29.9:
                print('''Classificação: Sobrepeso
Obesidade (grau) = 1''')
            elif imc >= 30 and imc <= 39.9:
                print('''Classificação: Obesidade
Obesidade (grau) = 2''')
            else:
                print('''Classificação: Obesidade grave
Obesidade (grau) = 3''')


imc = Imc()
imc.Iniciar()
