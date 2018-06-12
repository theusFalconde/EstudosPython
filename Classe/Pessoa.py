#Pessoa.py

class Pessoa:
    __id = 0
    def __init__(self, nome, idade):
        self.__nome = nome
        self.__idade = idade
        Pessoa.__id +=1

    def getId(self):
        return self.__id

    def getNome(self):
        return self.__nome

    def getIdade(self):
        return self.__idade