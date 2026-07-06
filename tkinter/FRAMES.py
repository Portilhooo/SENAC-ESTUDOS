import tkinter as tk

root= tk.Tk()
root.title("Layout com Frames")
root.geometry("500x300")

side = tk.Frame(root, bg="#016316", width=150)
side.pack (side=tk.LEFT, fill= tk.Y)

tk.Label(side, text="MENU", bg="#016316",
            fg="WHITE").pack(pady=20)

main= tk.Frame(root, bg="WHITE")
main.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

tk.Label(main, text="Painel de Controle",
            font=("Arial", 18)).pack(pady=50)

root.mainloop()