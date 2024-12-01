class Agendamento:
    def __init__(self, data, hora, status, idcoletor):
        self.__data = data  
        self.__hora = hora  
        self.__status = status  
        self.__idcoletor = idcoletor 

    #Get
    def get_data(self):
        return self.__data

    def get_hora(self):
        return self.__hora

    def get_status(self):
        return self.__status

    def get_idcoletor(self):
        return self.__idcoletor

    #Set
    def set_data(self, data):
        self.__data = data

    def set_hora(self, hora):
        self.__hora = hora

    def set_status(self, status):
        self.__status = status

    def set_idcoletor(self, idcoletor):
        self.__idcoletor = idcoletor
