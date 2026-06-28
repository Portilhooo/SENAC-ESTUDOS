import tkinter as tk
from tkinter import messagebox
import sqlite3
conexao=sqlite3.connect("drogaria.db")
cursor=conexao.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS produtos1(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TXT NOT NULL,
    preco REAL NOT NULL              
                        )
""")
conexao.commit()
def cadastro():
    id = txt_id.get()
    nome = txt_nome.get()
    preco = txt_preco.get()

    cursor.execute("""
    INSERT INTO produto(id, nome, preco) 
    VALUES (?, ?, ?)""", 
    (id, nome, preco)
    )
    conexao.commit()
    print("CADASTRADO")

janela = tk.Tk()
janela.title("Sistema da Drogaria")
janela.geometry("900x700")
janela.configure(bg="#e6f2ff")
janela.resizable(False, False)

# ===== CONTAINER =====
frame = tk.Frame(janela, bg="white", bd=2, relief="groove")
frame.place(x=170, y=90, width=600, height=460)

# ===== TÍTULO =====
titulo = tk.Label(
    frame,
    text="CADASTRO DE PRODUTOS",
    font=("Arial", 16, "bold"),
    bg="white",
    fg="darkblue"
)
titulo.pack(pady=15)

# ===== CAMPOS =====
# Nome
tk.Label(frame, text="Nome do Produto:", bg="white", anchor="w").pack(fill="x", padx=20)
txt_nome = tk.Entry(frame, font=("Arial", 11))
txt_nome.pack(padx=20, pady=5, fill="x")

# Preço
tk.Label(frame, text="Preço:", bg="white", anchor="w").pack(fill="x", padx=20)
txt_preco = tk.Entry(frame, font=("Arial", 11))
txt_preco.pack(padx=20, pady=5, fill="x")

# Quantidade
tk.Label(frame, text="ID:", bg="white", anchor="w").pack(fill="x", padx=20)
txt_id = tk.Entry(frame, font=("Arial", 11))
txt_id.pack(padx=20, pady=5, fill="x")

# BOTÕES 
btn_cadastrar = tk.Button(
    frame,
    text="Cadastrar",
    bg="#2ecc71",
    fg="white",
    font=("Arial", 11, "bold"),
    height=2,
    command=cadastro
)
btn_cadastrar.pack(pady=10, fill="x", padx=20)

#BOTÃO BUSCAR

btn_buscar = tk.Button(
    frame,
    text="Buscar",
    bg="#3498db",
    fg="white",
    font=("Arial", 11, "bold"),
    height=2
)
btn_buscar.pack(pady=5, fill="x", padx=20)

#BOTÃO LISTAR

btn_alterar = tk.Button(
    frame,
    text="Alterar",
    bg="#f1c40f",
    fg="black",
    font=("Arial", 11, "bold"),
    height=2
)
btn_alterar.pack(pady=5, fill="x", padx=20)

#BOTÃO EXCLUIR
btn_excluir = tk.Button(
    frame,
    text="Excluir",
    bg="#e74c3c",
    fg="white",
    font=("Arial", 11, "bold"),
    height=2
)
btn_excluir.pack(pady=5, fill="x", padx=20)

janela.mainloop()