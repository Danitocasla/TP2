import Queue


class OficinaAtencion():
    def __init__(self, interno):
        self.colaRemolque = Queue()
        self.colaReparacion = Queue()
        self.interno = interno
    
    def recibirAuxiolio(self, auxilio):
        pass
    
    def primerAuxilioAEnviar(self):
        pass
    
    def enviarAuxilio(self, zonaDeGrua):
        pass
    
    def auxiliosPorTipo(self):
        pass
    
    def cantidadTotalAuxilios(self):
        pass
    
    def esCritica(self):
        pass
    
    def auxiliosEnEspera(self):
        pass
    
    def buscarAuxilio(self, nroPatente):
        pass
    
    def eliminarAuxilio(self, nroPatente):
        pass
    
    def cambiaDeTipo(self, nroPatente):
        pass
    