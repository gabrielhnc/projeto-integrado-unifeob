from utils.crud import *

class RankingDB:
    def __init__(self, conexao, cursor):
        self.conexao = conexao
        self.cursor = cursor

    def consultar_ranking_usuarios(self):
        try:
            sql_query = """
            SELECT 
                RANK() OVER (ORDER BY SUM(e.quantidade) DESC) AS posicao,
                u.nome AS nome_usuario,
                CONCAT(FORMAT(SUM(e.quantidade), 1), ' g') AS quantidade_total,
                MAX(e.dataEntrada) AS ultima_entrada
            FROM 
                entrada e
            INNER JOIN usuario u ON e.usuario_idusuario = u.idusuario
            GROUP BY 
                u.nome
            ORDER BY 
                posicao
            """
            self.cursor.execute(sql_query)
            ranking = self.cursor.fetchall()

            if ranking:
                for i in range(len(ranking)):
                    ranking[i] = (str(ranking[i][0]) + '◦',) + ranking[i][1:]

                print("\n=== Ranking de Usuários por Quantidade Depositada ===")
                headers = ["Posição", "Nome", "Quantidade Total(g)", "Última Entrada"]
                print(tabulate(ranking, headers=headers, tablefmt="fancy_grid", stralign="center"))
            else:
                print("[!] Nenhum dado disponível para o ranking.")
        except Error as e:
            print(f"Erro ao buscar dados do ranking: {e}")


    def consultar_ranking_por_data(self, data_inicio, data_fim):
        try:
            sql_query = f"""
            SELECT 
                u.idusuario,
                u.nome AS nome_usuario,
                CONCAT(FORMAT(SUM(e.quantidade), 1), ' g') AS quantidade_total,
                MAX(e.dataEntrada) AS ultima_entrada
            FROM 
                entrada e
            INNER JOIN usuario u ON e.usuario_idusuario = u.idusuario
            WHERE 
                e.dataEntrada BETWEEN '{data_inicio}' AND '{data_fim}'
            GROUP BY 
                u.idusuario, u.nome
            ORDER BY 
                u.idusuario ASC;
            """
            self.cursor.execute(sql_query)
            ranking = self.cursor.fetchall()
            if ranking:
                print(f"\n=== Ranking de {data_inicio} a {data_fim} ===")
                headers = ["ID", "Usuário", "Quantidade Total(g)", "Última Entrada"]
                print(tabulate(ranking, headers=headers, tablefmt="fancy_grid"))
            else:
                print(f"[!] Nenhum dado encontrado para o intervalo de {data_inicio} a {data_fim}.")
        except Error as e:
            print(f"Erro ao buscar dados do ranking: {e}")


    def consultar_materiais_usuario(self, idusuario):
        try:
            sql_query_nome = """
            SELECT nome FROM usuario WHERE idusuario = %s
            """
            self.cursor.execute(sql_query_nome, (idusuario,))
            nome_usuario = self.cursor.fetchone()

            if nome_usuario:
                sql_query_materiais = """
                SELECT 
                    m.nome AS nome_material, 
                    CONCAT(FORMAT(e.quantidade, 1), ' g') AS quantidade, 
                    e.dataEntrada
                FROM 
                    entrada e
                INNER JOIN material m ON e.material_idmaterial = m.idmaterial
                WHERE 
                    e.usuario_idusuario = %s
                ORDER BY 
                    e.dataEntrada DESC
                """
                self.cursor.execute(sql_query_materiais, (idusuario,))
                materiais = self.cursor.fetchall()

                if materiais:
                    print(f"\n=== Materiais depositados por {nome_usuario[0]} ===")
                    headers = ["Material", "Quantidade(g)", "Data da Entrada"]
                    print(tabulate(materiais, headers=headers, tablefmt="fancy_grid"))
                else:
                    print(f"[!] Nenhum material depositado pelo usuário {nome_usuario[0]}.")
            else:
                print(f"[!] Usuário com ID {idusuario} não encontrado. \n[!] Tente novamente.")
        except Error as e:
            print(f"Erro ao buscar materiais: {e}")
