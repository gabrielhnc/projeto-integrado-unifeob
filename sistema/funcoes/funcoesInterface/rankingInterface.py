from utils.interface import *
del obter_hora, obter_status, obter_quantidade
from funcoes.funcoesCRUD.rankingdb import RankingDB
from funcoes.funcoesCRUD.usuariodb import UsuarioDB

class RankingInterface:
    def __init__(self, banco):
        self.rankingdb = RankingDB(banco.conexao, banco.cursor)
        self.usuariodb = UsuarioDB(banco.conexao, banco.cursor)
    
    def consultar_ranking_usuarios(self):
        print("\nConsultando ranking...")
        time.sleep(1)
        self.rankingdb.consultar_ranking_usuarios()


    def consultar_ranking_por_data(self):
        print("\n==== Consulta por Data ====")

        data_inicio = obter_data("\nDigite a data de início (DD/MM/YYYY) [0 para cancelar]: ")
        if data_inicio is None:
            return
        
        data_fim = obter_data("Digite a data de fim (DD/MM/YYYY) [0 para cancelar]: ")
        if data_fim is None:
            return
        
        print(f"\nFiltrando resultados entre {data_inicio} e {data_fim}...")
        time.sleep(1)
        self.rankingdb.consultar_ranking_por_data(conversao_data(data_inicio), conversao_data(data_fim))


    def consultar_materiais_depositados(self):
        print("\nConsultando usuários...")
        time.sleep(1)
        self.usuariodb.consultar_usuarios()

        while True:
            try:
                nome_usuario = input("\nDigite o ID do usuário para visualizar os materiais depositados [0 para cancelar]: ").strip()
                if nome_usuario == '0':
                    print("[!] Consulta cancelada.")
                    return
                elif nome_usuario:
                    print("\nVerificando escolha...")
                    time.sleep(2)
                    self.rankingdb.consultar_materiais_usuario(nome_usuario)
            except ValueError:
                print("Digite um numero valido.")
