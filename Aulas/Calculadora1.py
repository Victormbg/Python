#coding: utf-8
# Author: Victor Manuel
# Calculadora
import sys

opcao = input("Deseja entrar na calculadora? Sim/Não: ")

if opcao == "Sim":
          def main():
                    print('''
                    Escolha a operação:
                    1 - Adição
                    2 - Subtração
                    3 - Divisão
                    4 - Multiplicação
                    5 - Sair
                    ''')
                    operacao = int(input("Escolha uma operação acima: "))
                    if operacao==1:
                              a = int(input("Digite o primeiro número: "))
                              b = int(input("Digite o segundo número: "))
                              c = (a+b)
                              print('A resposta da soma entre os valores de {} e {} é {}'.format(a,b,c))

                    elif operacao==2:
                              a = int(input("Digite o primeiro número: "))
                              b = int(input("Digite o segundo número: "))
                              c = (a-b)
                              print('A resposta da subtração entre os valores de {} e {} é {}'.format(a,b,c))
                    elif operacao==3:
                              a = int(input("Digite o primeiro número: "))
                              b = int(input("Digite o segundo número: "))
                              c = (a/b)
                              print('A resposta da divisão entre os valores de {} e {} é {}'.format(a,b,c))
                    elif operacao==4:
                              a = int(input("Digite o primeiro número: "))
                              b = int(input("Digite o segundo número: "))
                              c = (a*b)
                              print('A resposta da multiplicação entre os valores de {} e {} é {}'.format(a,b,c))
                    elif operacao==5:
                              saida()
                    else:
                              print("Operação invalida!!!")
                              main()          
                    
elif opcao=='nao':
          sys.exit()
else:
          print('Opção Invalida')
          main()
# função para sair do programa

def saida():
          print()
          sair = int(input("Sair? Digite 1 para sair, e 2 para continuar na calculadora: "))
          if sair == 1:
                    sys.exit()
          elif sair == 2:
                    main()
          else:
                    print('Erro')
                    saida()
              
if __name__ == '__main__':
    main()


