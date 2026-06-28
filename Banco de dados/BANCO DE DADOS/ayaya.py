import tkinter as tk

janela = tk.Tk() #chamando a biblioteca
janela.title("Teste") #definindo um titulo na aba superior esquerda
janela.geometry("800x600") #escolhendo a resolução da janela

titulo=tk.Label( #Definindo um nome de variavel para chamar uma função da biblioteca tkinter para fazer o titulo central
    janela,
    text="teste banco",
    font=("Arial", 16, "bold")
)

titulo.pack(pady=10)
frame_dados=tk.LabelFrame(
    janela,
    text="banco teste",
    padx=10,
    pady=10
)
frame_dados.pack(
    fill="x",
    padx=10,
    pady=10
)

tk.Label(
    frame_dados,
    text=
).grid (row=1, column=0)

janela.mainloop()