from CadastroAluno import lstAluno
from deletar import *
from listar import *
from tkinter import *
from PIL import Image, ImageTk
import sqlite3


def adicionar():
          
          janela = Tk()

          ###TABELA###
          conn = sqlite3.connect("BD/alunos.db")
          cursor = conn.cursor()

          def criarTabela():
                    cursor.execute("""
                    CREATE TABLE IF NOT EXISTS Aluno (
                    matricula INTEGER NOT NULL PRIMARY KEY,
                    nome TEXT NOT NULL,
                    cpf TEXT NOT NULL,
                    endereco TEXT NOT NULL
                    );
                    """)

          criarTabela()

          def CadastarAluno():
                    nome = etNome.get()
                    cpf = etCpf.get()
                    endereco = etEndereco.get()
                    matricula = etMatricula.get()
                    cursor.execute("""
                    INSERT INTO Aluno (nome, cpf, endereco,matricula) VALUES (?, ?, ?, ?)""", (nome, cpf, endereco, matricula))
                    conn.commit()
                    lstAluno.insert(END, (nome, cpf, endereco, matricula))
          def bt_sair():
                    janela.destroy()          

          ### Widgets - Adicionar Aluno ###
          lblAdicionarAluno = Label(janela, text="Adicionar Aluno")
          lblNome = Label(janela, text="Nome: ")
          lblCpf = Label(janela, text="CPF: ")
          lblEndereco = Label(janela, text="Endereco: ")
          lblMatricula = Label(janela, text="Matricula: ")

          etMatricula = Entry(janela)
          etNome = Entry(janela)
          etCpf = Entry(janela)
          etEndereco = Entry(janela)


          btnAdd = Button(janela, text="Adicionar", command=CadastarAluno)

          ### Posicionamento de Widgets - Adicionar Aluno ###
          lblAdicionarAluno.place(x=100, y=30)

          lblMatricula.place(x=10, y=52)
          etMatricula.place(x=115, y=50)

          lblNome.place(x=10, y=82)
          etNome.place(x=115, y=80)

          lblCpf.place(x=10, y=112)
          etCpf.place(x=115, y=110)

          lblEndereco.place(x=10, y=142)
          etEndereco.place(x=115, y=140)

          btnAdd.place(x=115, y=165)

          ###Outros###
          bt = Button(janela, width=30, text="Sair",command=bt_sair,font="Arial 15")
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
          
          janela.geometry('1366x768')
          janela.title('Adicionar')
          janela.mainloop()
