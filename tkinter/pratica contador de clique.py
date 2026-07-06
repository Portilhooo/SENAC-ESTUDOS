import tkinter as tk

def main():
    root= tk.Tk()
    root.title("Contador"), root.geometry("360x200")

    contador= tk.IntVar(value=0)
    def incrementar(): contador.set(contador.get() + 1)

    tk.Label(root, textvariable=contador, font=("Arial", 30)).pack(pady=20)
    tk.Button(root, text="Clique aqui", command=incrementar).pack()

    root.mainloop()
if __name__ == "__main__": main()

