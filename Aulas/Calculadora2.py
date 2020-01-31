# Author: Victor Manuel
# Calculadora
import sys

def menu():

    print (" ")
    print ("Calculadora")
    print("")
    print ("")
    var: int = int(input('''Para calcular digite a tecla correspondente:
    1 - Para Soma           
    2 - Para Subtração      
    3 - Para Multiplicação  
    4 - Para Divisão        
    5 - Sair
     '''))

    if var == 1:
        soma()

    elif var == 2:
        subtracao()

    elif var == 3:
        multiplicacao()

    elif var == 4:
        divisao()
	
    elif var == 5:
        sair()


# soma

def soma():

    print("")
    numero_1 = float(input("Digite o primeiro numero: "))
    print (" ")
    numero_2 = float(input("Digite o segundo numero: "))
    resultado_soma = (numero_1 + numero_2)
    print (" ")
    print ("O resultado da soma é:\n\n\t", resultado_soma)

    var= int(input('''

    Para calcular novamente tecle: 1
    Para voltar ao menu principal tecle 0

    '''))

    if var == 1:
        soma()

    else:
        menu()

# SUBTRAÇÃO

def subtracao():

    print(" ")
    numero_1 = float(input("Digite o primeiro numero: "))
    print (" ")
    numero_2 = float(input("Digite o segundo numero: "))
    resultado_sub = (numero_1 - numero_2)
    print (" ")
    print ("O resultado da subtração é:\n\n\t", resultado_sub())
    var= int(input('''

    Para calcular novamente tecle: 1
    Para voltar ao menu principal tecle 0

    '''))

    if var == 1:
        subtracao()

    else:
        menu()

# MULTIPLICAÇÃO

def multiplicacao():

    print (" ")
    numero_1 = float(input("Digite o primeiro numero: "))
    print (" ")
    numero_2 = float(input("Digite o segundo numero: "))
    resultado_multiplicacao = (numero_1 * numero_2)
    print (" ")
    print ("O resultado da multiplicação é:\n\n\t", resultado_multiplicacao)

    var= int(input('''

    Para calcular novamente tecle: 4
    Para voltar ao menu principal tecle 0

    '''))

    if var == 4:
        multiplicacao()

    else:
        menu()

# DIVISÃO

def divisao():
    print("")
    numero_1 = float(input("Digite o primeiro numero: "))
    print (" ")
    numero_2 = float(input("Digite o segundo numero: "))
    resultado_divisao = (numero_1 / numero_2)
    print (" ")
    print ("O resultado da divisão é:\n\n\t", resultado_divisao)

    var= int(input('''

    Para calcular novamente tecle: 2
    Para voltar ao menu principal tecle 0

    '''))

    if var == 7:
        divisao()

    else:
        menu()

#sair

def sair():
    while True:
        opcao = int(input('''Escolha uma opção: 
        		1 - Para continuar no programa
        		2 - Para sair do Programa

        		'''))

        if (opcao == 1):
            continue

            var = int(input('''

                Para voltar ao menu sair tecle: 1
                Para voltar ao menu principal tecle 0

                '''))

            if var == 1:
                sair()

            elif var ==0:
                menu()


        elif (opcao == 2):
            break
    else:
        print
        "Opcao invalida!"



if __name__ == '__main__':
    menu()
