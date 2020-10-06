from Stack import *
from Queue import *

## edificio -> m pisos -> n habitaculo/oficina
## la oficina tiene su nro de interno o "None" si esta vacio
class EdificioEmpresa():
    def __init__(self, cantPisos, cantHabitaculos):
        edificio = Stack()
        habitaculos = Queue()
        for piso in range(cantPisos):
            for habitaculo in range(cantHabitaculos):
                habitaculos[habitaculo].enqueue(None)
            edificio[piso].push(habitaculos)
        self.edificioEmpresa = edificio

    
    # recibe un nro de piso, nro de habitaculo y una oficina
    # pone la oficina en el habitaculo designado
    def establecerOficina(self, numeroPiso, numeroHabitaculo, oficinaAtencion):
        self.edificioEmpresa[numeroPiso][numeroHabitaculo] = oficinaAtencion

    ## RECURSIVA
    # retorna la cantidad de oficinas en situacion critica en el piso recibido
    def cantidadDeOficinasCriticas(self, piso):
        pass

    # retorna piso y habitaculo de la oficina con menor cant de auxilios tipo Remolque pendientes
    def oficinaMenosRecargada(self):
        pass

    # recibe en un nro de interno
    # retorna el piso y habitaculo donde se encuentra
    def buscaOficina(self, nroInterno):
        pass

# recibe una PILA de auxilios y los reparte de a uno a la oficina menos recargada
# (verificar entre cada entrega cual es la menos recargada)
    def centralTelefonica(self, pilaDeAuxilios):
        pass

# recibe un nro de patente, un nro interno de origen y otro nro de interno de destino
# mueve el auxilio de esa patente desde el interno de origen al interno de destino
    def moverAuxilio(self, nroPatente, internoOficinaOrigen, internoOficinaDestino):
        pass
