class Queue :
    def __init__(self) :
        self.queue = []
    
    def enqueue(self, val) :
        self.queue.append(val)
    
    def dequeue(self) :
            self.queue.pop(0)
        
    def peak(self) :
        return self.queue[0]
    
    
que = Queue()


que.enque(10)
que.enque(20)
que.enque(30)
que.enque(40)
que.enque(50)
