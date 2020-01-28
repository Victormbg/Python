from tkinter import *
janela = Tk()

def bt_click():
          num1 = int(ed1.get())
          num2 = int(ed2.get())
          op = ed3.get()
          if op=='soma':
                    lb["text"] = num1+num2
          if op=='subtracao':
                    lb["text"] = num1-num2
          if op=='divisao':
                    lb["text"] = num1/num2
          if op=='multiplicacao':
                    lb["text"] = num1*num2
          





ed1 = Entry(janela)
ed1.place(x=100,y=100)

ed2 = Entry(janela)
ed2.place(x=100,y=130)

ed3 = Entry(janela)
ed3.place(x=100,y=150)

bt = Button(janela, width=20, text="Calcular",command=bt_click)
bt.place(x=100, y=170)

lb = Label(janela, text="")
lb.place(x=100, y=200)









janela.geometry('400x300+200+200')

janela.mainloop()
