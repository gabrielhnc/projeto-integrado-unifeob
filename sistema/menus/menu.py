from utils.conexaoInterface import ConexaoInterface
import time
import sys
import pyfiglet

# Menu recebendo o banco conectado do arquivo 'main.py'

class Menu:
    def __init__(self, banco):
        self.sistema = ConexaoInterface(banco)

    def animacao_menu(self, titulo):
        grande_titulo = pyfiglet.figlet_format(titulo, font="standard", width=80)
        for letra in grande_titulo:
            sys.stdout.write(letra)
            sys.stdout.flush()
            time.sleep(0.0005)

    def exibir_menu_principal(self):
        while True:
            self.animacao_menu("SISTEMA RECICLA")
            print("=" * 60)
            print("[1] Cadastrar Dados")
            print("[2] Atualizar Dados")
            print("[3] Excluir Dados")
            print("[4] Consultar Dados")
            print("[5] Ranking")
            print("\n[0] Sair")
            print("=" * 60)
            escolha = input("Escolha uma opção: ").strip()
            print("=" * 60)

            if escolha == '1':
                self.exibir_menu_cadastrar()
            elif escolha == '2':
                self.exibir_menu_atualizar()
            elif escolha == '3':
                self.exibir_menu_excluir()
            elif escolha == '4':
                self.exibir_menu_consultar()
            elif escolha == '5':
                self.exibir_menu_ranking()
            elif escolha == '0':
                print("\nSaindo do Sistema...")
                time.sleep(2)
                break
            else:
                print("\n[!] OPÇÃO INVÁLIDA. Tente novamente.\n")

    def exibir_menu_cadastrar(self):
        while True:
            self.animacao_menu("Cadastrar Dados")
            print("=" * 60)
            print("[1] Tipo de usuário")
            print("[2] Usuário")
            print("[3] Categoria")
            print("[4] Material")
            print("[5] Estado")
            print("[6] Cidade")
            print("[7] Coletor")
            print("[8] Agendamento")
            print("[9] Depósito")
            print("[10] Entrada")
            print("[11] Saída")
            print("\n[0] Voltar ao Menu Principal")
            print("=" * 60)
            escolha = input("Escolha uma opção: ").strip()
            print("=" * 60)

            if escolha == '1':
                self.sistema.tipo_usuario.cadastrar_tipo_usuario()
            elif escolha == '2':
                self.sistema.usuario.cadastrar_usuario()
            elif escolha == '3':
                self.sistema.categoria.cadastrar_categoria()
            elif escolha == '4':
                self.sistema.material.cadastrar_material()
            elif escolha == '5':
                self.sistema.estado.cadastrar_estado()
            elif escolha == '6':
                self.sistema.cidade.cadastrar_cidade()
            elif escolha == '7':
                self.sistema.coletor.cadastrar_coletor()
            elif escolha == '8':
                self.sistema.agendamento.cadastrar_agendamento()
            elif escolha == '9':
                self.sistema.deposito.cadastrar_deposito()
            elif escolha == '10':
                self.sistema.entrada.cadastrar_entrada()
            elif escolha == '11':
                self.sistema.saida.cadastrar_saida()
            elif escolha == '0':
                break
            else:
                print("\n[!] OPÇÃO INVÁLIDA. Tente novamente.\n")

    def exibir_menu_atualizar(self):
        while True:
            self.animacao_menu("Atualizar Dados")
            print("=" * 60)
            print("[1] Tipo de usuário")
            print("[2] Usuário")
            print("[3] Categoria")
            print("[4] Material")
            print("[5] Estado")
            print("[6] Cidade")
            print("[7] Coletor")
            print("[8] Agendamento")
            print("[9] Depósito")
            print("[10] Entrada")
            print("[11] Saída")
            print("\n[0] Voltar ao Menu Principal")
            print("=" * 60)
            escolha = input("Escolha uma opção: ").strip()
            print("=" * 60)

            if escolha == '1':
                self.sistema.tipo_usuario.atualizar_tipo_usuario()
            elif escolha == '2':
                self.sistema.usuario.atualizar_usuario()
            elif escolha == '3':
                self.sistema.categoria.atualizar_categoria()
            elif escolha == '4':
                self.sistema.material.atualizar_material()
            elif escolha == '5':
                self.sistema.estado.atualizar_estado()
            elif escolha == '6':
                self.sistema.cidade.atualizar_cidade()
            elif escolha == '7':
                self.sistema.coletor.atualizar_coletor()
            elif escolha == '8':
                self.sistema.agendamento.atualizar_agendamento()
            elif escolha == '9':
                self.sistema.deposito.atualizar_deposito()
            elif escolha == '10':
                self.sistema.entrada.atualizar_entrada()
            elif escolha == '11':
                self.sistema.saida.atualizar_saida()
            elif escolha == '0':
                break
            else:
                print("\n[!] OPÇÃO INVÁLIDA. Tente novamente.\n")

    def exibir_menu_excluir(self):
        while True:
            self.animacao_menu("Excluir Dados")
            print("=" * 60)
            print("[1] Tipo de usuário")
            print("[2] Usuário")
            print("[3] Categoria")
            print("[4] Material")
            print("[5] Estado")
            print("[6] Cidade")
            print("[7] Coletor")
            print("[8] Agendamento")
            print("[9] Depósito")
            print("[10] Entrada")
            print("[11] Saída")
            print("\n[0] Voltar ao Menu Principal")
            print("=" * 60)
            escolha = input("Escolha uma opção: ").strip()
            print("=" * 60)

            if escolha == '1':
                self.sistema.tipo_usuario.excluir_tipo_usuario()
            elif escolha == '2':
                self.sistema.usuario.excluir_usuario()
            elif escolha == '3':
                self.sistema.categoria.excluir_categoria()
            elif escolha == '4':
                self.sistema.material.excluir_material()
            elif escolha == '5':
                self.sistema.estado.excluir_estado()
            elif escolha == '6':
                self.sistema.cidade.excluir_cidade()
            elif escolha == '7':
                self.sistema.coletor.excluir_coletor()
            elif escolha == '8':
                self.sistema.agendamento.excluir_agendamento()
            elif escolha == '9':
                self.sistema.deposito.excluir_deposito()
            elif escolha == '10':
                self.sistema.entrada.excluir_entrada()
            elif escolha == '11':
                self.sistema.saida.excluir_saida()
            elif escolha == '0':
                break
            else:
                print("\n[!] OPÇÃO INVÁLIDA. Tente novamente.\n")

    def exibir_menu_consultar(self):
        while True:
            self.animacao_menu("Consultar Dados")
            print("=" * 60)
            print("[1] Tipo de usuário")
            print("[2] Usuário")
            print("[3] Categoria")
            print("[4] Material")
            print("[5] Estado")
            print("[6] Cidade")
            print("[7] Coletor")
            print("[8] Agendamento")
            print("[9] Depósito")
            print("[10] Entrada")
            print("[11] Saída")
            print("\n[0] Voltar ao Menu Principal")
            print("=" * 60)
            escolha = input("Escolha uma opção: ").strip()
            print("=" * 60)

            if escolha == '1':
                self.sistema.tipo_usuario.consultar_tipos_usuario()
            elif escolha == '2':
                self.sistema.usuario.consultar_usuarios()
            elif escolha == '3':
                self.sistema.categoria.consultar_categorias()
            elif escolha == '4':
                self.sistema.material.consultar_materiais()
            elif escolha == '5':
                self.sistema.estado.consultar_estados()
            elif escolha == '6':
                self.sistema.cidade.consultar_cidades()
            elif escolha == '7':
                self.sistema.coletor.consultar_coletores()
            elif escolha == '8':
                self.sistema.agendamento.consultar_agendamentos()
            elif escolha == '9':
                self.sistema.deposito.consultar_depositos()
            elif escolha == '10':
                self.sistema.entrada.consultar_entradas()
            elif escolha == '11':
                self.sistema.saida.consultar_saidas()
            elif escolha == '0':
                break
            else:
                print("\n[!] OPÇÃO INVÁLIDA. Tente novamente.\n")

    def exibir_menu_ranking(self):
        while True:
            self.animacao_menu("Ranking de Usuarios")
            print("=" * 60)
            print("[1] Consultar Ranking Completo")
            print("[2] Consultar Ranking por Data")
            print("[3] Materiais Depositados por Usuário")
            print("\n[0] Voltar ao Menu Principal")
            print("=" * 60)
            escolha = input("Escolha uma opção: ").strip()
            print("=" * 60)

            if escolha == '1':
                self.sistema.ranking.consultar_ranking_usuarios()
            elif escolha == '2':
                self.sistema.ranking.consultar_ranking_por_data()
            elif escolha == '3':
                self.sistema.ranking.consultar_materiais_depositados()
            elif escolha == '0':
                break
            else:
                print("\n[!] OPÇÃO INVÁLIDA. Tente novamente.\n")
