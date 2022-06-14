# Author: Victor Manuel
# CadastroAluno

from tkinter import *
import sqlite3

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

###FUNCOES DA TELA###

def CadastarAluno():
    nome = etNome.get()
    cpf = etCpf.get()
    endereco = etEndereco.get()
    matricula = etMatricula.get()
    cursor.execute("""
        INSERT INTO Aluno (nome, cpf, endereco,matricula) VALUES (?, ?, ?, ?)""", (nome, cpf, endereco, matricula))
    conn.commit()
    lstAluno.insert(END, (nome, cpf, endereco, matricula))


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


#FUNCOES E CONFIGURAÇOES DA TELA

#### Definições da Aplicação Principal ###
principal = Tk()
principal.title("Cadastro de Alunos")
principal.geometry("600x333")
principal.resizable(FALSE, FALSE)

### Widgets - Principal ###
lblTitulo = Label(principal, text="Aluno")
lblNomeNota = Label(principal, text="Nome / CPF / Endereco / Matricula")

### Widgets - Adicionar Aluno ###
lblAdicionarAluno = Label(principal, text="Adicionar Aluno")
lblNome = Label(principal, text="Nome: ")
lblCpf = Label(principal, text="CPF: ")
lblEndereco = Label(principal, text="Endereco: ")
lblMatricula = Label(principal, text="Matricula: ")

etMatricula = Entry(principal)
etNome = Entry(principal)
etCpf = Entry(principal)
etEndereco = Entry(principal)


btnAdd = Button(principal, text="Adicionar", command=CadastarAluno)

### Widgets - Deletar Aluno ###
lblDeletarAluno = Label(principal, text="Deletar Aluno")
lblMatriculaDeletar = Label(principal, text="Matrícula: ")
etMatriculaDeletar = Entry(principal, width=10)
btnDel = Button(principal, text="Deletar", command=deletar_estudante)

### Widgets - Listar Alunos ###
scrollbar = Scrollbar(principal)
lstAluno = Listbox(principal, width=35, height=16)
lstAluno.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=lstAluno.yview)
lista = cursor.execute("""
    SELECT * FROM Aluno;
    """)
for i in lista:
    lstAluno.insert(END, i)

### Posicionamento de Widgets - Principal ###
lblTitulo.place(x=275)
lblNomeNota.place(x=308, y=30)

### Posicionamento de Widgets - Listar Alunos ####
lstAluno.place(x=310, y=52)
scrollbar.place()

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

### Posicionamento de Widgets - Deletar Aluno ###
lblDeletarAluno.place(x=100, y=195)
lblMatriculaDeletar.place(x=10, y=207)
etMatriculaDeletar.place(x=80, y=218)
btnDel.place(x=175, y=218)

principal.mainloop()
