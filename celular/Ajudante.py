import androidhelper
import sys
import time
def menu():
          login = input('Digite o usuário: ')
          senha = int(input('Digite a senha: '))
          if senha==123:
                    print('Bem-vindo, Mestre Victor Como posso ajuda-la? ')
                    res = int(input('''O que deseja Mestre?
                    1 - Ouvir hora e data
                    2 - Falar Algo
                    3 - Tirar Foto
                    4 - Sair
                    '''))
                    if res==1:
                              droid= androidhelper.Android()
                              droid.ttsSpeak(time.strftime("%I %M %p on %A, %B %e, %Y"))
                    elif res==2:
                              droid = androidhelper.Android()
                              message = droid.dialogGetInput('Fala', 'Fale alguma coisa que queira repetir?').result
                              droid.ttsSpeak(message)
                    elif res==3:
                              droid = androidhelper.Android()
                              droid.cameraInteractiveCapturePicture('/sdcard/qpython.jpg')
                    elif res==4:
                              s = int(input('''Tem certeza que deseja sair, Mestre?
                              1 - sim
                              2 - nao
                              '''))
                              if s==1:
                                        print('Obrigado por me usar Mestre estarei as suas ordens!!!')
                                        sys.exit()
                              if s==2:
                                        print('Ok')
                                        menu()
                              else:
                                        print('Comando Invalido, Mestre')

                    else:
                              print('Você não e meu Mestre!!!')
                              sys.exit()
          else:
                    print('Usuario Incorreto!!!')
                    sys.exit()
menu()
          

if __name__ == '__main__':
    menu()
