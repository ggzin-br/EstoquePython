import db_crud
from simple_term_menu import TerminalMenu

#declaracao de variaveis:
optionsMenu = []
optionsUser = []
oprionsCrud = []
menu_entry_index = ''
choice = ''


#funcoes para abrir os menus:


#func para mostrar o menu principal
def show_menu_main():
    global optionsMenu
    optionsMenu = ["[1]Menu de usuários","[2]Menu de Produtos","[3]Sair"]
    terminal_menu = TerminalMenu(optionsMenu,title="\nO que deseja fazer??\n")
    global menu_entry_index
    menu_entry_index = terminal_menu.show()


#func para mostrar o menu do crud/gerenciamento de produtos
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
        global choice
        choice = optionsCrud[menu_entry_index]
        match choice:
            case "[1]Listar produtos":
               for i in db.listar_produtos():
                   print(i)
            case "[2]Adicionar produto":
                nome = input("Digite o nome do produto: ").strip()
                preco = float(input("Digite o preço do produto: ").strip())
                qtd = int(input("Digite a quantidade em estoque do produto: ").strip())
                db.inserir_produto(nome,qtd,preco)
            case "[3]Remover produto":
                id = input("Digite o id do produto que deseja ser deletado: ").strip()
                db.excluir_item(id)
            case "[4]Atualizar produto":
                id = int(input("digite o id do produto que deseja alterar: ").strip())
                nome = input("Digite o novo nome do produto: ").strip()
                preco = float(input("Digite o  novo preço do produto: ").strip())
                qtd = int(input("Digite a  nova quantidade em estoque do produto: ").strip())
                db.atualizar_item(id,nome,qtd,preco)
            case "[5]Sair":
                print("Saindo, volte sempre!")
                break


#func para realizar operacoes no menu dos usuarios
def menu_users(): 
    db:db_crud.DB_crud = db_crud.DB_crud("mercado_estoque.db")#ajustar
    email: str
    senha: str
    id: int 
    while True:
        show_menu_user()
        global choice
        choice = optionsUser[menu_entry_index]
        match choice:
            case "[1]Listar usuários": ...
            #    for i in db.listar_produtos():
            #        print(i)
            case "[2]Adicionar usuário": ...
                # email = input("Digite o email do usuário: ").strip()
                # senha = input("digite a senha do usuário").strip()
                # db.inserir_usuario(email,senha)
            case "[3]Remover usuário": ...
                # id = int(input("Digite o id do produto que deseja ser deletado: ").strip())
                # db_crud.excluir_item(id)
            case "[4]Sair":
                print("Saindo, volte sempre!")
                break







def main(): 
    while True:
        global choice
        show_menu_main()
        choice = optionsMenu[menu_entry_index]
        match choice:
            case "[1]Menu de usuários":
                  menu_users()
            case "[2]Menu de Produtos":
                    menu_estoque_produto()
            case "[3]Sair":
                print("Saindo, volte sempre!")
                break






if __name__ == "__main__":
    main()
