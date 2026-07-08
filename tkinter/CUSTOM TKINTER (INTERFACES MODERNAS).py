import customtkinter as ctk
ctk.set_appearance_mode("System")
ctk.set_default_color_theme("blue")

class DashboardModerno(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Dashboard CustomTkinter")
        self.geometry("400x300")
        self.resizable(False, False)
        self._criar_widgets()
    
    def _criar_widgets(self):
        self.label_titulo=ctk.CTkLabel(
            self,
            text="Painel de Controle",
            font=ctk.CTkFont(size=20, weight="bold")
        )
        self.label_titulo.pack(pady=20)

        #Switch para alternar modo escuro/claro
        self.switch_var = ctk.StringVar(value="dark")
        self.switch_tema = ctk.CTkSwitch(
            self,
            text="Modo Escuro",
            command=self._alternar_tema,
            variable=self.switch_var,
            onvalue="dark",
            offvalue="light"
        )
        self.switch_tema.pack(pady=15) 

        #Botão moderno com cores personalizadas de hover e fundo 
        self.btn_acao = ctk.CTkButton(
            self,
            text="Executar Processo",
            command=self._clique_botao,
            fg_color="#10B981",
            hover_color="#059669"
        )
        self.btn_acao.pack(pady=20)

        self.label_status = ctk.CTkLabel(self, text="Status: Aguardando Comando...", font=ctk.CTkFont(size=12))
        self.label_status.pack(pady=10)

    def _alternar_tema(self):
        modo_atual = self.switch_var.get()
        ctk.set_appearance_mode(modo_atual)
        if modo_atual == "dark":
            self.switch_tema.configure(text="Modo Escuro")
        else:
            self.switch_tema.configure(text="Modo Claro")
    def _clique_botao(self):
        self.label_status.configure(text="Status: Processo executado com sucesso!", text_color="10B981")

if __name__ == "__main__":
    app= DashboardModerno()
    app.mainloop()                        