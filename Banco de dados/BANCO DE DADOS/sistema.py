import tkinter as tk
from tkinter import messagebox
import sqlite3

# ==========================
# CONEXÃO COM BANCO
# ==========================
conexao = sqlite3.connect("produtos.db")
cursor = conexao.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS produto (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    preco REAL NOT NULL
)
""")

conexao.commit()

# ==========================
# FUNÇÕES
# ==========================
def cadastrar():
    nome = txt_nome.get().strip()

    if not nome:
        messagebox.showerror("Erro", "Digite o nome do produto!")
        return

    try:
        preco = float(txt_preco.get())
    except ValueError:
        messagebox.showerror("Erro", "Digite um preço válido!")
        return

    sql = "INSERT INTO produto (nome, preco) VALUES (?, ?)"
    dados = (nome, preco)

    cursor.execute(sql, dados)
    conexao.commit()

    messagebox.showinfo("Sucesso", "Produto cadastrado com sucesso!")

    txt_nome.delete(0, tk.END)
    txt_preco.delete(0, tk.END)

    txt_nome.focus()


def buscar():
    cursor.execute("SELECT * FROM produto")
    produtos = cursor.fetchall()

    print("\n===== PRODUTOS CADASTRADOS =====")

    if not produtos:
        print("Nenhum produto cadastrado.")
        return

    for produto in produtos:
        print(
            f"ID: {produto[0]} | "
            f"Nome: {produto[1]} | "
            f"Preço: R$ {produto[2]:.2f}"
        )


def fechar_sistema():
    conexao.close()
    janela.destroy()


# ==========================
# JANELA PRINCIPAL
# ==========================
janela = tk.Tk()
janela.title("Sistema de Produtos")
janela.geometry("800x600")

janela.protocol("WM_DELETE_WINDOW", fechar_sistema)

# ==========================
# TÍTULO
# ==========================
titulo = tk.Label(
    janela,
    text="SISTEMA DE PRODUTOS",
    font=("Arial", 16, "bold")
)
titulo.pack(pady=10)

# ==========================
# FRAME DADOS
# ==========================
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
tk.Label(frame_dados, text="ID").grid(
    row=0,
    column=0,
    padx=5,
    pady=5
)

txt_id = tk.Entry(frame_dados)
txt_id.grid(
    row=0,
    column=1,
    padx=5,
    pady=5
)

# NOME
tk.Label(frame_dados, text="Nome").grid(
    row=1,
    column=0,
    padx=5,
    pady=5
)

txt_nome = tk.Entry(frame_dados, width=40)
txt_nome.grid(
    row=1,
    column=1,
    padx=5,
    pady=5
)

# PREÇO
tk.Label(frame_dados, text="Preço").grid(
    row=2,
    column=0,
    padx=5,
    pady=5
)

txt_preco = tk.Entry(frame_dados, width=40)
txt_preco.grid(
    row=2,
    column=1,
    padx=5,
    pady=5
)

# ==========================
# FRAME BOTÕES
# ==========================
frame_botoes = tk.Frame(janela)
frame_botoes.pack(pady=10)

btn_cadastrar = tk.Button(
    frame_botoes,
    text="Cadastrar",
    width=15,
    command=cadastrar
)

btn_cadastrar.grid(
    row=0,
    column=0,
    padx=5
)

btn_alterar = tk.Button(
    frame_botoes,
    text="Alterar",
    width=15
)

btn_alterar.grid(
    row=0,
    column=1,
    padx=5
)

btn_excluir = tk.Button(
    frame_botoes,
    text="Excluir",
    width=15
)

btn_excluir.grid(
    row=0,
    column=2,
    padx=5
)

btn_buscar = tk.Button(
    frame_botoes,
    text="Buscar",
    width=15,
    command=buscar
)

btn_buscar.grid(
    row=0,
    column=3,
    padx=5
)

# ==========================
# EXECUTA JANELA
# ==========================
janela.mainloop()