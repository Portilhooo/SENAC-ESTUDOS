import tkinter as tk
from tkinter import messagebox

class AppCadastro(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Sistema de Cadastro POO")
        self.geometry("400x200")
        self._criar_widgets()

    def _criar_widgets(self):
        frame= tk.Frame(self, padx=12, pady=8)
        frame.pack()
        tk.Label(frame, text="Nome:").grid(row=0, column=0, sticky="w", pady=4)
        self.entry_nome = tk.Entry(frame,width=30)
        self.entry_nome.grid(row=0, column=1)
        tk.Button(self, text="CADASTRAR", command=self._cadastrar_usuario).pack(pady=8)

    def _cadastrar_usuario(self):
        nome=self.entry_nome.get()
        if not nome:
            messagebox.showwarning("Erro", "Preencha o nome!")
            return
        messagebox.showinfo("Sucesso, " f"Cadastrado: {nome}")

#Bloco necessário para rodar a aplicação

if __name__ == "__main__":
    app = AppCadastro()
    app.mainloop()        