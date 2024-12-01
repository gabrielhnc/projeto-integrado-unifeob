class Material:
    def __init__(self, nome, descricao, idcategoria):
        self.__nome = nome
        self.__descricao = descricao
        self.__idcategoria = idcategoria

    #Get
    def get_nome(self):
        return self.__nome

    def get_descricao(self):
        return self.__descricao

    def get_idcategoria(self):
        return self.__idcategoria

    #Set
    def set_nome(self, nome):
        self.__nome = nome

    def set_descricao(self, descricao):
        self.__descricao = descricao

    def set_idcategoria(self, idcategoria):
        self.__idcategoria = idcategoria
