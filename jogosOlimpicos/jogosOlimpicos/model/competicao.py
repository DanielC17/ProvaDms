

class Competicao:

    def __init__(self, comp_id, nome, local, dataHora, tipo, participantes = None):
        self.id = comp_id
        self.nome = nome
        self.local = local
        self.dataHora = dataHora
        self.participantes = []
        self.tipo = tipo 
        self.encerrada = False
        self.lista_resultado = None
   
    def get_id(self):
        return self.id

    def set_id(self, comp_id):
        self.id = comp_id

    def get_nome(self):
        return self.nome

    def set_nome(self, nome):
        self.nome = nome
    
    def get_local(self):
        return self.local

    def set_local(self, local):
        self.local = local

    def get_dataHora(self):
        return self.dataHora

    def set_dataHora(self, dataHora):
        self.dataHora = dataHora

    def get_participantes(self):
        return self.participantes
    
    def get_encerrada(self):
        return self.encerrada

    def set_encerrada(self, encerrada):
        self.encerrada = encerrada

    def get_tipo(self):
        return self.tipo

    def set_tipo(self, tipo):
        self.tipo = tipo

    def get_lista_resultado(self):
        return self.lista_resultado

    def set_lista_resultado(self, lista_resultado):
        self.lista_resultado = lista_resultado

    def add_participante(self, participante):
        self.participantes.append(participante)
