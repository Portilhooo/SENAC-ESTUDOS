import tkinter as tk

class MinhaAplicacao(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("App POO")
        self.geometry("400x300")
        self.criar_widgets()

    def criar_widgets(self):
        label = tk.Label(self, text="Bem-vindo à POO!")
        label.pack(pady=20)
        button = tk.Button(self, text="Clique-me", command=self.ao_clicar)
        button.pack(pady=10)

    def ao_clicar(self):
        print("Botão clicando na classe!")

if __name__ == "__main__":
    app = MinhaAplicacao()  
    app.mainloop()            