import sqlite3
# Este arquivo será responsável por gerenciar o DB nas funções básicas de CRUD

class DB_crud:
    ## Atributos
    conexao: sqlite3.Connection
    cursor: sqlite3.Cursor

    ## Construtor
    def __init__(self, nome_db: str):
        self.conexao = sqlite3.connect(nome_db)
        self.cursor = self.conexao.cursor()

        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS produto
            (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT UNIQUE NOT NULL,
            qtd INTEGER NOT NULL,
            preco FLOAT NOT NULL
            )
        """)

    # Fechar conexão
    def close_db(self):
        self.conexao.close()

    # CREATE - Inserir item
    def inserir_produto(self, nome:str, qtd:int, preco:float) -> None:
        try:
            self.cursor.execute("INSERT INTO produto (nome,qtd,preco) VALUES(?,?,?)", 
                        (nome,qtd,preco))
            self.conexao.commit()
            print(f"Produto \"{nome}\" inserido com sucesso")
        except sqlite3.IntegrityError:
            print("Erro: Produto já existente")


    # READ - Listar ou ler produtos 
    def listar_produtos(self) -> list[str]:
        produtos: list[str]

        self.cursor.execute("SELECT * FROM produto")
        produtos = self.cursor.fetchall()
        return produtos


    #UPDATE - Atualizar instancia(linha) do item
    def atualizar_item(self, id:int, nome:str, qtd:int, preco:float):
        self.cursor.execute("UPDATE produto SET nome = ?, qtd = ?, preco = ? WHERE id = ?",
        (nome, qtd, preco, id))
        self.conexao.commit()
        
        if self.cursor.rowcount > 0:
            print("Produto atualizado com sucesso!")
        else:
            print("Produto não encontrado!")


    #DELETE - Excluir produto
    def excluir_item(self, id) -> None:
        self.cursor.execute("DELETE FROM produto WHERE id = ?", tuple(id))
        self.conexao.commit()

        if self.cursor.rowcount > 0:
            print("Produto excluido com sucesso!")
        else:
            print("Produto não encontrado!")
