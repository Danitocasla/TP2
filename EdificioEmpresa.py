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
        self.edificioEmpresa[numeroPiso][numeroHabitaculo] = oficinaAtencion

    def cantidadDeOficinasCriticas(self, piso):
        # Retorna la cantidad de oficinas Críticas en el piso recibido por parámetro.
        count = 0
        for i in range(len(self.edificioEmpresa[piso])):
            if self.edificioEmpresa[piso][i] != None:
                if self.edificioEmpresa[piso][i].esCritica():
                    count += 1
        return count

    def oficinaMenosRecargada(self):
        # Retorna la ubicación (número de piso y número de habitáculo) de la oficina
        # que tiene el menor número de auxilios.
        salida = None
        oficina = None
        for nroPiso in range(len(self.edificioEmpresa)):
            for habitaculo in range(len(self.edificioEmpresa[nroPiso])):
                if self.edificioEmpresa[nroPiso][habitaculo] != None:
                    if oficina == None:
                        oficina = self.edificioEmpresa[nroPiso][habitaculo]
                    elif oficina.cantidadTotalAuxilios() > self.edificioEmpresa[nroPiso][habitaculo].cantidadTotalAuxilios():
                        oficina = self.edificioEmpresa[nroPiso][habitaculo]
        return oficina

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
        for element in pilaDeAuxilios:
            self.oficinaMenosRecargada().append(element)

    def moverAuxilio(self, nroPatente, internoOficinaOrigen, internoOficinaDestino):
        # Saca el auxilio del vehículo con patente nroPatente de la oficina internoOficinaOrigen
        # y lo pasa a la oficina de internoOficinaDestino.
        pisoOrigen, habOrigen = self.buscaOficina(internoOficinaOrigen)
        pisoDestino, habDestino = self.buscaOficina(internoOficinaDestino)
        oficinaOrigen = self.edificioEmpresa[pisoOrigen][habOrigen]
        oficinaDestino = self.edificioEmpresa[pisoDestino][habDestino]
        oficinaDestino.recibirAuxilio(oficinaOrigen.buscarAuxilio(nroPatente))
        oficinaOrigen.eliminarAuxilio(nroPatente)
