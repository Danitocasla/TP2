from Queue import *
from Auxilios import *
from Tipos import *

# Definición de TDA que representa una oficina donde se reciben las llamadas de los clientes,
# y maneja dos colas de auxilios. Cada ocina se identica con el interno en la central telefónica.
# Las oficinas tienen una cantidad crítica de auxilios de cada tipo (por defecto 50 pedidos)


class OficinaAtencion():
    def __init__(self, nroInterno, cantCritica=50):
        self.colaRemolque = Queue()
        self.colaReparacion = Queue()
        self.interno = nroInterno
        self.cantCritica = cantCritica

    def interno(self):
        return self.interno

    def __repr__(self):
        return "Interno: " + str(self.interno)

    def recibirAuxilio(self, auxilio):
        # Agrega el auxilio que recibe por parámetro a la cola que corresponde
        # a su tipo. Si se excede la cantidad crítica en alguna cola, se almacena
        # el auxilio, pero se debe informar por pantalla la situación
        if auxilio.tipo() is TipoAuxilio.Remolque:
            self.situacionCritica()
            self.colaRemolque.enqueue(auxilio)
        else:
            self.situacionCritica()
            self.colaReparacion.enqueue(auxilio)

    def primerAuxilioAEnviar(self):
        # Retorna el primer auxilio a enviar a los conductores de las grúas
        # No desencola el pedido, solo lo muestra.
        salida = "No hay auxilios disponibles"
        if self.colaRemolque.isEmpty():
            if not self.colaReparacion.isEmpty():
                salida = self.colaReparacion.top()
        else:
            salida = self.colaRemolque.top()
        return salida

    def enviarAuxilio(self, zonaDeGrua):
        # Recibe por parámetro la zona en donde se encuentra una
        # grúa y desencola y retorna el primer auxilio que se le puede enviar
        # Los pedidos de Remolque se tratan primero, si no hay ninguno de
        # Remolque en la zona, se tratan los de Reparación.
        clonRemolque = self.colaRemolque.clone()
        clonReparacion = self.colaReparacion.clone()
        salida = None
        if salida == None:
            salida = self.buscarPorZona(zonaDeGrua, self.colaRemolque)
        if salida == None:
            salida = self.buscarPorZona(zonaDeGrua, self.colaReparacion)
        return salida

    def auxiliosPorTipo(self):
        # retorna la cantidad de auxilios de cada tipopor separado.
        return self.colaRemolque.size(), self.colaReparacion.size()

    def cantidadTotalAuxilios(self):
        # retorna la cantidad total de auxilios en la oficina de atención.
        return self.colaRemolque.size() + self.colaReparacion.size()

    def esCritica(self):
        # retorna si alguna de las dos colas supera la cant critica (Booleano).
        return self.colaRemolque.size() >= self.cantCritica or self.colaReparacion.size() >= self.cantCritica

    def auxiliosEnEspera(self):
        # retorna el total de auxilios con estado: espera de la oficina de atención.
        return self.contarEnEspera(self.colaRemolque) + self.contarEnEspera(self.colaReparacion)

    def buscarAuxilio(self, nroPatente):
        # Recibe un número de patente (nroPatente) y si en alguna de las colas de auxilios hay un pedido para
        # ese vehiculo, lo retorna y desencola.
        salida = None
        if salida == None:
            salida = self.buscarPorPatente(nroPatente, self.colaRemolque)
        if salida == None:
            salida = self.buscarPorPatente(nroPatente, self.colaReparacion)
        return salida

    def buscarPorPatente(self, nroPatente, cola):
        # De una cola recibida por parámetro se busca un auxilio por patente
        clonR = cola.clone()
        cola.empty()
        salida = None
        while not clonR.isEmpty():
            if clonR.top().esPatente(nroPatente):
                salida = clonR.top()
            cola.enqueue(clonR.dequeue())
        return salida

    def eliminarAuxilio(self, nroPatente):
        # Recibe un número de patente (nroPatente) y si hay un pedido de auxilio para ese vehículo en alguna
        # de las colas de la oficina de atención, lo elimina de ella.
        self.buscarAuxilio(nroPatente)

    def cambiaDeTipo(self, nroPatente):
        # Cambia el tipo del auxilio del vehículo con la patente nroPatente (de Reparación a Remolque o viceversa),
        # en consecuencia, debe cambiarlo de cola.
        aux = self.buscarAuxilio(nroPatente)
        if aux != None:
            aux.cambiarTipo()
            self.recibirAuxilio(aux)

    def situacionCritica(self):
        # Imprime mensaje si la ditiacion de la oficina es Crítica.
        if self.esCritica():
            print("Situación Crírtica")
