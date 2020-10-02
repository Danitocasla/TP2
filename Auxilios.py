

class Auxilio():
    def __init__(self, patente, zonaPartida, zonaLlegada, estado):
        self.patente = patente
        self.zonaPartida = zonaPartida
        self.zonaLlegada = zonaLlegada
        self.estado = estado
    

class Remolque(Auxilio):
    def __init__(self, patente, zonaPartida, zonaLlegada, estado):
        super().__init__(patente, zonaPartida, zonaLlegada, estado)
    

class Reparacion(Auxilio):
    def __init__(self, patente, zonaPartida, zonaLlegada, estado):
        super().__init__(patente, zonaPartida, zonaLlegada, estado)

