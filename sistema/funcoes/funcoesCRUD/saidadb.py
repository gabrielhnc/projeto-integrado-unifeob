from utils.crud import *

class SaidaDB:
    def __init__(self, conexao, cursor):
        self.conexao = conexao
        self.cursor = cursor

    def cadastrar_saida(self, saida):
        try:
            sql_query = """
            INSERT INTO saida (deposito_iddeposito, coletor_idcoletor, material_idmaterial, dataSaida, quantidade) 
            VALUES (%s, %s, %s, %s, %s)
            """
            valores = (
                saida.get_iddeposito(), 
                saida.get_idcoletor(), 
                saida.get_idmaterial(), 
                saida.get_dataSaida(), 
                saida.get_quantidade()
            )
            self.cursor.execute(sql_query, valores)
            self.conexao.commit()
            print("\n[+] Saída cadastrada com sucesso!")
        except Error as e:
            self.conexao.rollback()
            print(f"Erro ao cadastrar dados: {e}")


    def consultar_saidas(self):
        try:
            sql_query = """
            SELECT 
                s.idsaida, 
                d.nome AS nome_deposito, 
                c.nome AS nome_coletor, 
                m.nome AS nome_material, 
                s.dataSaida, 
                CONCAT(FORMAT(s.quantidade, 1), ' g') AS quantidade
            FROM 
                saida s
            INNER JOIN deposito d ON s.deposito_iddeposito = d.iddeposito
            INNER JOIN coletor c ON s.coletor_idcoletor = c.idcoletor
            INNER JOIN material m ON s.material_idmaterial = m.idmaterial
            ORDER BY idsaida ASC
            """
            self.cursor.execute(sql_query)
            saidas = self.cursor.fetchall()
            if saidas:
                print("\n=== Saídas Cadastradas ===")
                headers = ["ID Saída", "Nome do Depósito", "Nome do Coletor", "Nome do Material", "Data Saída", "Quantidade(g)"]
                print(tabulate(saidas, headers=headers, tablefmt="fancy_grid"))
            else:
                print("\n[!] Nenhuma saída cadastrada.")
        except Error as e:
            print(f"Erro ao buscar dados: {e}")


    def consultar_saida_por_id(self, idsaida):
        try:
            sql_query = """
            SELECT 
                s.idsaida, 
                d.nome AS nome_deposito, 
                c.nome AS nome_coletor, 
                m.nome AS nome_material, 
                s.dataSaida, 
                CONCAT(FORMAT(s.quantidade, 1), ' g') AS quantidade
            FROM 
                saida s
            INNER JOIN deposito d ON s.deposito_iddeposito = d.iddeposito
            INNER JOIN coletor c ON s.coletor_idcoletor = c.idcoletor
            INNER JOIN material m ON s.material_idmaterial = m.idmaterial
            WHERE s.idsaida = %s
            """
            self.cursor.execute(sql_query, (idsaida,))
            saida = self.cursor.fetchone()
            if saida:
                print("\n=== Saída Escolhida ===")
                headers = ["ID Saída", "Nome do Depósito", "Nome do Coletor", "Nome do Material", "Data Saída", "Quantidade(g)"]
                print(tabulate([saida], headers=headers, tablefmt="fancy_grid"))
                return saida
            else:
                print(f"[!] Nenhuma saída encontrada com o ID {idsaida}.")
                return None
        except Error as e:
            print(f"Erro ao buscar dados: {e}")
            return None
        

    def atualizar_saida(self, idsaida, deposito_iddeposito, coletor_idcoletor, material_idmaterial, dataSaida, quantidade):
        try:           
            sql_query = """
            UPDATE 
                saida 
            SET 
                deposito_iddeposito = %s, 
                coletor_idcoletor = %s, 
                material_idmaterial = %s, 
                dataSaida = %s, 
                quantidade = %s 
            WHERE 
                idsaida = %s
            """
            self.cursor.execute(sql_query, (deposito_iddeposito, coletor_idcoletor, material_idmaterial, dataSaida, quantidade, idsaida))
            self.conexao.commit()
            if self.cursor.rowcount > 0:
                print(f"\n[+] Saída ID {idsaida} atualizada com sucesso.")
            else:
                print(f"Nenhuma saída com o ID {idsaida}.")
        except Error as e:
            self.conexao.rollback()
            print(f"Erro ao atualizar dados: {e}")

    
    def excluir_saida(self, idsaida):
        try:
            sql_query = "DELETE FROM saida WHERE idsaida = %s"
            self.cursor.execute(sql_query, (idsaida,))
            self.conexao.commit()
            if self.cursor.rowcount > 0:
                print(f"\n[+] Saida ID {idsaida} excluída com sucesso!")
            else:
                print(f"Nenhuma saída com o ID {idsaida}.")
        except Error as e:
            self.conexao.rollback()
            print(f"Erro ao excluir dados: {e}")