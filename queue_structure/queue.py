class Queue :
    def __init__(self) :
        self.queue = []
    
    def enque(self, val) :
        self.queue.append(val)
    
    def deque(self) :
            self.queue.pop(0)
        
    def peak(self) :
        print(self.queue[0])
    
    
que = Queue()


que.enque(10)
que.peak()

que.enque(20)
que.peak()

que.enque(30)
que.enque(40)
que.peak()

que.enque(50)



que.deque()
que.peak()