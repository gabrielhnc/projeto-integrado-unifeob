from utils.interface import time, consultar_e_validar_id
from funcoes.funcoesCRUD.cidadedb import CidadeDB
from funcoes.funcoesCRUD.estadodb import EstadoDB
from models.cidade import Cidade

class CidadeInterface:
    def __init__(self, banco):
        self.cidadedb = CidadeDB(banco.conexao, banco.cursor)
        self.estadodb = EstadoDB(banco.conexao, banco.cursor)

    def cadastrar_cidade(self):
        print("\n==== Cadastrar Cidade ====")
        nome = input("\nDigite o nome da cidade [0 para cancelar]: ")
        if nome == '0':
            print("[!] Cadastro de cidade cancelado.")
            return

        idestado = consultar_e_validar_id(self.estadodb.consultar_estados, self.estadodb.consultar_estado_por_id, "estado")
        if not idestado:
            return
        
        cidade = Cidade(nome, idestado)
        self.cidadedb.cadastrar_cidade(cidade)


    def consultar_cidades(self):
        print("\nConsultando cidades...")
        time.sleep(1)
        self.cidadedb.consultar_cidades()


    def atualizar_cidade(self):
        print("\n==== Atualizar Cidade ====")
        idcidade = consultar_e_validar_id(self.cidadedb.consultar_cidades, self.cidadedb.consultar_cidade_por_id, "cidade")
        if not idcidade:
            return
        
        print(f"\n[!] ATUALIZANDO INFORMAÇOES -> Cidade ID {idcidade}")
        novo_nome = input("\nDigite o novo nome da cidade: ")

        novo_idestado = consultar_e_validar_id(self.estadodb.consultar_estados, self.estadodb.consultar_estado_por_id, "estado")
        if not novo_idestado:
            return

        self.cidadedb.atualizar_cidade(idcidade, novo_nome, novo_idestado)


    def excluir_cidade(self):
        print("\n==== Excluir Cidade ====")
        idcidade = consultar_e_validar_id(self.cidadedb.consultar_cidades, self.cidadedb.consultar_cidade_por_id, "cidade")
        if idcidade is None:
            return

        confirmar = input(f"\nDeseja realmente excluir a cidade com ID {idcidade}? (s/n): ").lower()
        if confirmar == 's':
            self.cidadedb.excluir_cidade(idcidade)
        elif confirmar == 'n':
            print("[!] Exclusão cancelada.")
        else:
            print("[!] Resposta inválida.")
