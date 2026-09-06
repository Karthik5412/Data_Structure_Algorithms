class Deque :
    def __init__(self) :
        self.queue = []
    
    def enqueqe(self, val) :
        self.queue.append(val)
        
        print(f"{val} added to queue")
    
    def dequeqe(self) :
            val = self.queue.pop(0)
        
            print(f'{val} deleted from queue')
        
    def peak(self) :
        print(f'{self.queue[0]} is peak value')
    