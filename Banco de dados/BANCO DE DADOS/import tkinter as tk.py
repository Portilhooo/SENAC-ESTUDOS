import tkinter as tk
import sqlite3

# Conexão com o banco
conexao = sqlite3.connect("produtos.db")
cursor = conexao.cursor()

# Criação da tabela
cursor.execute("""
CREATE TABLE IF NOT EXISTS produto(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    preco REAL NOT NULL
)
""")
conexao.commit()


def cadastrar():
    nome = txt_nome.get()

    if nome == "":
        print("Digite o nome do produto!")
        return

    try:
        preco = float(txt_preco.get())
    except ValueError:
        print("Digite um preço válido!")
        return

    cursor.execute(
        "INSERT INTO produto(nome, preco) VALUES (?, ?)",
        (nome, preco)
    )

    conexao.commit()
    print("Produto cadastrado com sucesso!")

    txt_nome.delete(0, tk.END)
    txt_preco.delete(0, tk.END)


def buscar():
    cursor.execute("SELECT * FROM produto")
    produtos = cursor.fetchall()

    print("\n=== PRODUTOS CADASTRADOS ===")
    for produto in produtos:
        print(
            f"ID: {produto[0]} | "
            f"Nome: {produto[1]} | "
            f"Preço: R$ {produto[2]:.2f}"
        )


# Janela principal
janela = tk.Tk()
janela.title("Sistema de Produtos")
janela.geometry("800x600")

# Título
titulo = tk.Label(
    janela,
    text="SISTEMA DE PRODUTOS",
    font=("Arial", 16, "bold")
)
titulo.pack(pady=10)

# Frame de dados
frame_dados = tk.LabelFrame(
    janela,
    text="Dados do Produto",
    padx=10,
    pady=10
)
frame_dados.pack(
    fill="x",
    padx=10,
    pady=10
)

# ID
tk.Label(frame_dados, text="ID").grid(row=0, column=0, padx=5, pady=5)
txt_id = tk.Entry(frame_dados)
txt_id.grid(row=0, column=1, padx=5, pady=5)

# Nome
tk.Label(frame_dados, text="Nome").grid(row=1, column=0, padx=5, pady=5)
txt_nome = tk.Entry(frame_dados)
txt_nome.grid(row=1, column=1, padx=5, pady=5)

# Preço
tk.Label(frame_dados, text="Preço").grid(row=2, column=0, padx=5, pady=5)
txt_preco = tk.Entry(frame_dados)
txt_preco.grid(row=2, column=1, padx=5, pady=5)

# Frame de botões
frame_botoes = tk.Frame(janela)
frame_botoes.pack(pady=10)

btn_cadastro = tk.Button(
    frame_botoes,
    text="Cadastrar",
    width=15,
    command=cadastrar
)
btn_cadastro.grid(row=0, column=0, padx=5)

btn_alterar = tk.Button(
    frame_botoes,
    text="Alterar",
    width=15
)
btn_alterar.grid(row=0, column=1, padx=5)

btn_excluir = tk.Button(
    frame_botoes,
    text="Excluir",
    width=15
)
btn_excluir.grid(row=0, column=2, padx=5)

btn_busca = tk.Button(
    frame_botoes,
    text="Buscar",
    width=15,
    command=buscar
)
btn_busca.grid(row=0, column=3, padx=5)

# Executa a janela
janela.mainloop()

# Fecha conexão ao encerrar
conexao.close()