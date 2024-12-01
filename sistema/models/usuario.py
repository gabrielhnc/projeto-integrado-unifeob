class Usuario:
    def __init__(self, nome, email, telefone, dataCadastro, idtipoUsuario):
        self.__nome = nome
        self.__email = email
        self.__telefone = telefone
        self.__dataCadastro = dataCadastro
        self.__idtipoUsuario = idtipoUsuario

    #Get
    def get_nome(self):
        return self.__nome

    def get_email(self):
        return self.__email

    def get_telefone(self):
        return self.__telefone

    def get_dataCadastro(self):
        return self.__dataCadastro

    def get_idtipoUsuario(self):
        return self.__idtipoUsuario

    #Set
    def set_nome(self, nome):
        self.__nome = nome

    def set_email(self, email):
        self.__email = email

    def set_telefone(self, telefone):
        self.__telefone = telefone

    def set_dataCadastro(self, dataCadastro):
        self.__dataCadastro = dataCadastro

    def set_idtipoUsuario(self, idtipoUsuario):
        self.__idtipoUsuario = idtipoUsuario
