from utils.crud import *

class EntradaDB:
    def __init__(self, conexao, cursor):
        self.conexao = conexao
        self.cursor = cursor

    def cadastrar_entrada(self, entrada):
        try:
            sql_query = """
            INSERT INTO entrada (usuario_idusuario, deposito_iddeposito, material_idmaterial, dataEntrada, quantidade) 
            VALUES (%s, %s, %s, %s, %s)
            """
            valores = (
                entrada.get_idusuario(),
                entrada.get_iddeposito(),
                entrada.get_idmaterial(),
                entrada.get_dataEntrada(),
                entrada.get_quantidade()
            )
            self.cursor.execute(sql_query, valores)
            self.conexao.commit()
            print(f"\n[+] Entrada cadastrada com sucesso!")
        except Error as e:
            self.conexao.rollback()
            print(f"Erro ao cadastrar dados: {e}")

    def consultar_entradas(self):
        try:
            sql_query = """
            SELECT 
                e.identrada, 
                u.nome,
                d.nome,
                m.nome,
                e.dataEntrada, 
                CONCAT(FORMAT(e.quantidade, 1), ' g') AS quantidade
            FROM 
                entrada e
            INNER JOIN usuario u ON e.usuario_idusuario = u.idusuario
            INNER JOIN deposito d ON e.deposito_iddeposito = d.iddeposito
            INNER JOIN material m ON e.material_idmaterial = m.idmaterial
            ORDER BY identrada ASC
            """
            self.cursor.execute(sql_query)
            entradas = self.cursor.fetchall()
            if entradas:
                print("\n=== Entradas Cadastradas ===")
                headers = ["ID Entrada", "Nome do Usuário", "Nome do Depósito", "Nome do Material", "Data Entrada", "Quantidade(g)"]
                print(tabulate(entradas, headers=headers, tablefmt="fancy_grid"))
            else:
                print("\n[!] Nenhuma entrada cadastrada.")
        except Error as e:
            print(f"Erro ao buscar dados: {e}")


    def consultar_entrada_por_id(self, identrada):
        try:
            sql_query = """
            SELECT 
                e.identrada, 
                u.nome AS nome_usuario,
                d.nome AS nome_deposito, 
                m.nome AS nome_material,
                e.dataEntrada, 
                CONCAT(FORMAT(e.quantidade, 1), ' g') AS quantidade
            FROM 
                entrada e
            INNER JOIN usuario u ON e.usuario_idusuario = u.idusuario
            INNER JOIN deposito d ON e.deposito_iddeposito = d.iddeposito
            INNER JOIN material m ON e.material_idmaterial = m.idmaterial
            WHERE e.identrada = %s
            """
            self.cursor.execute(sql_query, (identrada,))
            entrada = self.cursor.fetchone()
            if entrada:
                print("\n=== Entrada Escolhida ===")
                headers = ["ID Entrada", "Nome do Usuário", "Nome do Depósito", "Nome do Material", "Data Entrada", "Quantidade(g)"]
                print(tabulate([entrada], headers=headers, tablefmt="fancy_grid"))
                return entrada
            else:
                print(f"[!] Nenhuma entrada encontrada com o ID {identrada}.")
                return None
        except Error as e:
            print(f"Erro ao buscar dados: {e}")
            return None

    def atualizar_entrada(self, identrada, usuario_idusuario, deposito_iddeposito, material_idmaterial, dataEntrada, quantidade):
        try:
            sql_query = """
            UPDATE 
                entrada 
            SET 
                usuario_idusuario = %s, 
                deposito_iddeposito = %s, 
                material_idmaterial = %s, 
                dataEntrada = %s, 
                quantidade = %s 
            WHERE 
                identrada = %s
            """
            self.cursor.execute(sql_query, (usuario_idusuario, deposito_iddeposito, material_idmaterial, dataEntrada, quantidade, identrada))
            self.conexao.commit()
            if self.cursor.rowcount > 0:
                print(f"\n[+] Entrada ID {identrada} atualizada com sucesso.")
            else:
                print(f"Nenhuma entrada com o ID {identrada}.")
        except Error as e:
            self.conexao.rollback()
            print(f"Erro ao atualizar dados: {e}")

    
    def excluir_entrada(self, identrada):
        try:
            sql_query = "DELETE FROM entrada WHERE identrada = %s"
            self.cursor.execute(sql_query, (identrada,))
            self.conexao.commit()
            if self.cursor.rowcount > 0:
                print(f"\n[+] Entrada ID {identrada} excluída com sucesso!")
            else:
                print(f"Nenhuma entrada com o ID {identrada}.")
        except Error as e:
            self.conexao.rollback()
            print(f"Erro ao excluir dados: {e}")