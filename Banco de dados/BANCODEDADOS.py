import sqlite3
conexao = sqlite3.connect("lojinhax.db")
cursor = conexao.cursor()  
cursor.execute("""
CREATE TABLE IF NOT EXISTS produtos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT,
        categoria TEXT,
        qtd INTEGER,
        preco REAL,
        estoque INTEGER)
""")
conexao.commit()
conexao.close()
print("Banco criado com sucesso")            