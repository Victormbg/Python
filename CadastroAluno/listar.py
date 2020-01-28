from deletar import *
from adicionar import *
from tkinter import *
import sqlite3
def listar():
          
          janela = Tk()

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
          def exportar():
                    with io.open('Aluno.sql', 'w') as f:
                              for linha in conn.iterdump():
                                        f.write('%s\n' % linha)
                    cursor.execute("""
                    SELECT * FROM Aluno;
                    """)
                    with io.open('Aluno.txt', 'w') as f:
                              for linha in cursor.fetchall():
                                        linha = str(linha)
                                        f.write('%s\n' % linha)

          ### Widgets - Listar Alunos ###
          scrollbar = Scrollbar(janela)
          lstAluno = Listbox(janela, width=35, height=16)
          lstAluno.config(yscrollcommand=scrollbar.set)
          scrollbar.config(command=lstAluno.yview)
          lista = cursor.execute("""
              SELECT * FROM Aluno;
          """)
          for i in lista:
                    lstAluno.insert(END, i)


          ### Posicionamento de Widgets - Listar Alunos ####
          lstAluno.place(x=310, y=52)
          scrollbar.place()
          
          janela.geometry('1366x768')
          janela.title('Listar Alunos')

          janela.mainloop()
