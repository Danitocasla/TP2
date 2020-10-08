
from Tipos import *
# DEFINICION DE AUXILIOS


class Auxilio():
    def __init__(self, patente, zonaPartida, zonaDestino, tipo, estado):
        self.patente = patente
        self.zonaPartida = zonaPartida
        self.zonaDestino = zonaDestino
        self.unTipo = tipo
        self.estado = estado

    def __repr__(self):
        return str(self.patente)+str(self.zonaPartida)+str(self.zonaDestino)+str(self.unTipo)+str(self.estado)

    def patente(self):
        return self.patente

    def zonaPartida(self):
        return self.zonaPartida

    def zonaDestino(self):
        return self.zonaDestino

    def esTipoReparacion(self):
        return self.unTipo

    def setTipo(self, nuevoTipo):
        self.unTipo = nuevoTipo

    def cambiarTipo(self):
        if self.unTipo.value == 0:
            self.setTipo(TipoAuxilio.Reparacion)
        else:
            self.setTipo(TipoAuxilio.Remolque)

    def estado(self):
        return self.estado
