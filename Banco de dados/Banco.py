import sqlite3
conexao = sqlite3.connect("lojinha.db")
cursor = conexao.cursor()  
cursor.execute("""
        CREATE TABLE IF NOT EXISTS produtos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT,
            categoria TEXT,
            qtd INTEGER,
            preco REAL)
    """)
print("Tabela lojinha criada")

conexao.commit()
conexao.close()