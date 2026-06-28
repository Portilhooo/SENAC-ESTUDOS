import sqlite3
conexao = sqlite3.connect("restaurante.db")
cursor = conexao.cursor()
cursor.execute("""CREATE TABLE IF NOT EXISTS clientes (    
    cpf INTEGER PRIMARY KEY AUTOINCREMENT, 
    nome TEXT NOT NULL)
""")

conexao.commit()
print("criado")
conexao.close()
