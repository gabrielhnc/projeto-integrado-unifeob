from utils.interface import time, consultar_e_validar_id
from funcoes.funcoesCRUD.categoriadb import CategoriaDB
from models.categoria import Categoria

class CategoriaInterface:
    def __init__(self, banco):
        self.categoriadb = CategoriaDB(banco.conexao, banco.cursor)

    def cadastrar_categoria(self):
        print("\n==== Cadastrar Categoria ====")
        nome_categoria = input("\nDigite o nome da categoria que deseja cadastrar [0 para cancelar]: ")
        if nome_categoria == '0':
            print("[!] Cadastro de categoria cancelado.")
            return

        categoria = Categoria(nome_categoria)
        self.categoriadb.cadastrar_categoria(categoria)


    def consultar_categorias(self):
        print("\nConsultando categorias...")
        time.sleep(1)
        self.categoriadb.consultar_categorias()


    def atualizar_categoria(self):
        print("\n==== Atualizar Categoria ====")
        idcategoria = consultar_e_validar_id(self.categoriadb.consultar_categorias, self.categoriadb.consultar_categoria_por_id, "categoria")
        if not idcategoria:
            return
    
        print(f"\n[!] ATUALIZANDO INFORMAÇOES -> Categoria ID {idcategoria}")
        nova_categoria = input("\nDigite o novo nome da categoria: ")

        self.categoriadb.atualizar_categoria(idcategoria, nova_categoria)


    def excluir_categoria(self):
        print("\n==== Excluir Categoria ====")
        idcategoria = consultar_e_validar_id(self.categoriadb.consultar_categorias, self.categoriadb.consultar_categoria_por_id, "categoria")
        if idcategoria is None:
            return

        confirmar = input(f"\nDeseja realmente excluir a categoria com ID {idcategoria}? (s/n): ").lower()
        if confirmar == 's':
            self.categoriadb.excluir_categoria(idcategoria)
        elif confirmar == 'n':
            print("[!] Exclusão cancelada.")
        else:
            print("[!] Resposta inválida.")
