from listar import *
from adicionar import *
from tkinter import *
import sqlite3
from tkinter import *

def deletar():
          ###TABELA###
          conn = sqlite3.connect("alunos.db")
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

          ###Funções###

          def bt_sair():
                    deletar.destroy()
          def deletar_estudante():
                    matricula_aluno = etMatriculaDeletar.get()
                    cursor.execute("""
                    DELETE FROM Aluno WHERE matricula=?""", (matricula_aluno,))
                    conn.commit()
                    lstAluno.delete(0, END)
                    lista = cursor.execute("""
                    SELECT * FROM Aluno;
                    """)
                    for i in lista:
                              lstAluno.insert(END, i)

          deletar = Tk()
          
          
          ### Widgets - Deletar Aluno ###
          lblDeletarAluno = Label(deletar, text="Deletar Aluno",font="Arial 50")
          blMatriculaDeletar = Label(deletar, text="Matrícula: ",font="Arial 30")
          etMatriculaDeletar = Entry(deletar, width=30)
          btnDel = Button(deletar, text="Deletar", command=deletar_estudante,font="Arial 15")
          bt = Button(deletar, width=30, text="Sair",command=bt_sair,font="Arial 15")



          ### Posicionamento de Widgets - Deletar Aluno ### 
          lblDeletarAluno.place(x=500, y=50)
          blMatriculaDeletar.place(x=350, y=200)
          etMatriculaDeletar.place(x=540, y=218)
          btnDel.place(x=550, y=300)
          bt.place(x=520, y=600)

          deletar.geometry('1366x768')
          deletar.title('Deletar')

          deletar.mainloop()
