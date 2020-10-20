from Stack import *
from Queue import *
from OficinaAtencion import *


class EdificioEmpresa():
    # Definición de un TDA que modela un Edificio de la Empresa de M pisos con N habitáculos
    def __init__(self, cantPisos, cantHabitaculos):
        edificio = []
        for i in range(cantPisos):
            edificio.append([])
            for j in range(cantHabitaculos):
                edificio[i].append(None)
        self.edificioEmpresa = edificio
        self.cantPisos = cantPisos
        self.cantHabitaculos = cantHabitaculos

    def __repr__(self):
        # Definición para representación del objeto Edificio Empresa
        return str(self.edificioEmpresa)

    def establecerOficina(self, numeroPiso, numeroHabitaculo, oficinaAtencion):
        # Pone la oficinaAtencion en habitáculo correspondiente.
        if not self.hayOficinaEn(numeroPiso, numeroHabitaculo):
            self.edificioEmpresa[numeroPiso][numeroHabitaculo] = oficinaAtencion
        else:
            raise Exception(
                "El Habitáculo está ocupado, intente en otro Habitáculo")

    def cantidadDeOficinasCriticas(self, nroPiso):
        # Retorna la cantidad de oficinas Críticas en el Número de piso recibido por parámetro.
        piso = self.edificioEmpresa[nroPiso]
        count = self.oficinasCriticasEnPisoRec(piso)
        return count

    def hayOficinaEnPiso(self, piso, habitaculo):
        # Retorna si hay una oficina en el Piso y Habitaculo indicado por parámetro (Booleano).
        return piso[habitaculo] != None

    def oficinasCriticasEnPisoRec(self, piso):
        # Retorna la cantidad de oficinas Críticas en el Piso recibido por parámetro de forma Recursiva.
        count = 0
        if len(piso) == 1:
            return 1 if self.hayOficinaEnPiso(piso, len(piso)-1) else 0
        else:
            count = 1 if self.hayOficinaEnPiso(piso, len(piso)-1) else 0
            count += self.oficinasCriticasEnPisoRec(piso[0:len(piso)-1])
        return count

    def oficinaMenosRecargada(self):
        # Retorna la ubicación (número de piso y número de habitáculo) de la oficina
        # que tiene el menor número de auxilios.
        oficina = None
        salida = None
        for nroPiso in range(len(self.edificioEmpresa)):
            for habitaculo in range(len(self.edificioEmpresa[nroPiso])):
                if self.hayOficinaEn(nroPiso, habitaculo):
                    if oficina == None:
                        salida = nroPiso, habitaculo
                    elif oficina.cantidadTotalAuxilios() > self.edificioEmpresa[nroPiso][habitaculo].cantidadTotalAuxilios():
                        salida = nroPiso, habitaculo
        return salida

    def hayOficinaEn(self, nroPiso, nroHabitaculo):
        # Retorna si hay una oficina en el nroPiso y nroHabitaculo indicado (Booleano).
        return self.edificioEmpresa[nroPiso][nroHabitaculo] != None

    def buscaOficina(self, nroInterno):
        # Recibe el número de interno y retorna la ubicación de la oficina en el edificio
        # (número de piso y número de habitáculo).
        for i in range(self.cantPisos):
            for j in range(self.cantHabitaculos):
                if self.hayOficinaEn(i, j):
                    if (self.edificioEmpresa[i][j]).interno == nroInterno:
                        salida = i, j
        return salida

    def centralTelefonica(self, pilaDeAuxilios):
        # Recibe como entrada una pila de auxilios y debe enviar los auxilios de a uno a la
        # oficina menos recargada.
        piso, habitaculo = self.oficinaMenosRecargada
        while not pilaDeAuxilios.isEmpty():
            self.edificioEmpresa[piso][habitaculo].recibirAuxilio(pilaDeAuxilios.pop())

    def moverAuxilio(self, nroPatente, internoOficinaOrigen, internoOficinaDestino):
        # Saca el auxilio del vehículo con patente nroPatente de la oficina internoOficinaOrigen
        # y lo pasa a la oficina de internoOficinaDestino.
        pisoOrigen, habOrigen = self.buscaOficina(internoOficinaOrigen)
        pisoDestino, habDestino = self.buscaOficina(internoOficinaDestino)
        if self.hayOficinaEn(pisoOrigen, habOrigen):
            oficinaOrigen = self.edificioEmpresa[pisoOrigen][habOrigen]
            oficinaDestino = self.edificioEmpresa[pisoDestino][habDestino]
            oficinaDestino.recibirAuxilio(
                oficinaOrigen.buscarAuxilio(nroPatente))
            oficinaOrigen.eliminarAuxilio(nroPatente)
        else:
            raise Exception("No hay Auxilio a Mover")
