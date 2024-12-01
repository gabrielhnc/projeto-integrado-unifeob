from utils.crud import *

class CidadeDB:
    def __init__(self, conexao, cursor):
        self.conexao = conexao
        self.cursor = cursor

    def cadastrar_cidade(self, cidade):
        try:
            sql_query = "INSERT INTO cidade (nome, estado_idestado) VALUES (%s, %s)"
            valores = (cidade.get_nome(), cidade.get_idestado())
            self.cursor.execute(sql_query, valores)
            self.conexao.commit()
            print(f"\n[+] Cidade '{cidade.get_nome()}' cadastrada com sucesso!")
        except Error as e:
            self.conexao.rollback()
            print(f"Erro ao cadastrar dados: {e}")


    def consultar_cidades(self):
        try:
            sql_query = "SELECT idcidade, nome, estado_idestado FROM cidade"
            self.cursor.execute(sql_query)
            cidades = self.cursor.fetchall()
            if cidades:
                print("\n=== Cidades Cadastradas ===")
                headers = ["ID Cidade", "Nome", "Sigla Estado"]
                print(tabulate(cidades, headers=headers, tablefmt="fancy_grid"))
            else:
                print("\n[!] Nenhuma cidade cadastrada.")
        except Error as e:
            print(f"Erro ao buscar dados: {e}")


    def consultar_cidade_por_id(self, idcidade):
        try:
            sql_query = "SELECT idcidade, nome, estado_idestado FROM cidade WHERE idcidade = %s"
            self.cursor.execute(sql_query, (idcidade,))
            cidade = self.cursor.fetchone()
            if cidade:
                print("\n=== Cidade Escolhida ===")
                headers = ["ID Cidade", "Nome", "Sigla Estado"]
                print(tabulate([cidade], headers=headers, tablefmt="fancy_grid"))
                return cidade
            else:
                print(f"[!] Nenhuma cidade encontrada com o ID {idcidade}.")
                return None
        except Error as e:
            print(f"Erro ao buscar dados: {e}")
            return None
        

    def atualizar_cidade(self, idcidade, estado_idestado, novo_nome):
        try:
            sql_query = "UPDATE cidade SET nome = %s WHERE idcidade = %s AND estado_idestado = %s"
            self.cursor.execute(sql_query, (novo_nome, idcidade, estado_idestado))
            self.conexao.commit()
            if self.cursor.rowcount > 0:
                print(f"\n[+] Cidade ID {idcidade} atualizada para '{novo_nome}' com sucesso.")
            else:
                print(f"Nenhuma cidade com o ID {idcidade}.")
        except Error as e:
            self.conexao.rollback()
            print(f"Erro ao atualizar dados: {e}")
        

    def excluir_cidade(self, idcidade):
        try:
            sql_query = "DELETE FROM cidade WHERE idcidade = %s"
            self.cursor.execute(sql_query, (idcidade,))
            self.conexao.commit()
            if self.cursor.rowcount > 0:
                print(f"\n[+] Cidade ID {idcidade} excluída com sucesso!")
            else:
                print(f"Nenhuma cidade com o ID {idcidade}.")
        except Error as e:
            self.conexao.rollback()
            print(f"Erro ao excluir dados: {e}")
