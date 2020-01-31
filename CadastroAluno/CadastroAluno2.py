### Importações ###
from tkinter import *
import sqlite3

### Globais ###
conn = sqlite3.connect("alunos.db")
cursor = conn.cursor()

def criarTabela():
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS alunos (
            matricula INTEGER NOT NULL PRIMARY KEY,
            nome TEXT NOT NULL,
            nota TEXT NOT NULL
        );
    """)

criarTabela()

#### Definições da Aplicação Principal ###
principal = Tk()
principal.title("Aluno - Principal")
principal.geometry("600x333")
principal.resizable(FALSE, FALSE)

#### Funções ###
def adicionar_estudante():
    matricula = etMatricula.get()
    nome = etNome.get()
    nota = etNota.get()
    cursor.execute("""
        INSERT INTO alunos (matricula, nome, nota) VALUES (?, ?, ?)""", (matricula, nome, nota))
    conn.commit()
    lstAlunos.insert(END, (matricula, nome, nota))

def deletar_estudante():
    matricula_aluno = etMatriculaDeletar.get()
    cursor.execute("""
        DELETE FROM alunos WHERE matricula=?""", (matricula_aluno,))
    conn.commit()
    lstAlunos.delete(0, END)
    lista = cursor.execute("""
        SELECT * FROM alunos;
        """)
    for i in lista:
        lstAlunos.insert(END, i)

def mudar_nota():
    matricula_aluno = etMatriculaMudar.get()
    nova_nota = etNovaNota.get()
    cursor.execute("""
        UPDATE alunos SET nota = ? WHERE matricula = ?""", (nova_nota, matricula_aluno))
    conn.commit()
    lstAlunos.delete(0, END)
    lista = cursor.execute("""
        SELECT * FROM alunos;
        """)
    for i in lista:
        lstAlunos.insert(END, i)

def exportar():
    with io.open('alunos.sql', 'w') as f:
        for linha in conn.iterdump():
            f.write('%s\n' % linha)
    cursor.execute("""
        SELECT * FROM alunos;
    """)
    with io.open('alunos.txt', 'w') as f:
        for linha in cursor.fetchall():
            linha = str(linha)
            f.write('%s\n' % linha)

### Widgets - Principal ###
lblTitulo = Label(principal, text="Aluno")
lblNomeNota = Label(principal, text="Matrícula / Nome / Nota")

### Widgets - Adicionar Aluno ###
lblAdicionarAluno = Label(principal, text="Adicionar Aluno")
lblMatricula = Label(principal, text="Matrícula: ")
lblNome = Label(principal, text="Nome do Aluno: ")
lblNota = Label(principal, text="Nota do Aluno: ")
etMatricula = Entry(principal)
etNome = Entry(principal)
etNota = Entry(principal)
btnAdd = Button(principal, text="Adicionar", command=adicionar_estudante)

### Widgets - Deletar Aluno ###
lblDeletarAluno = Label(principal, text="Deletar Aluno")
lblMatriculaDeletar = Label(principal, text="Matrícula: ")
etMatriculaDeletar = Entry(principal, width=10)
btnDel = Button(principal, text="Deletar", command=deletar_estudante)

### Widgets - Mudar Nota ###
lblMudarNota = Label(principal, text="Mudar Nota")
lblMatriculaMudar = Label(principal, text="Matrícula: ")
lblNovaNota = Label(principal, text="Nota Nota: ")
etMatriculaMudar = Entry(principal)
etNovaNota = Entry(principal)
btnMudarNota = Button(principal, text="Mudar Nota", command=mudar_nota)

### Widgets - Listar Alunos ###
scrollbar = Scrollbar(principal)
lstAlunos = Listbox(principal, width=35, height=16)
lstAlunos.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=lstAlunos.yview)
lista = cursor.execute("""
    SELECT * FROM alunos;
    """)
for i in lista:
    lstAlunos.insert(END, i)

### Posicionamento de Widgets - Principal ###
lblTitulo.place(x=275)
lblNomeNota.place(x=308, y=30)

### Posicionamento de Widgets - Listar Alunos ####
lstAlunos.place(x=310, y=52)
scrollbar.place()

### Posicionamento de Widgets - Adicionar Aluno ###
lblAdicionarAluno.place(x=100, y=30)
lblMatricula.place(x=10, y=52)
etMatricula.place(x=115, y=50)
lblNome.place(x=10, y=82)
etNome.place(x=115, y=80)
lblNota.place(x=10, y=112)
etNota.place(x=115, y=110)
btnAdd.place(x=115, y=145)

### Posicionamento de Widgets - Deletar Aluno ###
lblDeletarAluno.place(x=100, y=175)
lblMatriculaDeletar.place(x=10, y=197)
etMatriculaDeletar.place(x=80, y=195)
btnDel.place(x=175, y=198)

### Posicionamento de Widgets - Mudar Nota ###
lblMudarNota.place(x=105, y=225)
lblMatriculaMudar.place(x=10, y=247)
etMatriculaMudar.place(x=115, y=245)
lblNovaNota.place(x=10, y=277)
etNovaNota.place(x=115, y=275)
btnMudarNota.place(x=115, y=308)

principal.mainloop()