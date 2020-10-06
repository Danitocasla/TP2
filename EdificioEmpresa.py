from Stack import *
from Queue import *
from OficinaAtencion import *

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
        self.cantPisos = cantPisos
        self.cantHabitaculos = cantHabitaculos

    
    # recibe un nro de piso, nro de habitaculo y una oficina
    # pone la oficina en el habitaculo designado
    def establecerOficina(self, numeroPiso, numeroHabitaculo, oficinaAtencion):
        self.edificioEmpresa[numeroPiso][numeroHabitaculo] = oficinaAtencion

    ## RECURSIVA
    # retorna la cantidad de oficinas en situacion critica en el piso recibido
    def cantidadDeOficinasCriticas(self, piso):
        cantidad = 0
        for i in range(self.edificioEmpresa[piso].size()):
            if (self.edificioEmpresa[piso] [i]) != None and (self.edificioEmpresa[piso] [i]).esCritica():
                cantidad += 1
        return cantidad

    # retorna piso y habitaculo de la oficina con menor cant de auxilios tipo Remolque pendientes
    # hay que recorrer la matriz(self.edificioEmpresa) y devolver la 
    # oficina.cantidadTotalAuxilios()
    def oficinaMenosRecargada(self):
        pass

    # recibe en un nro de interno
    # retorna el piso y habitaculo donde se encuentra
    def buscaOficina(self, nroInterno):
        for i in range(self.cantPisos):
            for j in range(self.cantHabitaculos):
                if (self.edificioEmpresa[i] [j]) != None and (self.edificioEmpresa[i] [j]).interno() == nroInterno:
                    return i , j

# recibe una PILA de auxilios y los reparte de a uno a la oficina menos recargada
# (verificar entre cada entrega cual es la menos recargada)
    def centralTelefonica(self, pilaDeAuxilios):
        for element in pilaDeAuxilios:
            self.oficinaMenosRecargada().enqueue(element)

# recibe un nro de patente, un nro interno de origen y otro nro de interno de destino
# mueve el auxilio de esa patente desde el interno de origen al interno de destino
    def moverAuxilio(self, nroPatente, internoOficinaOrigen, internoOficinaDestino):
        pisoOrigen,habitaculoOrigen = self.buscaOficina(internoOficinaOrigen)
        pisoDestino,habitaculoDestino = self.buscaOficina(internoOficinaDestino)
        self.edificioEmpresa[pisoDestino][habitaculoDestino].recibirAuxilio((self.edificioEmpresa[pisoOrigen][habitaculoOrigen]).buscarAuxilio(nroPatente))
        self.edificioEmpresa[pisoOrigen][habitaculoOrigen].eliminarAuxilio(nroPatente)
