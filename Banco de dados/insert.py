import sqlite3
conexao = sqlite3.connect("lojinha.db")
cursor = conexao.cursor()  
cursor.execute("""
INSERT INTO produtos(nome, categoria, qtd, preco)
    VALUES 
    ('computador', 'informatica', 55, 500)
    ('mouse', 'informatica', 56, 55)
""")
conexao.commit()
conexao.close()
