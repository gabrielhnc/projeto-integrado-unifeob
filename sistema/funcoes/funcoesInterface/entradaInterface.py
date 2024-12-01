from utils.interface import *
del obter_hora, obter_status
from funcoes.funcoesCRUD.entradadb import EntradaDB
from funcoes.funcoesCRUD.usuariodb import UsuarioDB
from funcoes.funcoesCRUD.depositodb import DepositoDB
from funcoes.funcoesCRUD.materialdb import MaterialDB
from models.entrada import Entrada

class EntradaInterface:
    def __init__(self, banco):
        self.entradadb = EntradaDB(banco.conexao, banco.cursor)
        self.usuariodb = UsuarioDB(banco.conexao, banco.cursor)
        self.depositodb = DepositoDB(banco.conexao, banco.cursor)
        self.materialdb = MaterialDB(banco.conexao, banco.cursor)

    def cadastrar_entrada(self):
        print("\n==== Cadastrar Entrada ====")
        idusuario = consultar_e_validar_id(self.usuariodb.consultar_usuarios, self.usuariodb.consultar_usuario_por_id, "usuário")
        if idusuario is None:
            return

        iddeposito = consultar_e_validar_id(self.depositodb.consultar_depositos, self.depositodb.consultar_deposito_por_id, "depósito")
        if iddeposito is None:
            return

        idmaterial = consultar_e_validar_id(self.materialdb.consultar_materiais, self.materialdb.consultar_material_por_id, "material")
        if idmaterial is None:
            return

        data = obter_data(f"\nDigite a data de entrada do material ID {idmaterial} (DD/MM/YYYY) [0 para cancelar]: ")
        if data is None:
            return
        
        while True:
            quantidade = obter_quantidade("Digite a quantidade (em gramas) que está sendo depositada [0 para cancelar]: ")
            if quantidade is None:
                return
            
            entrada = Entrada(idusuario, iddeposito, idmaterial, conversao_data(data), quantidade)

            capacidade_suficiente, quantidade_total = self.depositodb.verificar_capacidade_deposito(entrada)

            if not capacidade_suficiente:
                print(f"\n[!] A quantidade inserida ultrapassa a capacidade máxima do depósito.")
                print(f"Quantidade já PREENCHIDA no depósito: {quantidade_total} g.")
                print("=" * 60)
            else:
                break

        self.entradadb.cadastrar_entrada(entrada)


    def consultar_entradas(self):
        print("\nConsultando entradas...")
        time.sleep(2)
        self.entradadb.consultar_entradas()


    def atualizar_entrada(self):
        print("\n==== Atualizar Entrada ====")
        identrada = consultar_e_validar_id(self.entradadb.consultar_entradas, self.entradadb.consultar_entrada_por_id, "entrada")
        if not identrada:
            return

        print(f"\n[!] ATUALIZANDO INFORMAÇÕES -> Escolha um novo usuario para entrada ID {identrada}")
        idusuario = consultar_e_validar_id(self.usuariodb.consultar_usuarios, self.usuariodb.consultar_usuario_por_id, "usuário")
        if not idusuario:
            return
        
        print(f"\n[!] ATUALIZANDO INFORMAÇÕES -> Escolha um novo depósito para entrada ID {identrada}")
        iddeposito = consultar_e_validar_id(self.depositodb.consultar_depositos, self.depositodb.consultar_deposito_por_id, "depósito")
        if not iddeposito:
            return
        
        print(f"\n[!] ATUALIZANDO INFORMAÇÕES -> Escolha um novo material para entrada ID {identrada}")
        idmaterial = consultar_e_validar_id(self.materialdb.consultar_materiais, self.materialdb.consultar_material_por_id, "material")
        if not idmaterial:
            return
        
        nova_data = obter_data("\nDigite a nova data de entrada (DD/MM/YYYY) [0 para cancelar]: ")
        if nova_data is None:
            return
        
        while True:
            nova_quantidade = obter_quantidade("Digite a nova_quantidade (em gramas) que está sendo depositada [0 para cancelar]: ")
            if nova_quantidade is None:
                return
            
            entrada = Entrada(idusuario, iddeposito, idmaterial, conversao_data(nova_data), nova_quantidade)

            capacidade_suficiente, quantidade_total = self.depositodb.verificar_capacidade_deposito(entrada)

            if not capacidade_suficiente:
                print(f"\n[!] A quantidade inserida ultrapassa a capacidade máxima do depósito.")
                print(f"Quantidade já PREENCHIDA no depósito: {quantidade_total} g.")
                print("=" * 60)
            else:
                break

        self.entradadb.atualizar_entrada(identrada, idusuario, iddeposito, idmaterial, conversao_data(nova_data), nova_quantidade)


    def excluir_entrada(self):
        print("\n==== Excluir Entrada ====")
        identrada = consultar_e_validar_id(self.entradadb.consultar_entradas, self.entradadb.consultar_entrada_por_id, "entrada")
        if identrada is None:
            return

        confirmar = input(f"\nDeseja realmente excluir a entrada com ID {identrada}? (s/n): ").lower()
        if confirmar == 's':
            self.entradadb.excluir_entrada(identrada)
        elif confirmar == 'n':
            print("[!] Exclusão cancelada.")
        else:
            print("[!] Resposta inválida.")
