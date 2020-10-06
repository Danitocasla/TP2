# DEFINICION DE AUXILIOS
class Auxilio():
    def __init__(self, patente, zonaPartida, zonaDestino, tipo, estado):
        self.patente = patente
        self.zonaPartida = zonaPartida
        self.zonaDestino = zonaDestino
        self.tipo = tipo
        self.estado = estado

    def patente(self):
        return self.patente

    def zonaPartida(self):
        return self.zonaPartida

    def zonaDestino(self):
        return self.zonaDestino

    def tipo(self):
        return self.tipo

    def estado(self):
        return self.estado
