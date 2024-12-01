from utils.interface import consultar_e_validar_id, time
from funcoes.funcoesCRUD.materialdb import MaterialDB
from funcoes.funcoesCRUD.categoriadb import CategoriaDB
from models.material import Material

class MaterialInterface:
    def __init__(self, banco):
        self.materialdb = MaterialDB(banco.conexao, banco.cursor)
        self.categoriadb = CategoriaDB(banco.conexao, banco.cursor)

    def cadastrar_material(self):
        print("\n==== Cadastrar Material ====")

        nome = input("\nDigite o nome do material [0 para cancelar]: ")
        if nome == '0':
            print("[!] Cadastro de material cancelado.")
            return

        descricao = input("Digite a descrição do material: ")

        idcategoria = consultar_e_validar_id(self.categoriadb.consultar_categorias, self.categoriadb.consultar_categoria_por_id, "categoria")
        if idcategoria is None:
            return

        material = Material(nome, descricao, idcategoria)
        self.materialdb.cadastrar_material(material)


    def consultar_materiais(self):
        print("\nConsultando materiais...")
        time.sleep(1)
        self.materialdb.consultar_materiais()


    def atualizar_material(self):
        print("\n==== Atualizar Material ====")
        idmaterial = consultar_e_validar_id(self.materialdb.consultar_materiais, self.materialdb.consultar_material_por_id, "material")
        if not idmaterial:
            return

        print(f"\n[!] ATUALIZANDO INFORMAÇOES -> Material ID {idmaterial}")
        novo_nome = input("\nDigite o novo nome da categoria: ")
        nova_descricao = input("Digite a nova descrição do material: ")

        idcategoria = consultar_e_validar_id(self.categoriadb.consultar_categorias, self.categoriadb.consultar_categoria_por_id, "categoria")
        if idcategoria is None:
            return

        self.materialdb.atualizar_material(idmaterial, novo_nome, nova_descricao, idcategoria)


    def excluir_material(self):
        print("\n==== Excluir Material ====")
        idmaterial = consultar_e_validar_id(self.materialdb.consultar_materiais, self.materialdb.consultar_material_por_id, "material")
        if idmaterial is None:
            return

        confirmar = input(f"\nDeseja realmente excluir a material com ID {idmaterial}? (s/n): ").lower()
        if confirmar == 's':
            self.materialdb.excluir_material(idmaterial)
        elif confirmar == 'n':
            print("[!] Exclusão cancelada.")
        else:
            print("[!] Resposta inválida.")
