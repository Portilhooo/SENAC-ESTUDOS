import sqlite3
conexao = sqlite3.connect("escola.db")
cursor = conexao.cursor()
cursor.execute(
    "INSERT INTO alunos (nome, idade) VALUES (?,?)",
    ("Mayler", 37)
)
conexao.commit()
print("Aluno cadastrado com sucesso")
conexao.close()
