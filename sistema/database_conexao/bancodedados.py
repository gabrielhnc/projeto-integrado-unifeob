# Classe responsável por realizar a conexao com o banco recebendo os parametros no arquivo 'main.py'

import mysql.connector

class BancoDeDados:
    def __init__(self, host, user, password, database):
        self.host = host
        self.user = user
        self.password = password
        self.database = database

    def conectar(self):
        try:
            self.conexao = mysql.connector.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                database=self.database
            )
            self.cursor = self.conexao.cursor()
            print("\nConexão com o banco de dados estabelecida com SUCESSO.\n")
        except mysql.connector.Error as e:
            print(f"Erro ao conectar com o banco de dados: {e}")

    def desconectar(self):
        if self.conexao and self.cursor:
            self.cursor.close() 
            self.conexao.close()
            print("Conexão com o banco de dados encerrada com SUCESSO.\n")
        else:
            print("Nenhuma conexão ativa para desconectar.")
