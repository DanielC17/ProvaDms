

class Participantes:

    def __init__(self, id, nome, idade, altura, peso):
        self.id = id
        self.nome = nome
        self.idade = idade 
        self.altura = altura
        self.peso = peso 

    def get_id(self):
        return self.id 

    def set_id(self, id):
        self.id = id

    def get_nome(self):
        return self.nome 

    def set_nome(self, nome):
        self.nome = nome

    def get_idade(self):
        return self.idade 

    def set_idade(self, idade):
        self.idade = idade

    def get_altura(self):
        return self.altura

    def set_altura(self, altura):
        self.altura = altura

    def get_peso(self):
        return self.peso 

    def set_peso(self, peso):
        self.peso = peso
