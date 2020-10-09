from Stack import *
from Queue import *
from OficinaAtencion import *

# edificio -> m pisos -> n habitaculo/oficina
# la oficina tiene su nro de interno o "None" si esta vacio


class EdificioEmpresa():
    def __init__(self, cantPisos, cantHabitaculos):
        edificio = []
        for i in range(cantPisos):
            edificio.append([])
            for j in range(cantHabitaculos):
                edificio[i].append(None)
        self.edificioEmpresa = edificio
        self.cantPisos = cantPisos
        self.cantHabitaculos = cantHabitaculos

    # recibe un nro de piso, nro de habitaculo y una oficina
    # pone la oficina en el habitaculo designado
    def __repr__(self):
        return str(self.edificioEmpresa)

    def establecerOficina(self, numeroPiso, numeroHabitaculo, oficinaAtencion):
        self.edificioEmpresa[numeroPiso][numeroHabitaculo] = oficinaAtencion

    # retorna la cantidad de oficinas en situacion critica en el piso recibido
    def cantidadDeOficinasCriticas(self, piso):
        count = 0
        for i in range(len(self.edificioEmpresa[piso])):
            if self.edificioEmpresa[piso][i]!= None:
                if self.edificioEmpresa[piso][i].esCritica():
                    count+=1
        return count

    # retorna piso y habitaculo de la oficina con menor cant de auxilios tipo Remolque pendientes
    # hay que recorrer la matriz(self.edificioEmpresa) y devolver la
    # oficina.cantidadTotalAuxilios()
    def oficinaMenosRecargada(self):
        salida = None
        oficina = None
        cantTotAux = 0
        for nroPiso in range(len(self.edificioEmpresa)):
            for habitaculo in range(len(self.edificioEmpresa[nroPiso])):
                pass
        

    # recibe en un nro de interno
    # retorna el piso y habitaculo donde se encuentra

    def hayOficinaEn(self, nroPiso, nroHabitaculo):
        return self.edificioEmpresa[nroPiso][nroHabitaculo] != None


    def buscaOficina(self, nroInterno):
        for i in range(self.cantPisos):
            for j in range(self.cantHabitaculos):
                if self.hayOficinaEn(i, j):
                    if (self.edificioEmpresa[i][j]).interno == nroInterno:
                        salida = i , j
        return salida

    # recibe una PILA de auxilios y los reparte de a uno a la oficina menos recargada
    # (verificar entre cada entrega cual es la menos recargada)
    def centralTelefonica(self, pilaDeAuxilios):
        for element in pilaDeAuxilios:
            self.oficinaMenosRecargada().append(element)

    # recibe un nro de patente, un nro interno de origen y otro nro de interno de destino
    # mueve el auxilio de esa patente desde el interno de origen al interno de destino
    def moverAuxilio(self, nroPatente, internoOficinaOrigen, internoOficinaDestino):

        pisoOrigen, habOrigen = self.buscaOficina(internoOficinaOrigen)
        pisoDestino, habDestino = self.buscaOficina(internoOficinaDestino)
        oficinaOrigen = self.edificioEmpresa[pisoOrigen][habOrigen]
        oficinaDestino = self.edificioEmpresa[pisoDestino][habDestino]
        oficinaDestino.recibirAuxilio(oficinaOrigen.buscarAuxilio(nroPatente))
        oficinaOrigen.eliminarAuxilio(nroPatente)
