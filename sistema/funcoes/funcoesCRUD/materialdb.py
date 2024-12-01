from utils.crud import *

class MaterialDB:
    def __init__(self, conexao, cursor):
        self.conexao = conexao
        self.cursor = cursor

    def cadastrar_material(self, material):
        try:
            sql_query = "INSERT INTO material (nome, descricao, categoria_idcategoria) VALUES (%s, %s, %s)"
            valores = (
                material.get_nome(), 
                material.get_descricao(), 
                material.get_idcategoria()
            )
            self.cursor.execute(sql_query, valores)
            self.conexao.commit()
            print(f"\n[+] Material '{material.get_nome()}' cadastrado com sucesso!")
        except Error as e:
            self.conexao.rollback()
            print(f"Erro ao cadastrar dados: {e}")


    def consultar_materiais(self):
        try:
            sql_query = """
            SELECT 
                m.idmaterial, 
                m.nome, 
                m.descricao, 
                c.categoria
            FROM 
                material m
            INNER JOIN categoria c ON m.categoria_idcategoria = c.idcategoria
            ORDER BY idmaterial ASC
            """
            self.cursor.execute(sql_query)
            materiais = self.cursor.fetchall()
            if materiais:
                print("\n=== Materiais Cadastrados ===")
                headers = ["ID", "Nome", "Descrição", "Categoria"]
                print(tabulate(materiais, headers=headers, tablefmt="fancy_grid"))
            else:
                print("\n[!] Nenhum material cadastrado.")
        except Error as e:
            print(f"Erro ao buscar dados: {e}")


    def consultar_material_por_id(self, idmaterial):
        try:
            sql_query = """
            SELECT 
                m.idmaterial, 
                m.nome, 
                m.descricao, 
                c.categoria
            FROM 
                material m
            INNER JOIN categoria c ON m.categoria_idcategoria = c.idcategoria
            WHERE m.idmaterial = %s
            """
            self.cursor.execute(sql_query, (idmaterial,))
            material = self.cursor.fetchone()
            if material:
                print("\n=== Material Escolhido ===")
                headers = ["ID", "Nome", "Descrição", "Categoria"]
                print(tabulate([material], headers=headers, tablefmt="fancy_grid"))
                return material
            else:
                print(f"[!] Nenhum material encontrado com o ID {idmaterial}.")
                return None
        except Error as e:
            print(f"Erro ao buscar dados: {e}")
            return None
        
    
    def atualizar_material(self, id_material, novo_nome, nova_descricao, categoria_id):
        try:
            sql_query = "UPDATE material SET nome = %s, descricao = %s, categoria_idcategoria = %s WHERE idmaterial = %s"
            self.cursor.execute(sql_query, (novo_nome, nova_descricao, categoria_id, id_material))
            self.conexao.commit()
            if self.cursor.rowcount > 0:
                print(f"\n[+] material ID {id_material} atualizado para '{novo_nome}' com sucesso.")
            else:
                print(f"Nenhum material com o ID {id_material}.")
        except Error as e:
            self.conexao.rollback()
            print(f"Erro ao atualizar dados: {e}")

        
    def excluir_material(self, id_material):
        try:
            sql_query = "DELETE FROM material WHERE idmaterial = %s"
            self.cursor.execute(sql_query, (id_material,))
            self.conexao.commit()
            if self.cursor.rowcount > 0:
                print(f"\n[+] Material ID {id_material} excluído com sucesso!")
            else:
                print(f"Nenhum material com o ID {id_material}.")
        except Error as e:
            self.conexao.rollback()
            print(f"Erro ao excluir dados: {e}")
