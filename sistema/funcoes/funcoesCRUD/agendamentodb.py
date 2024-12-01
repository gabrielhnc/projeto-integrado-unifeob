from utils.crud import *

class AgendamentoDB:
    def __init__(self, conexao, cursor):
        self.conexao = conexao
        self.cursor = cursor
        
    def cadastrar_agendamento(self, agendamento):
        try:
            sql_query = "INSERT INTO agendamento (dataAgendamento, hora, statusAgendamento, coletor_idcoletor) VALUES (%s, %s, %s, %s)"
            valores = (
                agendamento.get_data(), 
                agendamento.get_hora(), 
                agendamento.get_status(), 
                agendamento.get_idcoletor() 
            )
            self.cursor.execute(sql_query, valores)
            self.conexao.commit()
            print(f"\n[+] Agendamento para o coletor ID {agendamento.get_idcoletor()} cadastrado com sucesso!")
        except Error as e:
            self.conexao.rollback()
            print(f"Erro ao cadastrar dados: {e}")


    def consultar_agendamentos(self):
        try:
            sql_query = """
            SELECT 
                agendamento.idagendamento, 
                agendamento.dataAgendamento, 
                agendamento.hora, 
                agendamento.statusAgendamento, 
                coletor.nome
            FROM 
                agendamento 
            INNER JOIN 
                coletor ON agendamento.coletor_idcoletor = coletor.idcoletor
            ORDER BY idagendamento ASC
            """
            self.cursor.execute(sql_query)
            agendamentos = self.cursor.fetchall()
            if agendamentos:
                print("\n=== Agendamentos Cadastrados ===")
                headers = ["ID Agendamento", "Data", "Hora", "Status", "Nome Coletor"]
                print(tabulate(agendamentos, headers=headers, tablefmt="fancy_grid"))
            else:
                print("\n[!] Nenhum agendamento encontrado.")
        except Error as e:
            print(f"Erro ao buscar dados: {e}")


    def consultar_agendamento_por_id(self, idagendamento):
        try:
            sql_query = """
            SELECT 
                agendamento.idagendamento, 
                agendamento.dataAgendamento, 
                agendamento.hora, 
                agendamento.statusAgendamento, 
                coletor.nome
            FROM 
                agendamento 
            INNER JOIN 
                coletor ON agendamento.coletor_idcoletor = coletor.idcoletor
            WHERE 
                agendamento.idagendamento = %s
            """
            self.cursor.execute(sql_query, (idagendamento,))
            agendamento = self.cursor.fetchone()
            if agendamento:
                print("\n=== Agendamento Escolhido ===")
                headers = ["ID Agendamento", "Data", "Hora", "Status", "Nome Coletor"]
                print(tabulate([agendamento], headers=headers, tablefmt="fancy_grid"))
                return agendamento
            else:
                print(f"[!] Nenhum agendamento com ID {idagendamento} encontrado.")
                return None

        except Error as e:
            print(f"Erro ao buscar dados: {e}")
            return None


    def atualizar_agendamento(self, idagendamento, nova_data, nova_hora, novo_status, novo_idcoletor):
        try:
            sql_query = """
            UPDATE 
                agendamento 
            SET 
                dataAgendamento = %s, 
                hora = %s, 
                statusAgendamento = %s, 
                coletor_idcoletor = %s 
            WHERE 
                idagendamento = %s
            """
            self.cursor.execute(sql_query, (nova_data, nova_hora, novo_status, novo_idcoletor, idagendamento))
            self.conexao.commit()
            
            if self.cursor.rowcount > 0:
                print(f"\n[+] Agendamento ID {idagendamento} atualizado com sucesso!")
            else:
                print(f"Nenhum agendamento com o ID {idagendamento}.")
        except Error as e:
            print(f"Erro ao editar dados: {e}")

        
    def excluir_agendamento(self, idagendamento):
        try:           
            sql_query = "DELETE FROM agendamento WHERE idagendamento = %s"
            self.cursor.execute(sql_query, (idagendamento,))
            self.conexao.commit()
            if self.cursor.rowcount > 0:
                print(f"\n[+] Agendamento ID {idagendamento} excluído com sucesso!")
            else:
                print(f"Nenhum agendamento com o ID {idagendamento}.")
        except Error as e:
            print(f"Erro ao excluir dados: {e}")
