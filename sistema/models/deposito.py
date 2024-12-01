class Deposito:
    def __init__(self, nome, endereco, cep, idcidade, telefone, capacidadeMaxima, dataCadastro, horaAbertura, horaFechamento):
        self.__nome = nome 
        self.__endereco = endereco 
        self.__cep = cep 
        self.__idcidade = idcidade  
        self.__telefone = telefone  
        self.__capacidadeMaxima = capacidadeMaxima 
        self.__dataCadastro = dataCadastro 
        self.__horaAbertura = horaAbertura  
        self.__horaFechamento = horaFechamento  

    #Get
    def get_nome(self):
        return self.__nome

    def get_endereco(self):
        return self.__endereco

    def get_cep(self):
        return self.__cep

    def get_idcidade(self):
        return self.__idcidade

    def get_telefone(self):
        return self.__telefone

    def get_capacidadeMaxima(self):
        return self.__capacidadeMaxima

    def get_dataCadastro(self):
        return self.__dataCadastro

    def get_horaAbertura(self):
        return self.__horaAbertura

    def get_horaFechamento(self):
        return self.__horaFechamento

    #Set
    def set_nome(self, nome):
        self.__nome = nome

    def set_endereco(self, endereco):
        self.__endereco = endereco

    def set_cep(self, cep):
        self.__cep = cep

    def set_idcidade(self, idcidade):
        self.__idcidade = idcidade

    def set_telefone(self, telefone):
        self.__telefone = telefone

    def set_capacidadeMaxima(self, capacidadeMaxima):
        self.__capacidadeMaxima = capacidadeMaxima

    def set_dataCadastro(self, dataCadastro):
        self.__dataCadastro = dataCadastro

    def set_horaAbertura(self, horaAbertura):
        self.__horaAbertura = horaAbertura

    def set_horaFechamento(self, horaFechamento):
        self.__horaFechamento = horaFechamento
