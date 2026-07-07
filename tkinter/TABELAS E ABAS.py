import tkinter as tk
from tkinter import ttk, messagebox

class PainelEscolar(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Sistema Escolar - ttk Avançado")
        self.geometry("450x300")

        self._configurar_estilos()
        self._criar_abas()

    def _configurar_estilos(self):
        style= ttk.Style()
        style.theme_use("clam")
        style.configure("TButtom", font=("Arial", 10, "bold"), foreground="#1D4ED8")
        style.configure("Treeview.Heading", font=("Arial", 10, "bold"))

    def _criar_abas(self):
        notebook= ttk.Notebook(self)
        notebook.pack(expand=True, fill="both", padx=10, pady=10)

    #aba 1: Cadastro

        self.aba_cadastro = ttk.Frame(notebook)   
        notebook.add(self.aba_cadastro, text="Novo Aluno")
        self._montar_cadastro()

    #Aba 2: Lista (Treeview)
        self.aba_lista = ttk.Frame(notebook)
        notebook.add(self.aba_lista, text="Turma (Tabela)")
        self._montar_tabela()

    def _montar_cadastro(self):
        frame=ttk.Frame(self.aba_cadastro, padding=20)
        frame.pack(fill="both", expand=True)

        ttk.Label(frame, text="Nome do aluno").grid(row=0, column=0, sticky="w", pady=5)
        self.entry_nome = ttk.Entry(frame, width=25)
        self.entry_nome.grid(row=0, column=1, pady=5, padx=5)

        ttk.Label(frame, text="Nota Final").grid (row=1, column=0, sticky= "w", pady=5)
        self.entry_nota= ttk.Entry(frame, width=10)
        self.entry_nota.grid(row=1, column=1, sticky="w", pady=5, padx=5)

        ttk.Button(frame, text="Adicionar Tabela", command=self._adicionar_aluno).grid(row=2, column=0, columnspan=2, pady=15)

    def _montar_tabela(self):
        colunas = ("nome", "nota")
        self.tree= ttk.Treeview(self.aba_lista, columns=colunas, show="headings")

        self.tree.heading("nome", text="Nome do aluno")
        self.tree.heading("nota", text="Nota")

        self.tree.column("nome", width=250)
        self.tree.column("nota", width=100, anchor="center")

        #DADOS INCIAIS
        self.tree.insert("", "end", values=("Ana Silva", "9.5"))
        self.tree.insert("", "end", values=("Carlos Souza", "7.0"))

        self.tree.pack(expand=True, fill="both", padx=5, pady=5) 

    def _adicionar_aluno(self):
        nome = self.entry_nome.get()
        nota = self.entry_nota.get()

        if not nome or not nota:
            messagebox.showerror("Erro", "Preencha todos os campos!") 
            return
        
        self.tree.insert("", "end", values=(nome, nota))
        self.entry_nome.delete(0, tk.END)
        self.entry_nota.delete(0, tk.END)
        messagebox.showinfo("Sucesso", "Aluno cadastrado!")

if __name__ == "__main__":
    app= PainelEscolar()
    app.mainloop()
