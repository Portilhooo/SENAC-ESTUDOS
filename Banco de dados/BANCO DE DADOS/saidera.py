import tkinter as tk
from tkinter import ttk
import sqlite3
# banco de dados
conexao = sqlite3.connect("produtos.db")
cursor = conexao.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS produto(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    preco REAL NOT NULL
)
""")

conexao.commit()

# função cadastrar

def cadastrar():

    nome = txt_nome.get()
    preco = txt_preco.get()

    cursor.execute(
        """
        INSERT INTO produto(nome, preco)
        VALUES (?, ?)
        """,
        (nome, preco)
    )

    conexao.commit()

    txt_nome.delete(0, tk.END)
    txt_preco.delete(0, tk.END)

    listar()

# função listar

def listar():

    tabela.delete(*tabela.get_children())

    cursor.execute(
        "SELECT id, nome, preco FROM produto"
    )

    produtos = cursor.fetchall()

    for produto in produtos:

        tabela.insert(
            "",
            tk.END,
            values=produto
        )

# função selecionar

def selecionar(event):

    item = tabela.focus()

    dados = tabela.item(item)

    valores = dados["values"]

    txt_id.delete(0, tk.END)
    txt_nome.delete(0, tk.END)
    txt_preco.delete(0, tk.END)

    txt_id.insert(0, valores[0])
    txt_nome.insert(0, valores[1])
    txt_preco.insert(0, valores[2])

# função alterar

def alterar():

    id_produto = txt_id.get()
    nome = txt_nome.get()
    preco = txt_preco.get()

    cursor.execute(
        """
        UPDATE produto
        SET nome = ?, preco = ?
        WHERE id = ?
        """,
        (nome, preco, id_produto)
    )

    conexao.commit()

    listar()

    txt_id.delete(0, tk.END)
    txt_nome.delete(0, tk.END)
    txt_preco.delete(0, tk.END)

# função excluir

def excluir():

    id_produto = txt_id.get()

    cursor.execute(
        """
        DELETE FROM produto
        WHERE id = ?
        """,
        (id_produto,)
    )

    conexao.commit()

    listar()

    txt_id.delete(0, tk.END)
    txt_nome.delete(0, tk.END)
    txt_preco.delete(0, tk.END)

# janela

janela = tk.Tk()

janela.title("PROJ TURMA 203")

janela.geometry("800x600")

# titulo

titulo = tk.Label(
    janela,
    text="PROJETO TURMA 203",
    font=("Arial", 16, "bold")
)

titulo.pack(pady=10)

# dados do produto

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

# campo id

tk.Label(
    frame_dados,
    text="ID"
).grid(row=0, column=0)

txt_id = tk.Entry(
    frame_dados,
    width=30
)

txt_id.grid(row=0, column=1)

# campo nome

tk.Label(
    frame_dados,
    text="Nome"
).grid(row=1, column=0)

txt_nome = tk.Entry(
    frame_dados,
    width=30
)

txt_nome.grid(row=1, column=1)

# campo preço

tk.Label(
    frame_dados,
    text="Preço"
).grid(row=2, column=0)

txt_preco = tk.Entry(
    frame_dados,
    width=30
)

txt_preco.grid(row=2, column=1)

# botoes

frame_botoes = tk.Frame(janela)

frame_botoes.pack(pady=10)

# botão cadastrar

btn_cadastrar = tk.Button(
    frame_botoes,
    text="Cadastrar",
    width=15,
    command=cadastrar
)

btn_cadastrar.grid(row=0, column=0, padx=5)

# botão alterar

btn_alterar = tk.Button(
    frame_botoes,
    text="Alterar",
    width=15,
    command=alterar
)

btn_alterar.grid(row=0, column=1, padx=5)

# botão excluir

btn_excluir = tk.Button(
    frame_botoes,
    text="Excluir",
    width=15,
    command=excluir
)

btn_excluir.grid(row=0, column=2, padx=5)

# tabela

tabela = ttk.Treeview(
    janela,
    columns=("id", "nome", "preco"),
    show="headings"
)

tabela.heading("id", text="ID")
tabela.heading("nome", text="Nome")
tabela.heading("preco", text="Preço")

tabela.column("id", width=100)
tabela.column("nome", width=400)
tabela.column("preco", width=150)

tabela.pack(
    fill="both",
    expand=True,
    padx=10,
    pady=10
)

# evento da tabela

tabela.bind(
    "<<TreeviewSelect>>",
    selecionar
)

# carregar produtos

listar()

# executar janela

janela.mainloop()

# fechar banco

conexao.close()