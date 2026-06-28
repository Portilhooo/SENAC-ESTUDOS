import sqlite3
conexao = sqlite3.connect("escola.db")
cursor = conexao.cursor()
cursor.execute("""CREATE TABLE IF NOT EXISTS alunos (    
    id INTENGER PRIMARY KEY AUTOINCREMENT, 
    nome TEXT NOT NULL,y
    idade INTENGER)   
""")
print("\nTabela do banco master criado")
conexao.commit()
conexao.close()
