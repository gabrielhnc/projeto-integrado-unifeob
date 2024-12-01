class Coletor:
    def __init__(self, nome, cnpjCpf, telefone, endereco, idcidade, dataCadastro):
        self.__nome = nome  
        self.__cnpjCpf = cnpjCpf  
        self.__telefone = telefone  
        self.__endereco = endereco  
        self.__idcidade = idcidade  
        self.__dataCadastro = dataCadastro  

    #Get
    def get_nome(self):
        return self.__nome

    def get_cnpjCpf(self):
        return self.__cnpjCpf

    def get_telefone(self):
        return self.__telefone

    def get_endereco(self):
        return self.__endereco

    def get_idcidade(self):
        return self.__idcidade

    def get_dataCadastro(self):
        return self.__dataCadastro

    #Set
    def set_nome(self, nome):
        self.__nome = nome

    def set_cnpjCpf(self, cnpjCpf):
        self.__cnpjCpf = cnpjCpf

    def set_telefone(self, telefone):
        self.__telefone = telefone

    def set_endereco(self, endereco):
        self.__endereco = endereco

    def set_idcidade(self, idcidade):
        self.__idcidade = idcidade

    def set_dataCadastro(self, dataCadastro):
        self.__dataCadastro = dataCadastro
