from utils.crud import *

class ColetorDB:
    def __init__(self, conexao, cursor):
        self.conexao = conexao
        self.cursor = cursor

    def cadastrar_coletor(self, coletor):
        try:
            sql_query = "INSERT INTO coletor (nome, cnpjCpf, telefone, endereco, cidade_idcidade, dataCadastro) VALUES (%s, %s, %s, %s, %s, %s)"
            valores = (
                coletor.get_nome(),
                coletor.get_cnpjCpf(),
                coletor.get_telefone(),
                coletor.get_endereco(),
                coletor.get_idcidade(),
                coletor.get_dataCadastro()
            )
            self.cursor.execute(sql_query, valores)
            self.conexao.commit()
            print(f"\n[+] Coletor '{coletor.get_nome()}' cadastrado com sucesso!")
        except Error as e:
            self.conexao.rollback()
            print(f"Erro ao cadastrar dados: {e}")

        
    def consultar_coletores(self):
        try:
            
            sql_query = """
            SELECT 
                coletor.idcoletor, 
                coletor.nome, 
                coletor.cnpjCpf, 
                coletor.telefone, 
                coletor.endereco, 
                cidade.nome AS nome_cidade,  -- Seleciona o nome da cidade
                coletor.dataCadastro 
            FROM 
                coletor 
            INNER JOIN 
                cidade ON coletor.cidade_idcidade = cidade.idcidade  -- Realiza o JOIN
            ORDER BY idcoletor ASC
            """
            self.cursor.execute(sql_query)
            coletores = self.cursor.fetchall()
            if coletores:
                print("\n=== Coletores Cadastrados ===")
                headers = ["ID Coletor", "Nome", "CNPJ/CPF", "Telefone", "Endereço", "Cidade", "Data Cadastro"]
                print(tabulate(coletores, headers=headers, tablefmt="fancy_grid"))
            else:
                print("\n[!] Nenhum coletor cadastrado.")
        except Error as e:
            print(f"Erro ao buscar dados: {e}")

        
    def consultar_coletor_por_id(self, idcoletor):
        try:
            sql_query = """
            SELECT 
                coletor.idcoletor, 
                coletor.nome, 
                coletor.cnpjCpf, 
                coletor.telefone, 
                coletor.endereco, 
                cidade.nome AS nome_cidade, 
                coletor.dataCadastro 
            FROM 
                coletor 
            INNER JOIN 
                cidade ON coletor.cidade_idcidade = cidade.idcidade 
            WHERE coletor.idcoletor = %s
            """
            self.cursor.execute(sql_query, (idcoletor,))
            coletor = self.cursor.fetchone()
            if coletor:
                print("\n=== Coletor Escolhido ===")
                headers = ["ID Coletor", "Nome", "CNPJ/CPF", "Telefone", "Endereço", "Nome Cidade", "Data Cadastro"]
                print(tabulate([coletor], headers=headers, tablefmt="fancy_grid"))
                return coletor
            else:
                print(f"[!] Nenhum coletor encontrado com o ID {idcoletor}.")
                return None
        except Error as e:
            print(f"Erro ao buscar dados: {e}")
            return None
        

    def atualizar_coletor(self, idcoletor, novo_nome, novo_cnpjCpf, novo_telefone, novo_endereco, nova_dataCadastro, novo_idcidade):
        try:
            sql_query = """
            UPDATE 
                coletor 
            SET 
                nome = %s, 
                cnpjCpf = %s, 
                telefone = %s, 
                endereco = %s, 
                dataCadastro = %s 
            WHERE 
                idcoletor = %s 
            AND 
                cidade_idcidade = %s
            """
            self.cursor.execute(sql_query, (novo_nome, novo_cnpjCpf, novo_telefone, novo_endereco, nova_dataCadastro, idcoletor, novo_idcidade))
            self.conexao.commit()
            if self.cursor.rowcount > 0:
                print(f"\n[+] Coletor ID {idcoletor} atualizado para '{novo_nome}' com sucesso.")
            else:
                print(f"Nenhum coletor com o ID {idcoletor}.")
        except Error as e:
            self.conexao.rollback()
            print(f"Erro ao atualizar dados: {e}")

        
    def excluir_coletor(self, idcoletor):
        try:
            sql_query = "DELETE FROM coletor WHERE idcoletor = %s"
            self.cursor.execute(sql_query, (idcoletor,))
            self.conexao.commit()
            if self.cursor.rowcount > 0:
                print(f"[+] Coletor ID {idcoletor} excluído com sucesso!")
            else:
                print(f"Nenhum coletor com o ID {idcoletor}.")
        except Error as e:
            self.conexao.rollback()
            print(f"Erro ao excluir dados: {e}")
