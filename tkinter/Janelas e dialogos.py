import tkinter as tk
from tkinter import ttk, filedialog, messagebox
import os

class LeitorArquivos(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Inspetor de Arquivos")
        self.geometry("350x180")
        
        self._criar_widgets()

    def _criar_widgets(self):
        frame = ttk.Frame(self, padding=20)
        frame.pack(fill="both", expand=True)

        ttk.Label(frame, text="Selecione um arquivo para inspecionar:", font=("Arial", 10)).pack(pady=10)

        ttk.Button(
            frame,
            text="Abrir Explorador de arquivos",
            command=self._selecionar_arquivos
        ).pack(pady=15)

    def _selecionar_arquivos(self):
        #Abertura do dialogo nativo do sistema operacional
        caminho_arquivo=filedialog.askopenfilename(
            title="Selecione um arquivo qualquer",
            filetypes=[("Todos os Aquivos", "*.*"), ("Arquivos de Texto", "*.txt"), ("Arquivos Python", "*.py")]
        )        
        if caminho_arquivo:
            self._abrir_janela_detalhes(caminho_arquivo)
        else:
            messagebox.showinfo("Aviso", "Nenhum arquivo foi selecionado") 

    def _abrir_janela_detalhes(self, caminho):
        #Criação da janela secundaria independente
        top= tk.Toplevel(self)
        top.title("Detalhes do Arquivo")
        top.geometry("400x220")
        top.resizable(False, False)

        #Extração de metadados simples
        nome_arquivo= os.path.basename(caminho)
        tamanho_bytes= os.path.getsize(caminho)
        tamanho_kb= round(tamanho_bytes / 1024, 2)

        frame_top = ttk.Frame(top, padding=20)
        frame_top.pack(fill="both", expand=True)

        ttk.Label(frame_top, text="Análise Concluída", font=("Arial", 12, "bold")).pack(pady=5)
        ttk.Label(frame_top, text=f"Nome: {nome_arquivo}").pack(anchor="w", pady=3)
        ttk.Label(frame_top, text=f"Tamanho: {tamanho_kb} KB ({tamanho_bytes} bytes)").pack(anchor="w",pady=3)

        ttk.Label(frame_top, text="Caminho Absoluto").pack(anchor="w", pady=(10, 0))
        entry_caminho= ttk.Entry(frame_top, width=50)
        entry_caminho.insert(0, caminho)
        entry_caminho.config(state="readonly")
        entry_caminho.pack(fill="x", pady=2)

        ttk.Button(frame_top, text="Fechar", command=top.destroy).pack(pady=10)

if __name__ == "__main__":
    app =LeitorArquivos()
    app.mainloop()          