# cadastroAluno
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

###FUNCOES###

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
    with io.open('Banco.sql', 'w') as f:
        for linha in conn.iterdump():
            f.write('%s\n' % linha)
    cursor.execute("""
        SELECT * FROM Aluno;
    """)
    with io.open('BD/Banco.txt', 'w') as f:
        for linha in cursor.fetchall():
            linha = str(linha)
            f.write('%s\n' % linha)
