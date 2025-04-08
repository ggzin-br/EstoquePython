import db_crud
from simple_term_menu import TerminalMenu

#declaracao de variaveis:
optionsMenu = []
optionsUser = []
oprionsCrud = []
menu_entry_index = ''


#funcoes para abrir os menus:

#func para mostrar o menu do crud/ger
def show_menu_crud():
    global optionsCrud 
    optionsCrud = ["[1]Listar produtos","[2]Adicionar produto","[3]Remover produto","[4]Atualizar produto","[5]Sair"]
    terminal_menu = TerminalMenu(optionsCrud,title="\nO que deseja fazer??\n")
    global menu_entry_index 
    menu_entry_index= terminal_menu.show()


#func para mostras o menu dos usuarios
def show_menu_user():
    global optionsUser
    optionsUser = ["[1]listar usuários","[2]Adicionar usuários","[3]remover usuários","[4]Sair"]
    terminal_menu = TerminalMenu(optionsUser,title="\nO que deseja fazer??\n")
    global menu_entry_index 
    menu_entry_index= terminal_menu.show()


#funcoes para operacoes nos menus

#func para realizar operacoes no menu dos produtos
def menu_estoque_produto(): 
    db:db_crud.DB_crud = db_crud.DB_crud("mercado_estoque.db")
    nome:str
    preco:float
    qtd:int
    id:int
    while True:
        show_menu_crud()
        choice = optionsCrud[menu_entry_index]
        match choice:
            case "[1]Listar produtos":
               for i in db.listar_produtos():
                   print(i)
            case "[2]Adicionar produto":
                nome = input("Digite o nome do produto: ").strip()
                preco = float(input("Digite o preço do produto: ").strip())
                qtd = int(input("Digite a quantidade em estoque do produto: ").strip())
                db.inserir_produto(nome,preco,qtd)
            case "[3]Remover produto":
                id = input("Digite o id do produto que deseja ser deletado: ").strip()
                db_crud.excluir_item(id)
            case "[4]Atualizar produto":
                id = input("digite o id do produto que deseja alterar: ").strip()
                nome = input("Digite o novo nome do produto: ").strip()
                preco = float(input("Digite o  novo preço do produto: ").strip())
                qtd = int(input("Digite a  nova quantidade em estoque do produto: ").strip())
                db.atualizar_item(nome,preco,qtd,id)
            case "[5]Sair":
                print("Saindo, volte sempre!")
                break

#func para realizar operacoes no menu dos produtos
def menu_estoque_produto(): 
    db:db_crud.DB_crud = db_crud.DB_crud("mercado_estoque.db")
    nome:str
    preco:float
    qtd:int
    id:int
    while True:
        show_menu_crud()
        choice = optionsCrud[menu_entry_index]
        match choice:
            case "[1]Listar produtos":
               for i in db.listar_produtos():
                   print(i)
            case "[2]Adicionar produto":
                nome = input("Digite o nome do produto: ").strip()
                preco = float(input("Digite o preço do produto: ").strip())
                qtd = int(input("Digite a quantidade em estoque do produto: ").strip())
                db.inserir_produto(nome,preco,qtd)
            case "[3]Remover produto":
                id = input("Digite o id do produto que deseja ser deletado: ").strip()
                db_crud.excluir_item(id)
            case "[4]Atualizar produto":
                id = input("digite o id do produto que deseja alterar: ").strip()
                nome = input("Digite o novo nome do produto: ").strip()
                preco = float(input("Digite o  novo preço do produto: ").strip())
                qtd = int(input("Digite a  nova quantidade em estoque do produto: ").strip())
                db.atualizar_item(nome,preco,qtd,id)
            case "[5]Sair":
                print("Saindo, volte sempre!")
                break







def main(): 
    while True:
        menu_estoque_produto()





if __name__ == "__main__":
    main()
