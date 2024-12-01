from utils.interface import *
from funcoes.funcoesCRUD.estadodb import EstadoDB
from models.estado import Estado

class EstadoInterface:
    def __init__(self, banco):
        self.estadodb = EstadoDB(banco.conexao, banco.cursor)
    
    def cadastrar_estado(self):
        print("\n==== Cadastrar Estado ====")
        idestado = input("\nDigite a sigla do estado (2 letras) [0 para cancelar]: ").upper()
        if idestado == '0':
            print("[!] Cadastro de estado cancelado.")
            return
        elif len(idestado) != 2 or not idestado.isalpha():
            print("Erro: O ID do estado deve ter exatamente 2 letras.")
            return

        nome_estado = input("Digite o nome do estado: ")
        if not nome_estado:
            print("Erro: O nome do estado não pode estar vazio.")
            return

        estado = Estado(idestado, nome_estado)
        self.estadodb.cadastrar_estado(estado)


    def consultar_estados(self):
        print("\nConsultando estados...")
        time.sleep(1)
        self.estadodb.consultar_estados()


    def atualizar_estado(self):
        print("\n==== Atualizar Estado ====")
        id_estado = consultar_e_validar_id(self.estadodb.consultar_estados,self.estadodb.consultar_estado_por_id,"estado")
        if id_estado is None:
            return

        novo_nome = input("\nDigite o novo nome do estado: ")
        if not novo_nome:
            print("Erro: O nome do estado não pode estar vazio.")
            return

        self.estadodb.atualizar_estado(id_estado, novo_nome)


    def excluir_estado(self):
        print("\n==== Excluir Estado ====")
        id_estado = consultar_e_validar_id(self.estadodb.consultar_estados,self.estadodb.consultar_estado_por_id,"estado")
        if id_estado is None:
            return

        confirmar = input(f"\nDeseja realmente excluir o estado com ID '{id_estado}'? (s/n): ").lower()
        if confirmar == 's':
            self.estadodb.excluir_estado(id_estado)
        elif confirmar == 'n':
            print("[!] Exclusão cancelada.")
        else:
            print("Resposta inválida. Digite 's' para sim ou 'n' para não.")
