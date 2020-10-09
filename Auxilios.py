from Tipos import *

class Auxilio():
    # Modelo TDA de los auxilios pedidos por los clientes.
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
        # Función para representar un auxilio
        return "Nro Patente: " + str(self.patente) + " Zona de Partida: " + str(self.zonaPartida) + " Zona Destino: " + str(self.zonaDestino) + " Tipo de Auxilio: " + str(self.unTipo) + " Estado: " + str(self.estado)
    
    def patente(self):
        # Getter de patente de auxilio.
        return self.patente

    def zonaPartida(self):
        # Getter Zona de Partida de auxilio.
        return self.zonaPartida

    def zonaDestino(self):
        # Getter Zona de Destino de auxilio.
        return self.zonaDestino

    def tipo(self):
        # Getter de Tipo de auxilio.
        return self.unTipo

    def estado(self):
        # Getter de Estado de auxilio.
        return self.estado

    def setTipo(self, nuevoTipo):
        # Setter de nuevo tipo de auxilio.
        self.unTipo = nuevoTipo

    def cambiarTipo(self):
        # Función para cambio de tipo de auxilio.
        if self.unTipo is TipoAuxilio.Remolque:
            self.unTipo = TipoAuxilio.Reparacion
        else:
            self.unTipo = TipoAuxilio.Remolque
