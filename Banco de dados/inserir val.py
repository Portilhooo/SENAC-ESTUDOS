import sqlite3
conexao=sqlite3.connect("lojinha.db")       
cursor=conexao.cursor()
cursor.execute("""
    INSERT INTO produtos(nome, categoria, qtd, preco) VALUES
        ('Mouse', 'Informática', 55, 200),
        ('Teclado', 'Informática', 56, 304)         
""")
conexao.commit()
conexao.close()
