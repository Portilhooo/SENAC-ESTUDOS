import sqlite3
conexao=sqlite3.connect("produtos.db")
cursor=conexao.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS produto(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        preco REAL NOT NULL
    )               
        """)

conexao.commit()
while True:
    print("\n===Mercadinho===")
    print("1 - Cadastro")
    print("2 - Listar")
    print("3 - Sair")
    
    opcao=input("Escolha:")
    
    if opcao=="1":
        nome = input(("Nome do produto:"))
        preco=float(input("Preço:"))
        cursor.execute(
            "INSERT INTO produto (nome, preco) VALUES (?,?)",
            (nome,preco)
        )
        conexao.commit()
        print("Produto Cadastrado com sucesso")
    elif opcao=="2":
        cursor.execute("SELECT *FROM produto")
        produtos=cursor.fetchall()
        if len(produtos)==0:
            print("Nenhum produto cadastrado")
        else:
            print("Produtos cadastrados")
            for produto in produtos:
                print(
                    f"ID:{produto[0]}|"
                    f"nome:{produto[1]}|"
                    f"preco:{produto[2]:.2f}"
                )
    elif opcao=="3":
        print("Sistema encerrado")
        break
    
    else:
        print("Opção inválida")
conexao.close()        