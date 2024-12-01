from utils.interface import *
del obter_status, obter_quantidade
from funcoes.funcoesCRUD.coletordb import ColetorDB
from funcoes.funcoesCRUD.cidadedb import CidadeDB
from models.coletor import Coletor

class ColetorInterface:
    def __init__(self, banco):
        self.coletordb = ColetorDB(banco.conexao, banco.cursor)
        self.cidadedb = CidadeDB(banco.conexao, banco.cursor)

    def cadastrar_coletor(self):
        print("\n==== Cadastrar Coletor ====")
        nome = input("\nDigite o nome do coletor [0 para cancelar]: ")
        if nome == '0':
            print("[!] Cadastro de coletor cancelado.")
            return

        cnpjCpf = input("Digite o CNPJ ou CPF do coletor: ")
        telefone = input("Digite o telefone do coletor: ")
        endereco = input("Digite o endereço do coletor: ")

        idcidade = consultar_e_validar_id(self.cidadedb.consultar_cidades,self.cidadedb.consultar_cidade_por_id,"cidade")
        if idcidade is None:
            return

        dataCadastro = obter_data("\nDigite a data de cadastro do coletor (DD/MM/YYYY) [0 para cancelar]: ")
        if dataCadastro is None:
            return

        coletor = Coletor(nome, cnpjCpf, telefone, endereco, idcidade, conversao_data(dataCadastro))
        self.coletordb.cadastrar_coletor(coletor)


    def consultar_coletores(self):
        print("\nConsultando coletores...")
        time.sleep(1)
        self.coletordb.consultar_coletores()


    def atualizar_coletor(self):
        print("\n==== Atualizar Coletor ====")
        idcoletor = consultar_e_validar_id(self.coletordb.consultar_coletores,self.coletordb.consultar_coletor_por_id,"coletor")
        if idcoletor is None:
            return

        print(f"\n[!] ATUALIZANDO INFORMAÇÕES -> Coletor ID {idcoletor}")
        novo_nome = input("\nDigite o novo nome do coletor: ")
        novo_cnpjCpf = input("Digite o novo CNPJ ou CPF do coletor: ")
        novo_telefone = input("Digite o novo telefone do coletor: ")
        novo_endereco = input("Digite o novo endereço do coletor: ")

        novo_idcidade = consultar_e_validar_id(self.cidadedb.consultar_cidades,self.cidadedb.consultar_cidade_por_id,"cidade")
        if novo_idcidade is None:
            return

        nova_dataCadastro = obter_data("\nDigite a nova data de cadastro (DD/MM/YYYY) [0 para cancelar]: ")
        if nova_dataCadastro is None:
            return

        self.coletordb.atualizar_coletor(idcoletor, novo_nome, novo_cnpjCpf, novo_telefone, novo_endereco, novo_idcidade, conversao_data(nova_dataCadastro))


    def excluir_coletor(self):
        print("\n==== Excluir Coletor ====")

        idcoletor = consultar_e_validar_id(self.coletordb.consultar_coletores,self.coletordb.consultar_coletor_por_id,"coletor")
        if idcoletor is None:
            return

        confirmar = input(f"\nDeseja realmente excluir o coletor com ID {idcoletor}? (s/n): ").lower()
        if confirmar == 's':
            self.coletordb.excluir_coletor(idcoletor)
        elif confirmar == 'n':
            print("[!] Exclusão cancelada.")
        else:
            print("[!] Resposta inválida. Operação cancelada.")
