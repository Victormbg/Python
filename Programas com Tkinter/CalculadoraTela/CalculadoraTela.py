from tkinter import *
from PIL import Image, ImageTk
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
def bt_sair():
          janela.destroy()

image = Image.open('cal.png')
image = image.resize((130, 130))
photo = ImageTk.PhotoImage(image)
label = Label(image=photo)
label.image = photo 
label.place(x=650, y=10)

lbt = Label(janela,text='Calculadora',bg='blue',font="Arial 30")
lbt.place(x=600, y=150)

lb1 = Label(janela,text='Digite o primeiro valor: ',bg='blue',font="Arial 30")
lb1.place(x=10, y=200)
ed1 = Entry(janela)
ed1.insert(INSERT, 'Insira um valor')
ed1.place(x=420,y=220)

lb2 = Label(janela,text='Digite o primeiro valor: ',bg='blue',font="Arial 30")
lb2.place(x=10, y=300)
ed2 = Entry(janela)
ed2.place(x=420,y=320)

lb3 = Label(janela,text='Escolha a operação: ',bg='blue',font="Arial 30")
lb3.place(x=10, y=400)
ed3 = Entry(janela)
ed3.place(x=400,y=420)

bt = Button(janela, width=20, text="Calcular",command=bt_click)
bt.place(x=650, y=500)

lbres = Label(janela,text='A resposta é:',bg='blue',font="Arial 24")
lbres.place(x=630, y=580)
lb = Label(janela,text="",bg='blue',font="Arial 24")
lb.place(x=820, y=580)

bt = Button(janela, width=20, text="Sair",command=bt_sair)
bt.place(x=650, y=650)

janela.geometry('1366x768+200+200')
janela.title('Calculadora')

janela.iconbitmap('calc.ico')
janela['bg'] = 'blue'
janela.mainloop()
