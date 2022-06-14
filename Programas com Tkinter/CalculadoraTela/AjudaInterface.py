from tkinter import *

def bt_click():
          lb['text']='Tchau'

janela = Tk()

bt = Button(janela, width=20, text='clica aqui', command=bt_click)
bt.place(x=100, y=100)




lb = Label(janela, text='Ola')
lb.place(x=100, y=180)


janela.title('Janela Principal')
janela['bg'] = 'green'
#LxA+E+T
#300x300+100+100
janela.geometry('300x300+100+100')

janela.mainloop()
