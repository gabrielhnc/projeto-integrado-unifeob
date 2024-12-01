from utils.crud import *

class CategoriaDB:
    def __init__(self, conexao, cursor):
        self.conexao = conexao
        self.cursor = cursor

    def cadastrar_categoria(self, categoria):
        try:
            sql_query = "INSERT INTO categoria (categoria) VALUES (%s)"
            self.cursor.execute(sql_query, (categoria.get_categoria(),))
            self.conexao.commit()
            print(f"\n[+] Categoria '{categoria.get_categoria()}' cadastrada com sucesso!")
        except Error as e:
            self.conexao.rollback()
            print(f"Erro ao cadastrar dados: {e}")


    def consultar_categorias(self):
        try:
            sql_query = "SELECT * FROM categoria"
            self.cursor.execute(sql_query)
            categorias = self.cursor.fetchall()
            if categorias:
                print("\n=== Categorias Cadastradas ===")
                headers = ["ID", "Categoria"]
                print(tabulate(categorias, headers=headers, tablefmt="fancy_grid")) 
            else:
                print("\n[!] Nenhuma categoria cadastrada.")
        except Error as e:
            print(f"Erro ao buscar dados: {e}")


    def consultar_categoria_por_id(self, idcategoria):
        try:
            sql_query = "SELECT * FROM categoria WHERE idcategoria = %s"
            self.cursor.execute(sql_query, (idcategoria,))
            categoria = self.cursor.fetchone()
            if categoria:
                print("\n=== Categoria Escolhida ===")
                headers = ["ID", "Categoria"]
                print(tabulate([categoria], headers=headers, tablefmt="fancy_grid"))
                return categoria
            else:
                print(f"[!] Nenhuma categoria encontrada com o ID {idcategoria}.")
                return None
        except Error as e:
            print(f"Erro ao buscar dados: {e}")
            return None
        

    def atualizar_categoria(self, idcategoria, novacategoria):
        try:
            sql_query = "UPDATE categoria SET categoria = %s WHERE idcategoria = %s"
            self.cursor.execute(sql_query, (novacategoria,idcategoria))
            self.conexao.commit()

            if self.cursor.rowcount > 0:
                print(f"\n[+] Categoria ID {idcategoria} atualizada para '{novacategoria}' com sucesso.")
            else:
                print(f"Nenhuma categoria com o ID {idcategoria}.")
        except Error as e:
            self.conexao.rollback()
            print(f"Erro ao atualizar dados: {e}")

        
    def excluir_categoria(self, idcategoria):
        try:            
            sql_query = "DELETE FROM categoria WHERE idcategoria = %s"
            self.cursor.execute(sql_query, (idcategoria,))
            self.conexao.commit()
            
            if self.cursor.rowcount > 0:
                print(f"\n[+] Categoria ID {idcategoria} excluída com sucesso!")
            else:
                print(f"Nenhuma categoria com o ID {idcategoria}.")
        except Error as e:
            self.conexao.rollback()
            print(f"Erro ao excluir dados: {e}")
