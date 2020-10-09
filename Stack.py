
class Stack():
    def __init__(self):
        self.pila = []

    def __repr__(self):
        return str(self.pila)

    def empty(self):
        self.pila.clear()

    def clone(self):
        pilaNew = Stack()
        for element in self.pila:
            pilaNew.push(element)
        return pilaNew

    def size(self):
        return len(self.pila)

    def isEmpty(self):
        return self.pila.size() == 0

    def push(self, element):
        self.pila.append(element)

    def top(self):
        dato = None
        if not self.isEmpty():
            dato = self.pila[(len(self.pila)-1)]
        return dato

    def pop(self):
        dato = None
        if not self.pila.isEmpty():
            dato = self.pila.pop()
        return dato
