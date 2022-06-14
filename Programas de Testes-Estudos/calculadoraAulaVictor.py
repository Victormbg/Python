# calculadora - Victor Manuel
import sys

def menu():
          a = int(input('Digite o primeiro valor: '))
          b = int(input('Digite o segundo valor: '))
          o = int(input('''Digite um número:
          Escolha a operação
          1 - soma
          2 - subtração
          3 - divisão
          4 - multiplicação
          5 - sair
          '''))
          if o==1:
                    c = a+b
                    print('A resposta entre {} e {} é {}'.format(a,b,c))
          elif o==2:
                    c = a-b
                    print('A resposta entre {} e {} é {}'.format(a,b,c))
          elif o==3:
                    c = a/b
                    print('A resposta entre {} e {} é {}'.format(a,b,c))
          elif o==4:
                    c = a*b
                    print('A resposta entre {} e {} é {}'.format(a,b,c))
          elif o==5:
                    saida()
          else:
                    print('Operação Invalida!!!')
def saida():
          r = input('Voce deseja sair da calculadora ? ')
          if r=='sim':
                    sys.exit()
          elif r=='nao' or 'não':
                    menu()
          else:
                    print('Erro!!!')
                    saida()

if __name__ == '__main__':
    menu()
