
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
        dato = None
        if not self.isEmpty():
            dato = self.cola[0]
        return dato

    def clone(self):
        colaNew = Queue()
        for element in self.cola:
            colaNew.enqueue(element)
        return colaNew

    def size(self):
        return len(self.cola)

    def isEmpty(self):
        return self.cola.size() == 0
