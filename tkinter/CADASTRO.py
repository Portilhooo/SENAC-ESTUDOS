import tkinter as tk
from tkinter import messagebox

def cadastrar():
    nome, email=ent_nome.get(), ent_email.get()
    if not nome or not email:
        messagebox.showwarning("Erro", "Preencha todos os campos!")
        return
    messagebox.showinfo("Sucesso", f"Cadastrado:{nome}")
    ent_nome.delete(0,tk.END), ent_email.delete(0,tk.END)

root=tk.Tk()
root.title("Sistema de Cadastro"), 
root.geometry("400x250")

frame=tk.Frame(root, padx=20, pady=20)
frame.pack()

tk.Label(frame, text="Nome:").grid (row=0, column=0, sticky="w", pady=5)
ent_nome=tk.Entry(frame, width=30)
ent_nome.grid(row=0, column=1)

tk.Label(frame, text="E-mail:").grid (row=1, column=0, sticky="w", pady=5)
ent_email= tk.Entry(frame, width=30)
ent_email.grid(row=1, column=1)

tk.Button(root, text="CADASTRAR", bg="#06B6D4", fg="white",
            font=("Inter", 10, "bold"), command=cadastrar).pack(pady=20)

root.mainloop()
