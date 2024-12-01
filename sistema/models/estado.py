class Estado:
    def __init__(self, idestado, nome):
        self.__idestado = idestado
        self.__nome = nome

    #Get
    def get_idestado(self):
        return self.__idestado

    def get_nome(self):
        return self.__nome
    
    #Set
    def set_idestado(self, idestado):
        self.__idestado = idestado

    def set_nome(self, nome):
        self.__nome = nome
