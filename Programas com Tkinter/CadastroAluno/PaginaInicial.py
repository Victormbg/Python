from deletar import *
from adicionar import *
from listar import *
from tkinter import *
from PIL import Image, ImageTk


def bt_sair():
    janela.destroy()


janela = Tk()

image = Image.open('img/iserj.png')
image = image.resize((700, 180))
photo = ImageTk.PhotoImage(image)
label = Label(image=photo)
label.image = photo
label.place(x=300, y=10)

bt = Button(janela, width=30, text="Cadastrar Aluno", font="Arial 15", command=adicionar)
bt.place(x=520, y=250)

bt = Button(janela, width=30, text="Listar Alunos Cadastrados", font="Arial 15", command=listar)
bt.place(x=520, y=350)

bt = Button(janela, width=30, text="Deletar Alunos", font="Arial 15", command=deletar)
bt.place(x=520, y=450)

bt = Button(janela, width=30, text="Sair", command=bt_sair, font="Arial 15")
bt.place(x=520, y=550)

image = Image.open('img/faetec.png')
image = image.resize((650, 50))
photo = ImageTk.PhotoImage(image)
label = Label(image=photo)
label.image = photo
label.place(x=60, y=630)

image = Image.open('img/rj.jpg')
image = image.resize((250, 100))
photo = ImageTk.PhotoImage(image)
label = Label(image=photo)
label.image = photo
label.place(x=900, y=600)

janela.geometry('1366x768+200+200')
janela.title('Sistema Academico')
janela.iconbitmap('img/escola.ico')
janela.mainloop()
