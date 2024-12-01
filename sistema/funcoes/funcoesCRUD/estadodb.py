from utils.crud import *

class EstadoDB:
    def __init__(self, conexao, cursor):
        self.conexao = conexao
        self.cursor = cursor

    def cadastrar_estado(self, estado):
        try:
            sql_query = "INSERT INTO estado (idestado, nome) VALUES (%s, %s)"
            valores = (estado.get_idestado(), estado.get_nome())
            self.cursor.execute(sql_query, valores)
            self.conexao.commit
            print(f"\n[+] Estado '{estado.get_nome()}' cadastrado com sucesso!")
        except Error as e:
            self.conexao.rollback()
            print(f"Erro ao cadastrar dados: {e}")


    def consultar_estados(self):
        try:
            sql_query = "SELECT idestado, nome FROM estado"
            self.cursor.execute(sql_query)
            estados = self.cursor.fetchall()
            if estados:
                print("\n=== Estados Cadastrados ===")
                headers = ["ID(Sigla)", "Nome"]
                print(tabulate(estados, headers=headers, tablefmt="fancy_grid"))
            else:
                print("\n[!] Nenhum estado cadastrado.")
        except Error as e:
            print(f"Erro ao buscar dados: {e}")


    def consultar_estado_por_id(self, idestado):
        try:
            sql_query = "SELECT idestado, nome FROM estado WHERE idestado = %s"
            self.cursor.execute(sql_query, (idestado,))
            estado = self.cursor.fetchone()
            if estado:
                print("\n=== Estado Escolhido ===")
                headers = ["ID(Sigla)", "Nome"]
                print(tabulate([estado], headers=headers, tablefmt="fancy_grid"))
                return estado
            else:
                print(f"[!] Nenhum estado encontrado com o ID {idestado}.")
                return None
        except Error as e:
            print(f"Erro ao buscar dados: {e}")
            return None

    def atualizar_estado(self, id_estado, novo_nome):
        try:    
            sql_query = "UPDATE estado SET nome = %s WHERE idestado = %s"
            self.cursor.execute(sql_query, (novo_nome, id_estado))
            self.conexao.commit()
            if self.cursor.rowcount > 0:
                print(f"\n[+] Estado ID {id_estado} atualizado para '{novo_nome}' com sucesso.")
            else:
                print(f"Nenhum estado com o ID {id_estado}.")
        except Error as e:
            self.conexao.rollback()
            print(f"Erro ao atualizar dados: {e}")


    def excluir_estado(self, id_estado):
        try:
            sql_query = "DELETE FROM estado WHERE idestado = %s"
            self.cursor.execute(sql_query, (id_estado,))
            self.conexao.commit()
            if self.cursor.rowcount > 0:
                print(f"\n[+] Estado ID {id_estado} excluído com sucesso!")
            else:
                print(f"Nenhum estado com o ID {id_estado}.")
        except Error as e:
            self.conexao.rollback()
            print(f"Erro ao excluir dados: {e}")