import sqlite3
# Este arquivo será responsável por gerenciar o DB nas funções de criação de usuário e deleção

class DB_login:
    ## Atributos
    conexao: sqlite3.Connection
    cursor: sqlite3.Cursor

    ## Construtor
    def __init__(self, nome_db: str):
        self.conexao = sqlite3.connect(nome_db)
        self.cursor = self.conexao.cursor()

        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS usuario
            (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            email TEXT UNIQUE NOT NULL,
            senha TEXT DEFAULT NULL,
            FOREIGN KEY id
            )
        """)

    # Fechar conexão
    def close_db(self):
        self.conexao.close()

    # CREATE - Inserir usuário
    def inserir_usuario(self, email:str, senha:str) -> None:
        try:
            self.cursor.execute("INSERT INTO usuario (email, senha) VALUES(?,?,?)", 
                        (email, senha))
            self.conexao.commit()
        except sqlite3.IntegrityError as e:
            print(f"Usuário já existe: {e}")


    #UPDATE - Atualizar instancia(linha) do item
    def atualizar_item(self, id:int, nome:str, qtd:int, preco:float) -> None:
        self.cursor.execute("UPDATE produto SET nome = ?, qtd = ?, preco = ? WHERE id = ?",
        (nome, qtd, preco, id))
        self.conexao.commit()
        
        if self.cursor.rowcount > 0:
            print("Produto atualizado com sucesso!")
        else:
            raise sqlite3.IntegrityError("Produto não encontrado!")


    #DELETE - Excluir produto
    def excluir_item(self, id) -> None:
        self.cursor.execute("DELETE FROM produto WHERE id = ?", tuple(id))
        self.conexao.commit()
        

        if self.cursor.rowcount > 0:
            print(f"Produto excluido com sucesso!")
        else:
            print("Produto não encontrado!")
