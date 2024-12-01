from utils.interface import *
del obter_status
from funcoes.funcoesCRUD.depositodb import DepositoDB
from funcoes.funcoesCRUD.cidadedb import CidadeDB
from models.deposito import Deposito

class DepositoInterface:
    def __init__(self, banco):
        self.depositodb = DepositoDB(banco.conexao, banco.cursor)
        self.cidadedb = CidadeDB(banco.conexao, banco.cursor)

    def cadastrar_deposito(self):
        print("\n==== Cadastrar Depósito ====")

        nome = input("\nDigite o nome do depósito [0 para cancelar]: ")
        if nome == '0':
            print("[!] Cadastro de depósito cancelado.")
            return

        endereco = input("Digite o endereço do depósito: ")
        cep = input("Digite o CEP do depósito: ")

        idcidade = consultar_e_validar_id(self.cidadedb.consultar_cidades,self.cidadedb.consultar_cidade_por_id,"cidade")
        if idcidade is None:
            return

        telefone = input("\nDigite o telefone do depósito: ")

        capacidade_maxima = obter_quantidade("Digite a capacidade máxima do depósito (em quilos) [0 para cancelar]: ")
        if capacidade_maxima is None:
            return

        data_cadastro = obter_data("Digite a data de cadastro do depósito (DD/MM/YYYY) [0 para cancelar]: ")
        if data_cadastro is None:
            return

        hora_abertura = obter_hora("Digite a hora de abertura do depósito (HH:MM:SS) [0 para cancelar]: ")
        if hora_abertura is None:
            return

        hora_fechamento = obter_hora("Digite a hora de fechamendo do depósito (HH:MM:SS) [0 para cancelar]: ")
        if hora_fechamento is None:
            return

        deposito = Deposito(nome, endereco, cep, idcidade, telefone, capacidade_maxima,conversao_data(data_cadastro), hora_abertura, hora_fechamento)
        self.depositodb.cadastrar_deposito(deposito)


    def consultar_depositos(self):
        print("\nConsultando depósitos...")
        time.sleep(1)
        self.depositodb.consultar_depositos()


    def atualizar_deposito(self):
        print("\n==== Atualizar Depósito ====")
        iddeposito = consultar_e_validar_id(self.depositodb.consultar_depositos,self.depositodb.consultar_deposito_por_id,"depósito")
        if iddeposito is None:
            return

        print(f"\n[!] ATUALIZANDO INFORMAÇÕES -> Depósito ID {iddeposito}")
        nome = input("Digite o novo nome do depósito: ")
        endereco = input("Digite o novo endereço do depósito: ")
        cep = input("Digite o novo CEP do depósito: ")

        idcidade = consultar_e_validar_id(self.cidadedb.consultar_cidades,self.cidadedb.consultar_cidade_por_id,"cidade")
        if idcidade is None:
            return

        telefone = input("Digite o novo telefone do depósito: ")

        capacidade_maxima = obter_quantidade("Digite a nova capacidade máxima do depósito (em gramas) [0 para cancelar]: ")
        if capacidade_maxima is None:
            return

        data_cadastro = obter_data("\nDigite a nova data de cadastro do depósito (DD/MM/YYYY): ")
        if data_cadastro is None:
            return

        hora_abertura = obter_hora("\nDigite a nova hora de abertura do depósito (HH:MM): ")
        if hora_abertura is None:
            return

        hora_fechamento = obter_hora("\nDigite a nova hora de fechamento do depósito (HH:MM): ")
        if hora_fechamento is None:
            return

        self.depositodb.atualizar_deposito(iddeposito, nome, endereco, cep, idcidade, telefone,capacidade_maxima, conversao_data(data_cadastro), hora_abertura, hora_fechamento)


    def excluir_deposito(self):
        print("\n==== Excluir Depósito ====")
        iddeposito = consultar_e_validar_id(self.depositodb.consultar_depositos,self.depositodb.consultar_deposito_por_id,"depósito")
        if iddeposito is None:
            return

        confirmar = input(f"\nDeseja realmente excluir o depósito com ID {iddeposito}? (s/n): ").lower()
        if confirmar == 's':
            self.depositodb.excluir_deposito(iddeposito)
        elif confirmar == 'n':
            print("[!] Exclusão cancelada.")
        else:
            print("[!] Resposta inválida.")
