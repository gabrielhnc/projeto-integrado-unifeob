class Entrada:
    def __init__(self, idusuario, iddeposito, idmaterial, dataEntrada, quantidade):
        self.__idusuario = idusuario
        self.__iddeposito = iddeposito
        self.__idmaterial = idmaterial
        self.__dataEntrada = dataEntrada
        self.__quantidade = quantidade

    #Get
    def get_idusuario(self):
        return self.__idusuario

    def get_iddeposito(self):
        return self.__iddeposito

    def get_idmaterial(self):
        return self.__idmaterial

    def get_dataEntrada(self):
        return self.__dataEntrada

    def get_quantidade(self):
        return self.__quantidade

    #Set
    def set_idusuario(self, idusuario):
        self.__idusuario = idusuario

    def set_iddeposito(self, iddeposito):
        self.__iddeposito = iddeposito

    def set_idmaterial(self, idmaterial):
        self.__idmaterial = idmaterial

    def set_dataEntrada(self, dataEntrada):
        self.__dataEntrada = dataEntrada

    def set_quantidade(self, quantidade):
        self.__quantidade = quantidade
