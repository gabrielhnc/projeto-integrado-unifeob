from utils.interface import *
from funcoes.funcoesCRUD.usuariodb import UsuarioDB
from funcoes.funcoesCRUD.tipousuariodb import TipoUsuarioDB
from models.usuario import Usuario

class UsuarioInterface:
    def __init__(self, banco):
        self.usuariodb = UsuarioDB(banco.conexao, banco.cursor)
        self.tipo_usuariodb = TipoUsuarioDB(banco.conexao, banco.cursor)

    def cadastrar_usuario(self):
        print("\n==== Cadastro de Usuario ====")
        nome = input("\nDigite o nome do usuário [0 para cancelar]: ")
        if nome == '0':
            print("[!] Cadastro de usuário cancelado.")
            return

        email = input("Digite o email do usuário: ")
        telefone = input("Digite o telefone do usuário: ")
        
        dataCadastro = obter_data(f"Digite a data de cadastro do usuário '{nome}' (DD/MM/YYYY) [0 para cancelar]: ")
        if dataCadastro is None:
            return

        id_tipousuario = consultar_e_validar_id(self.tipo_usuariodb.consultar_tipos_usuario, self.tipo_usuariodb.consultar_tipo_usuario_por_id, "tipo de usuário")
        if id_tipousuario is None:
            return

        usuario = Usuario(nome, email, telefone, conversao_data(dataCadastro), id_tipousuario)
        self.usuariodb.cadastrar_usuario(usuario)


    def consultar_usuarios(self):
        print("\nConsultando usuários...")
        time.sleep(1)
        self.usuariodb.consultar_usuarios()


    def atualizar_usuario(self):
        print("\n==== Atualizar Usuário ====")
        id_usuario = consultar_e_validar_id(self.usuariodb.consultar_usuarios, self.usuariodb.consultar_usuario_por_id, "usuário")
        if id_usuario is None:
            return

        print(f"\n[!] ATUALIZANDO INFORMAÇÕES -> Usuário ID {id_usuario}")
        novo_nome = input("\nDigite o novo nome do usuário: ")
        novo_email = input("Digite o novo email do usuário: ")
        novo_telefone = input("Digite o novo telefone do usuário: ")

        nova_dataCadastro = obter_data(f"Digite a nova data de cadastro do usuário '{novo_nome}' (DD/MM/YYYY) [0 para cancelar]: ")
        if nova_dataCadastro is None:
            return

        novo_idtipousuario = consultar_e_validar_id(self.tipo_usuariodb.consultar_tipos_usuario, self.tipo_usuariodb.consultar_tipo_usuario_por_id, "tipo de usuário")
        if novo_idtipousuario is None:
            return

        self.usuariodb.atualizar_usuario(id_usuario, novo_nome, novo_email, novo_telefone, conversao_data(nova_dataCadastro), novo_idtipousuario)


    def excluir_usuario(self):
        print("\n==== Excluir Usuário ====")
        id_usuario = consultar_e_validar_id(self.usuariodb.consultar_usuarios, self.usuariodb.consultar_usuario_por_id, "usuário")
        if id_usuario is None:
            return

        confirmar = input(f"\nDeseja realmente excluir o usuário com ID {id_usuario}? (s/n): ").lower()
        if confirmar == 's':
            self.usuariodb.excluir_usuario(id_usuario)
        elif confirmar == 'n':
            print("[!] Exclusão cancelada.")
        else:
            print("[!] Resposta inválida.")
