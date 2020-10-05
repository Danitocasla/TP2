from enum import Enum
import Zonas

# USO DE ENUM
class TipoAuxilio(int,Enum):
    Reparacion = 0
    Remolque = 1

class Estado(int,Enum):
    espera = 0
    aprobado = 1

class Estado(int,Enum):
    espera = 0
    aprobado = 1

# DEFINICION DE AUXILIOS
class Auxilio():
    def __init__(self, patente, zonaPartida, estado):
        self.patente = patente
        self.zonaPartida = zonaPartida
        self.estado = estado
    
    def enEspera(self):
        return self.estado == 0
    
    def zonaPartida(self):
        return self.zonaPartida

class Remolque(Auxilio):
    def __init__(self, patente, zonaPartida, zonaLlegada, estado):
        super().__init__(patente, zonaPartida, estado)
        self.zonaLlegada = zonaLlegada
        self.tipoAuxilio = TipoAuxilio(1)
    

class Reparacion(Auxilio):
    def __init__(self, patente, zonaPartida, estado):
        super().__init__(patente, zonaPartida, estado)
        self.zonaLlegada = zonaPartida
        self.tipoAuxilio = TipoAuxilio(0)

# ACCESORIOS A AUXILIOS
class Patente():
    def __init__(self, letras, numero):
        self.letras = letras
        self.numero = numero
    
    def getNumero(self):
        return self.numero
        
