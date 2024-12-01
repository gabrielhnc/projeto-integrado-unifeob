from utils.interface import time, consultar_e_validar_id
from funcoes.funcoesCRUD.tipousuariodb import TipoUsuarioDB
from models.tipo_usuario import TipoUsuario

class TipoUsuarioInterface:
    def __init__(self, banco):
        self.tipo_usuariodb = TipoUsuarioDB(banco.conexao, banco.cursor)

    def cadastrar_tipo_usuario(self):
        print("\n==== Cadastrar Tipo de Usuário ====")

        tipo = input("\nDigite o tipo de usuário [0 para cancelar]: ")
        if tipo == '0':
            print("[!] Cadastro de tipo de usuário cancelado.")
            return

        tipo_usuario = TipoUsuario(tipo)
        self.tipo_usuariodb.cadastrar_tipo_usuario(tipo_usuario)


    def consultar_tipos_usuario(self):
        print("\nConsultando tipos de usuário...")
        time.sleep(1)
        self.tipo_usuariodb.consultar_tipos_usuario()


    def atualizar_tipo_usuario(self):
        print("\n==== Atualizar Tipo de Usuário ====")
        idtipo = consultar_e_validar_id(self.tipo_usuariodb.consultar_tipos_usuario, self.tipo_usuariodb.
        consultar_tipo_usuario_por_id, "tipo de usuário")
        if not idtipo:
            return

        print(f"\n[!] ATUALIZANDO INFORMAÇÕES -> Tipo de usuário ID {idtipo}")
        novo_tipo = input("\nDigite o novo nome do tipo de usuário: ")
        
        self.tipo_usuariodb.atualizar_tipo_usuario(idtipo, novo_tipo)


    def excluir_tipo_usuario(self):
        print("\n==== Excluir Tipo de Usuário ====")
        idtipo = consultar_e_validar_id(self.tipo_usuariodb.consultar_tipos_usuario, self.tipo_usuariodb.consultar_tipo_usuario_por_id, "tipo de usuário")
        if idtipo is None:
            return

        confirmar = input(f"\nDeseja realmente excluir o tipo de usuário com ID {idtipo}? (s/n): ").lower()
        if confirmar == 's':
            self.tipo_usuariodb.excluir_tipo_usuario(idtipo)
        elif confirmar == 'n':
            print("[!] Exclusão cancelada.")
        else:
            print("[!] Resposta inválida.")
