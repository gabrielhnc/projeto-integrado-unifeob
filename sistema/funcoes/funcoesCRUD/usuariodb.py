from utils.crud import *

class UsuarioDB:
    def __init__(self, conexao, cursor):
        self.conexao = conexao
        self.cursor = cursor

    def cadastrar_usuario(self, usuario):
        try:
            sql_query = "INSERT INTO usuario (nome, email, telefone, dataCadastro, tipoUsuario_idtipoUsuario) VALUES (%s, %s, %s, %s, %s)"
            valores = (
                usuario.get_nome(), 
                usuario.get_email(), 
                usuario.get_telefone(), 
                usuario.get_dataCadastro(),
                usuario.get_idtipoUsuario()
            )
            self.cursor.execute(sql_query, valores)
            self.conexao.commit()
            print(f"\n[+] Usuário '{usuario.get_nome()}' cadastrado com sucesso!")
        except Error as e:
            self.conexao.rollback()
            print(f"Erro ao cadastrar dados: {e}")

        
    def consultar_usuarios(self):
        try:
            sql_query = """
            SELECT 
                u.idusuario, 
                u.nome, 
                u.email, 
                u.telefone, 
                u.dataCadastro,
                t.tipo 
            FROM 
                usuario u
            INNER JOIN tipoUsuario t ON u.tipoUsuario_idtipoUsuario = t.idtipoUsuario
            ORDER BY idusuario ASC
            """
            self.cursor.execute(sql_query)
            usuarios = self.cursor.fetchall()
            if usuarios:
                print("\n=== Usuários Cadastrados ===")
                headers = ["ID", "Nome", "Email", "Telefone", "Data Cadastro", "Tipo de Usuário"]
                print(tabulate(usuarios, headers=headers, tablefmt="fancy_grid"))
            else:
                print("\n[!] Nenhum usuário cadastrado.")
        except Error as e:
            print(f"Erro ao buscar dados: {e}")


    def consultar_usuario_por_id(self, idusuario):
        try:
            sql_query = """
            SELECT 
                u.idusuario, 
                u.nome, 
                u.email, 
                u.telefone, 
                u.dataCadastro,
                t.tipo 
            FROM 
                usuario u
            INNER JOIN tipoUsuario t ON u.tipoUsuario_idtipoUsuario = t.idtipoUsuario
            WHERE u.idusuario = %s
            """
            self.cursor.execute(sql_query, (idusuario,))
            usuario = self.cursor.fetchone()
            if usuario:
                print("\n=== Usuário Escolhido ===")
                headers = ["ID", "Nome", "Email", "Telefone", "Data Cadastro", "Tipo de Usuário"]
                print(tabulate([usuario], headers=headers, tablefmt="fancy_grid"))
                return usuario
            else:
                print(f"[!] Nenhum usuário encontrado com o ID {idusuario}.")
                return None
        except Error as e:
            print(f"Erro ao buscar dados: {e}")
            return None
        
    
    def atualizar_usuario(self, id_usuario, novo_nome, novo_email, novo_telefone, nova_dataCadastro, tipo_usuario_id):
        try:
            sql_query = "UPDATE usuario SET nome = %s, email = %s, telefone = %s, dataCadastro = %s, tipoUsuario_idtipoUsuario = %s WHERE idusuario = %s"
            self.cursor.execute(sql_query, (novo_nome, novo_email, novo_telefone, nova_dataCadastro, tipo_usuario_id, id_usuario))
            self.conexao.commit()
            if self.cursor.rowcount > 0:
                print(f"\n[+] Usuário ID {id_usuario} atualizado para '{novo_nome}' com sucesso.")
            else:
                print(f"Nenhum usuário com o ID {id_usuario}.")
        except Error as e:
            self.conexao.rollback()
            print(f"Erro ao atualizar dados: {e}")

        
    def excluir_usuario(self, id_usuario):
        try:
            sql_query = "DELETE FROM usuario WHERE idusuario = %s"
            self.cursor.execute(sql_query, (id_usuario,))
            self.conexao.commit()
            if self.cursor.rowcount > 0:
                print(f"\n[+] Usuário ID {id_usuario} excluído com sucesso!")
            else:
                print(f"Nenhum usuário com o ID {id_usuario}.")
        except Error as e:
            self.conexao.rollback()
            print(f"Erro ao excluir dados: {e}")
