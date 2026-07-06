import tkinter as tk
from tkinter import messagebox

def mostrar_saudacao():
    nome= entry_nome.get()
    if nome:
        messagebox.showinfo("Ola,"f"Bem vindo, {nome}!")
    else:
        messagebox.showwarning("Erro", "Digite seu nome!")

root= tk.Tk()
root.title("App de Saudação")
tk.Label(root, text="Seu nome:").pack(pady=10)
entry_nome=tk.Entry(root)
entry_nome.pack(pady=5)

tk.Button(root, text="Enviar", command=mostrar_saudacao).pack(pady=10)
root.mainloop()