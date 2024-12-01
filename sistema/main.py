
from menus.menu import Menu
from database_conexao.bancodedados import BancoDeDados

# Instancia da classe banco de dados (banco) recebendo os dados para realizar a conexão
if __name__ == "__main__":
    banco = BancoDeDados(host="host", user="user", password="password", database="database")

    banco.conectar()

    # Criando uma instancia da classe 'Menu' e passando o banco
    menu = Menu(banco)

    # Chamando o menu principal
    opcao = menu.exibir_menu_principal()

    banco.desconectar()
