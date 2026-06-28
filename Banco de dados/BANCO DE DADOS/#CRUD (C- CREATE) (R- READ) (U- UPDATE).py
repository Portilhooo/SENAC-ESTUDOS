#CRUD (C- CREATE) (R- READ) (U- UPDATE) (D -DROP)

import sqlite3
conexao=sqlite3.connect("mercadinho.db")
cursor=conexao.cursor()
dados=[
    ("Feijao", 3),
    ("Arroz", 4),
    ("Carne", 5),    
]
cursor.executemany("""
INSERT INTO produto (nome, preco)
VALUES (?,?), produto) 
""")
    
conexao.commit()
conexao.close()
print("testando")