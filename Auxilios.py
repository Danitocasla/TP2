from Tipos import *
# DEFINICION DE AUXILIOS


class Auxilio():
    def __init__(self, patente, zonaPartida, zonaDestino, tipo, estado):
        self.patente = patente

        if type(zonaPartida) is ZonaAuxilio:
            self.zonaPartida = zonaPartida
        else:
            raise Exception("No es valido el dato", type(zonaPartida))

        if type(zonaDestino) is ZonaAuxilio:
            self.zonaDestino = zonaDestino
        else:
            raise Exception("No es valido el dato", type(zonaDestino))

        if type(tipo) is TipoAuxilio:
            self.unTipo = tipo
        else:
            raise Exception("No es valido el dato", type(TipoAuxilio))

        if type(estado) is EstadoAuxilio:
            self.estado = estado
        else:
            raise Exception("No es valido el dato", type(EstadoAuxilio))

    def __repr__(self):
        return "Nro Patente: " + str(self.patente) + " Zona de Partida: " + str(self.zonaPartida) + " Zona Destino: " + str(self.zonaDestino) + " Tipo de Auxilio: " + str(self.unTipo) + " Estado: " + str(self.estado)

    def patente(self):
        return self.patente

    def zonaPartida(self):
        return self.zonaPartida

    def zonaDestino(self):
        return self.zonaDestino


    def tipo(self):
        return self.unTipo

    def estado(self):
        return self.estado

    def setTipo(self, nuevoTipo):
        self.unTipo = nuevoTipo

    def cambiarTipo(self):
        if self.unTipo is TipoAuxilio.Remolque:
            self.unTipo = TipoAuxilio.Reparacion
        else:
            self.unTipo = TipoAuxilio.Remolque
