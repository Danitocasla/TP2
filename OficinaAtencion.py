import Queue
import Auxilios


class OficinaAtencion():
    def __init__(self, interno):
        self.colaRemolque = Queue()
        self.colaReparacion = Queue()
        self.interno = validar(interno)
    
    def validar(self, interno):
        salida = None
        if 0 < interno < 1000:
            salida = interno
        else:
            salida = "Numero fuera de rango, por favor ingrese un número del 1 al 999"
        return salida
    
    def getInterno(self):
        return self.interno
    
    def recibirAuxiolio(self, auxilio):
        if auxilio.tipoAuxilio == 1:
            situacionCritica()
            self.colaRemolque.enqueue(auxilio)
        else:
            situacionCritica()
            self.colaReparacion.enqueue(auxilio)
    
    def primerAuxilioAEnviar(self):
        salida = None
        if self.colaRemolque.size() > 0:
            salida = self.colaRemolque.top()
        else:
            salida = self.colaReparacion.top()
        return salida
    
    def enviarAuxilio(self, zonaDeGrua):
        pass
    
    def auxiliosPorTipo(self):
        # Ver el orden que se espera y si es lo esperado
        return self.colaRemolque.size(), self.colaReparacion.size()
    
    def cantidadTotalAuxilios(self):
        return self.colaRemolque.size() + self.colaReparacion.size()
    
    def esCritica(self):
        remolques  = self.colaRemolque.size()
        reparacion = self.colaReparacion.size()
        return remolques > 50 or reparacion > 50
    
    def auxiliosEnEspera(self):
        return self.contarEnEspera(self.colaRemolque) + self.contarEnEspera(self.colaReparacion)
    
    def buscarAuxilio(self, nroPatente):
        pass
    
    def eliminarAuxilio(self, nroPatente):
        pass
    
    def cambiaDeTipo(self, nroPatente):
        pass
    
    def situacionCritica(self):
        if self.esCritica():
            return "Situacion Crírtica"
        else: 
            pass 
    
    def contarEnEspera(self,cola):
        clon = cola.clone()
        count = 0
        for i in range(len(clon)):
            aux = clon.dequeue()
            if aux.enEspera():
                count += 1
        return count
    