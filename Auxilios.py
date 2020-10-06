# DEFINICION DE AUXILIOS
class Auxilio():
    def __init__(self, patente, zonaPartida, zonaDestino, tipo, estado):
        self.patente = patente
        self.zonaPartida = zonaPartida
        self.zonaDestino = zonaDestino
        self.tipo = tipo
        self.estado = estado
    
    def tipo(self):
        return self.tipo
    
    def enEspera(self):
        return self.estado == 0
    
    def zonaPartida(self):
        return self.zonaPartida

# VER SI ESTO SIRVE
#class Patente():
#    def __init__(self, letras, numero):
#        self.letras = letras
#        self.numero = numero
#    
#    def getNumero(self):
#        return self.numero
        
