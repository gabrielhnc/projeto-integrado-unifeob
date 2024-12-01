class TipoUsuario:
    def __init__(self, tipo):
        self.__tipo = tipo

    #Get
    def get_tipo(self):
        return self.__tipo

    #Set
    def set_tipo(self, tipo):
        self.__tipo = tipo
