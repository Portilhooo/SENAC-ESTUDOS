import sqlite3
conexao = sqlite3.connect("restaurante.db")
cursor = conexao.cursor()

cursor.execute(
    "INSERT INTO clientes(cpf, nome) VALUES (?, ?)",
    ("654656354", "Daniel")
    ("654645344", "Junior")
    ("654342354", "Carlos")
    ("213656354", "Pedro")

)

conexao.commit()
print("agua")

conexao.close()
