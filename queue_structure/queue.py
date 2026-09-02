class Queue :
    def __init__(self) :
        self.queue = []
    
    def enqueue(self, val) :
        self.queue.append(val)
    
    def dequeue(self) :
            self.queue.pop(0)
        
    def peak(self) :
        pass
    
    
que = Queue()