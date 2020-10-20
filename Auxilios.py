from Tipos import *

class Auxilio():
    # Modelo TDA de los auxilios pedidos por los clientes.
    def __init__(self, patente, zonaPartida, zonaDestino, tipo, estado):
        self.patente = patente
        self.zonaPartida = validarZona(zonaPartida)
        self.zonaDestino = validarZona(zonaDestino)
        self.unTipo = validarTipo(tipo)
        self.estado = validarEstado(estado)

    def __repr__(self):
        # Función para representar un auxilio
        return "Nro Patente: " + str(self.patente) + " Zona de Partida: " + str(self.zonaPartida) + " Zona Destino: " + str(self.zonaDestino) + " Tipo de Auxilio: " + str(self.unTipo) + " Estado: " + str(self.estado)
    
    def patente(self):
        # Getter de patente de auxilio.
        return self.patente

    def esPatente(self, patente):
        # Getter de patente de auxilio.
        return self.patente == patente
    
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
        if self.esTipoRemolque:
            self.unTipo = TipoAuxilio.Reparacion
        else:
            self.unTipo = TipoAuxilio.Remolque

    def esTipoRemolque(self):
        return self.unTipo is TipoAuxilio.Remolque
    
    def esZonaPartida(self, unaZona):
        # Función de verificacion de zona
        return self.zonaPartida == unaZona

##########################################################################################################
########################## Definición de Funciones de Validación #########################################
##########################################################################################################


def validarZona(zonaAux):
    if type(zonaAux) is ZonaAuxilio:
        return zonaAux
    else:
        raise Exception("No es valido el dato", type(ZonaAuxilio))


def validarTipo(tipoAux):
    if type(tipoAux) is TipoAuxilio:
        return tipoAux
    else:
        raise Exception("No es valido el dato", type(TipoAuxilio))


def validarEstado(estadoAux):
    if type(estadoAux) is EstadoAuxilio:
        return estadoAux
    else:
        raise Exception("No es valido el dato", type(EstadoAuxilio))
