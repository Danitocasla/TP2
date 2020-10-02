
class Queue():
    """
    
    """
    def __init__(self):
        self.queue = []
    
    def __repr__(self):
        return str(self.queue)
    
    def empty(self):
        self.queue.clear()
        
    def enqueue(self, element):
        self.enqueue.append(element)
    
    def dequeue(self):
        date = None
        if not isEmpty():
            date = self.queue.pop(0)
        return date
    
    def top(self):
        date = None
        if not isEmpty():
            date = self.queue[0]
        return date
    
    def clone(self):
        queueNew = Queue()
        for element in self.queue:
            queueNew.enqueue(element)
        return queueNew
    
    def size(self):
        return len(self.queue)
    
    def isEmpty(self):
        return self.enqueue.size() == 0
