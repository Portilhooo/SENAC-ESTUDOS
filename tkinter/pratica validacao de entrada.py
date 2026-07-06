import tkinter as tk
from tkinter import messagebox

def processar():
    texto=entry_campo.get()
    if not texto:
        messagebox.showwarning("Atenção", "Campo vazio!")
    else:
        messagebox.showinfo("Sucesso", f"Enviado: {texto}")
        entry_campo.delete(0, tk.END)
root = tk.Tk()
root.title("Validação")
root.geometry("350x180")

tk.Label(root, text="Insira um valor:").pack(pady=10)
entry_campo=tk.Entry(root, width=40)
entry_campo.pack(pady=5)

tk.Button(root, text="Enviar", command=processar).pack(pady=10)

root.mainloop()