class Cidade:
    def __init__(self, nome, idestado):
        self.__nome = nome 
        self.__idestado = idestado  

    #Get
    def get_nome(self):
        return self.__nome

    def get_idestado(self):
        return self.__idestado

    #Set
    def set_nome(self, nome):
        self.__nome = nome

    def set_idestado(self, idestado):
        self.__idestado = idestado
