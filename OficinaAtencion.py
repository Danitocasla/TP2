from Queue import *
from Auxilios import *
from Tipos import *


# 2 colas: colaRemolque y colaReparacion
# interno de la central: 1 a 999
# cantidad critica de auxilios por defecto: 50


class OficinaAtencion():
    def __init__(self, nroInterno, cantCritica=50):
        self.colaRemolque = Queue()
        self.colaReparacion = Queue()
        self.interno = nroInterno
        self.cantCritica = cantCritica

    def interno(self):
        return self.interno
    ###################################################################

    def recibirAuxilio(self, auxilio):
        if type(auxilio) is TipoAuxilio:
            if auxilio.tipo() is TipoAuxilio.Remolque:
                self.situacionCritica()
                self.colaRemolque.enqueue(auxilio)
            else:
                self.situacionCritica()
                self.colaReparacion.enqueue(auxilio)
        else:
            raise Exception("Ingresar axilio válido")

    def primerAuxilioAEnviar(self):
        salida = "No hay auxilios disponibles"
        if self.colaRemolque.isEmpty:
            if not self.colaRemolque.isEmpty:
                salida = self.colaReparacion.top()
        else:
            salida = self.colaRemolque.top()
        return salida

    # recibe la zona donde se encuentra una grua
    # devuelve y desencola el primer auxilio que se le puede enviar,
    # la zonaDeGrua debe ser la zona De Partida del auxilio. remolques tienen prioridad
    def enviarAuxilio(self, zonaDeGrua):
        # no anda pero creo que es por acá
        clonRemolque = self.colaRemolque.clone()
        clonReparacion = self.colaReparacion.clone()
        salida = None
        encontrado = False
        self.colaRemolque.empty()
        while not clonRemolque.isEmpty():
            if clonRemolque.top().zonaPartida() == zonaDeGrua and not encontrado:
                salida = clonRemolque.dequeue()
                encontrado = True
            self.colaRemolque.enqueue(clonRemolque.dequeue())
        if salida == None:
            self.colaReparacion.empty()
            while not clonReparacion.isEmpty():
                if clonReparacion.top().zonaPartida() == zonaDeGrua and not encontrado:
                    salida = clonReparacion.dequeue()
                    encontrado = True
                self.colaReparacion.enqueue(clonReparacion.dequeue())
            if salida == None:
                print("No hay auxilio en la zona")
        return salida

    # retorna la cantidad de auxilios de cada tipo:, ej: Remolque: n ; Reparacion: n

    def auxiliosPorTipo(self):
        # Ver el orden que se espera y si es lo esperado
        return self.colaRemolque.size(), self.colaReparacion.size()

    # retorna la cantidad sumando las dos colas
    def cantidadTotalAuxilios(self):
        return self.colaRemolque.size() + self.colaReparacion.size()

    # retorna true si alguna de las dos colas supera la cant critica
    def esCritica(self):
        return self.esCriticaRemolque() or self.esCriticaReparacion()
    # funciones auxiliares

    def esCriticaRemolque(self):
        return self.colaRemolque.size() >= self.cantCritica

    def esCriticaReparacion(self):
        return self.colaReparacion.size() >= self.cantCritica

    # retorna el total de auxilios con estado: espera. sumando las dos colas
    def auxiliosEnEspera(self):
        return self.contarEnEspera(self.colaRemolque) + self.contarEnEspera(self.colaReparacion)

    # recibe una patente
    # retorna(sin eliminarlo) el auxilio pedido por esa patente si hay alguno en las colas
    def buscarAuxilio(self, nroPatente):
        clonRemolque = self.colaRemolque.clone()
        clonReparacion = self.colaReparacion.clone()
        salida = None
        while not clonRemolque.isEmpty():
            if clonRemolque.top().patente() == nroPatente:
                salida = clonRemolque.top()
            clonRemolque.dequeue()
        while not clonReparacion.isEmpty():
            if clonReparacion.top().patente() == nroPatente:
                salida = clonReparacion.top()
            clonReparacion.dequeue()
        if salida == None:
            salida = "No hay auxilios con ese número de patente"
        return salida

    # recibe una patente
    # elimina el auxilio pedido por esa patente  si hay.
    def eliminarAuxilio(self, nroPatente):
        clonRemolque = self.colaRemolque.clone()
        clonReparacion = self.colaReparacion.clone()
        self.colaRemolque.empty()
        while not clonRemolque.isEmpty():
            if clonRemolque.top().patente() != nroPatente:
                self.colaRemolque.enqueue(clonRemolque.top())
            clonRemolque.dequeue()
        self.colaReparacion.empty()
        while not clonReparacion.isEmpty():
            if clonReparacion.top().patente() != nroPatente:
                self.colaReparacion.enqueue(clonReparacion.top())
            clonReparacion.dequeue()
                
    # recibe una patente
    # verifica que exista un pedido de esa patente
    # lo cambia de cola(reparacion - remolque)
    def cambiaDeTipo(self, nroPatente):
        aux = self.buscarAuxilio(nroPatente)
        if aux != None:
            aux.cambiarTipo()

    def situacionCritica(self):
        if self.esCritica():
            print("Situación Crírtica")

    def contarEnEspera(self, cola):
        clon = cola.clone()
        count = 0
        for i in range(len(clon)):
            aux = clon.dequeue()
            if aux.enEspera():
                count += 1
        return count
