from utils.crud import *

class TipoUsuarioDB:
    def __init__(self, conexao, cursor):
        self.conexao = conexao
        self.cursor = cursor

    def cadastrar_tipo_usuario(self, tipo):
        try:
            sql_query = "INSERT INTO tipousuario (tipo) VALUES (%s)"
            self.cursor.execute(sql_query, (tipo.get_tipo(),))
            self.conexao.commit()
            print(f"\n[+] Tipo de usuário '{tipo.get_tipo()}' cadastrado com sucesso!")
        except Error as e:
            self.conexao.rollback()
            print(f"Erro ao cadastrar dados: {e}")


    def consultar_tipos_usuario(self):
        try:
            
            sql_query = "SELECT * FROM tipoUsuario"
            self.cursor.execute(sql_query)
            tipos = self.cursor.fetchall()
            if tipos:
                print("\n=== Tipos de Usuários Cadastrados ===")
                headers = ["ID", "Tipo"]
                print(tabulate(tipos, headers=headers, tablefmt="fancy_grid"))
            else:
                print("\n[!] Nenhum tipo de usuário cadastrado.")
        except Error as e:
            print(f"Erro ao buscar dados: {e}")


    def consultar_tipo_usuario_por_id(self, idtipoUsuario):
        try:
            sql_query = "SELECT * FROM tipoUsuario WHERE idtipoUsuario = %s"
            self.cursor.execute(sql_query, (idtipoUsuario,))
            tipo_usuario = self.cursor.fetchone()
            if tipo_usuario:
                print("\n=== Tipo de Usuário Escolhido ===")
                headers = ["ID", "Tipo"]
                print(tabulate([tipo_usuario], headers=headers, tablefmt="fancy_grid"))
                return tipo_usuario
            else:
                print(f"[!] Nenhum tipo de usuário encontrado com o ID {idtipoUsuario}.")
                return None
        except Error as e:
            print(f"Erro ao buscar dados: {e}")
            return None
        

    def atualizar_tipo_usuario(self, id_tipo, novo_tipo):
        try:           
            sql_query = "UPDATE tipousuario SET tipo = %s WHERE idtipoUsuario = %s"
            self.cursor.execute(sql_query, (novo_tipo, id_tipo))
            self.conexao.commit()
            if self.cursor.rowcount > 0:
                print(f"[+] Tipo ID {id_tipo} atualizado para '{novo_tipo}' com sucesso.")
            else:
                print(f"\nNenhum tipo com o ID {id_tipo}.")
        except Error as e:
            self.conexao.rollback()
            print(f"Erro ao atualizar dados: {e}")

        
    def excluir_tipo_usuario(self, id_tipo):
        try:
            sql_query = "DELETE FROM tipoUsuario WHERE idtipoUsuario = %s"
            self.cursor.execute(sql_query, (id_tipo,))
            self.conexao.commit()
            if self.cursor.rowcount > 0:
                print(f"\n[+] Tipo ID {id_tipo} excluído com sucesso!")
            else:
                print(f"Nenhum tipo com o ID {id_tipo}.")
        except Error as e:
            self.conexao.rollback()
            print(f"Erro ao excluir dados: {e}")