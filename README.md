# Projeto CRUD e SQL
### Feito por 2 Pedro's 😎

Para rodar é só usar o `python3 ./main.py` na linha de comando.

## Separação dos arquivos fonte
Os arquivos foram separados baseados nas funcionalidades no projeto. No total 2 partes, sendo a de usuário e crud.

## Menu
O menu foi feito utilizando uma biblioteca bem legal chamada simple_term_menu, então precisa dar um `pip3 install simple_term_menu` :)

## O sistema de login
Esse sistema utiliza uma variável definida em tempo de execução contendo o id do usuário logado. Este id é atribuido em uma tuple se uma QUERY de SELECT for bem sucedida em buscar pelo email e senha, caso falhar será None. Nenhuma chave estrangeira foi usada nas tabelas.