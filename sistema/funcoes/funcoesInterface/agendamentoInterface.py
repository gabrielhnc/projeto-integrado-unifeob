from utils.interface import *
del obter_quantidade
from funcoes.funcoesCRUD.agendamentodb import AgendamentoDB
from funcoes.funcoesCRUD.coletordb import ColetorDB
from models.agendamento import Agendamento

class AgendamentoInterface:
    def __init__(self, banco):
        self.agendamentodb = AgendamentoDB(banco.conexao, banco.cursor)
        self.coletordb = ColetorDB(banco.conexao, banco.cursor)

    def cadastrar_agendamento(self):
        print("\n==== Cadastrar Agendamento ====")
        data = obter_data("\nDigite a data do agendamento (DD/MM/YYYY) [0 para cancelar]: ")
        if data is None:
            return
        
        hora = obter_hora("Digite a hora do agendamento (HH:MM:SS) [0 para cancelar]: ")
        if hora is None:
            return
        
        status = obter_status()
        if status is None:
            return

        idcoletor = consultar_e_validar_id(self.coletordb.consultar_coletores, self.coletordb.consultar_coletor_por_id, "coletor")
        if not idcoletor:
            return

        agendamento = Agendamento(conversao_data(data), hora, status, idcoletor)
        self.agendamentodb.cadastrar_agendamento(agendamento)


    def consultar_agendamentos(self):
        print("\nConsultando agendamentos...")
        time.sleep(2)
        self.agendamentodb.consultar_agendamentos()


    def atualizar_agendamento(self):
        print("\n==== Atualizar Agendamento ====")
        idagendamento = consultar_e_validar_id(self.agendamentodb.consultar_agendamentos, self.agendamentodb.consultar_agendamento_por_id, "agendamento")
        if not idagendamento:
            return

        print(f"\n[!] ATUALIZANDO INFORMAÇÕES -> Agendamento ID {idagendamento}")
        nova_data = obter_data("\nDigite a nova data do agendamento (DD/MM/YYYY): ")
        if nova_data is None:
            return
        
        nova_hora = obter_hora("Digite a nova hora do agendamento (HH:MM:SS): ")
        if nova_hora is None:
            return
        
        novo_status = obter_status("Digite o novo status do agendamento (Pendente, Confirmado, Cancelado): ")
        if novo_status is None:
            return
        
        print(f"\n[!] ATUALIZANDO INFORMAÇÕES -> Escolha um novo coletor para o agendamento ID {idagendamento}")
        novo_idcoletor = consultar_e_validar_id(self.coletordb.consultar_coletores, self.coletordb.consultar_coletor_por_id, "coletor")
        if not novo_idcoletor:
            return

        self.agendamentodb.atualizar_agendamento(idagendamento, conversao_data(nova_data), nova_hora, novo_status, novo_idcoletor)


    def excluir_agendamento(self):
        print("\n==== Excluir Agendamento ====")
        idagendamento = consultar_e_validar_id(self.agendamentodb.consultar_agendamentos, self.agendamentodb.consultar_agendamento_por_id, "agendamento")
        if idagendamento is None:
            return

        confirmar = input(f"\nDeseja realmente excluir o agendamento com ID {idagendamento}? (s/n): ").lower()
        if confirmar == 's':
            self.agendamentodb.excluir_agendamento(idagendamento)
        elif confirmar == 'n':
            print("[!] Exclusão cancelada.")
        else:
            print("[!] Resposta inválida.")
