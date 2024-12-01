class Saida:
    def __init__(self, iddeposito, idcoletor, idmaterial, dataSaida, quantidade):
        self.__iddeposito = iddeposito
        self.__idcoletor = idcoletor
        self.__idmaterial = idmaterial
        self.__dataSaida = dataSaida
        self.__quantidade = quantidade

    #Get
    def get_iddeposito(self):
        return self.__iddeposito

    def get_idcoletor(self):
        return self.__idcoletor

    def get_idmaterial(self):
        return self.__idmaterial

    def get_dataSaida(self):
        return self.__dataSaida

    def get_quantidade(self):
        return self.__quantidade

    #Set
    def set_iddeposito(self, iddeposito):
        self.__iddeposito = iddeposito

    def set_idcoletor(self, idcoletor):
        self.__idcoletor = idcoletor

    def set_idmaterial(self, idmaterial):
        self.__idmaterial = idmaterial

    def set_dataSaida(self, dataSaida):
        self.__dataSaida = dataSaida

    def set_quantidade(self, quantidade):
        self.__quantidade = quantidade
