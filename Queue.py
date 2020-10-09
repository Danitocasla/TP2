# DEFINICION DE LA CLASE QUEUE(COLA) JUNTO CON SUS FUNCIONALIDADES
class Queue():
    def __init__(self):
        self.cola = []

    def __repr__(self):
        return str(self.cola)

    def empty(self):
        self.cola.clear()

    def enqueue(self, element):
        self.cola.append(element)

    def dequeue(self):
        dato = None
        if not self.isEmpty():
            dato = self.cola.pop(0)
        return dato

    def top(self):
        return self.cola[0]

    def clone(self):
        colaNew = Queue()
        for element in self.cola:
            colaNew.enqueue(element)
        return colaNew

    def size(self):
        return len(self.cola)

    def isEmpty(self):
        return len(self.cola) == 0

    def index(self, elem):
        encontrado = False
        salida = 0
        for i in range(len(self.cola)):
            if self.cola[i] == elem and not encontrado:
                salida = i
                encontrado = True
        return salida

    def eliminar(self, indice):
        self.cola.pop(indice)
