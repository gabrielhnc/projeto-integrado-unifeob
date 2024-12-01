from utils.interface import *
del obter_hora, obter_status
from funcoes.funcoesCRUD.saidadb import SaidaDB
from funcoes.funcoesCRUD.depositodb import DepositoDB
from funcoes.funcoesCRUD.coletordb import ColetorDB
from funcoes.funcoesCRUD.materialdb import MaterialDB
from models.saida import Saida

class SaidaInterface:
    def __init__(self, banco):
        self.saidadb = SaidaDB(banco.conexao, banco.cursor)
        self.depositodb = DepositoDB(banco.conexao, banco.cursor)
        self.coletordb = ColetorDB(banco.conexao, banco.cursor)
        self.materialdb = MaterialDB(banco.conexao, banco.cursor)

    def cadastrar_saida(self):
        print("\n==== Cadastrar Saída ====")
        iddeposito = consultar_e_validar_id(self.depositodb.consultar_depositos, self.depositodb.consultar_deposito_por_id, "depósito")
        if iddeposito is None:
            return

        idcoletor = consultar_e_validar_id(self.coletordb.consultar_coletores, self.coletordb.consultar_coletor_por_id, "coletor")
        if idcoletor is None:
            return

        idmaterial = consultar_e_validar_id(self.materialdb.consultar_materiais, self.materialdb.consultar_material_por_id, "material")
        if idmaterial is None:
            return

        dataSaida = obter_data(f"\nDigite a data de saída do material ID {idmaterial} para o coletor ID {idcoletor} (DD/MM/YYYY) [0 para cancelar]: ")
        if dataSaida is None:
            return

        quantidade = obter_quantidade("Digite a quantidade (em gramas) que esta será alocada no coletor [0 para cancelar]: ")
        if quantidade is None:
            return

        saida = Saida(iddeposito, idcoletor, idmaterial, conversao_data(dataSaida), quantidade)
        self.saidadb.cadastrar_saida(saida)


    def consultar_saidas(self):
        print("\nConsultando saidas...")
        time.sleep(1)
        self.saidadb.consultar_saidas()


    def atualizar_saida(self):
        print("\n==== Atualizar Saída ====")
        idsaida = consultar_e_validar_id(self.saidadb.consultar_saidas, self.saidadb.consultar_saida_por_id, "saída")
        if idsaida is None:
            return

        print(f"\n[!] ATUALIZANDO INFORMAÇÕES -> Escolha um novo depósito para saída ID {idsaida}")
        iddeposito = consultar_e_validar_id(self.depositodb.consultar_depositos, self.depositodb.consultar_deposito_por_id, "depósito")
        if iddeposito is None:
            return

        print(f"\n[!] ATUALIZANDO INFORMAÇÕES -> Escolha um novo coletor para saída ID {idsaida}")
        idcoletor = consultar_e_validar_id(self.coletordb.consultar_coletores, self.coletordb.consultar_coletor_por_id, "coletor")
        if idcoletor is None:
            return

        print(f"\n[!] ATUALIZANDO INFORMAÇÕES -> Escolha um novo material para saída ID {idsaida}")
        idmaterial = consultar_e_validar_id(self.materialdb.consultar_materiais, self.materialdb.consultar_material_por_id, "material")
        if idmaterial is None:
            return

        nova_dataSaida = obter_data("\nDigite a nova data de saída (DD/MM/YYYY): ")
        if nova_dataSaida is None:
            return

        nova_quantidade = obter_quantidade("Digite a nova quantidade (g): ")
        if nova_quantidade is None:
            return

        self.saidadb.atualizar_saida(idsaida, iddeposito, idcoletor, idmaterial, conversao_data(nova_dataSaida), nova_quantidade)


    def excluir_saida(self):
        print("\n==== Excluir Saída ====")
        idsaida = consultar_e_validar_id(self.saidadb.consultar_saidas, self.saidadb.consultar_saida_por_id, "saída")
        if idsaida is None:
            return

        confirmar = input(f"\nDeseja realmente excluir a saída com ID {idsaida}? (s/n): ").lower()
        if confirmar == 's':
            self.saidadb.excluir_saida(idsaida)
        elif confirmar == 'n':
            print("[!] Exclusão cancelada.")
        else:
            print("[!] Resposta inválida.")
