class Queue :
    def __init__(self) :
        self.queue = []
    
    def enque(self, val) :
        self.queue.append(val)
        
        print(f"{val} added to queue")
    
    def deque(self) :
            val = self.queue.pop(0)
        
            print(f'{val} deleted from queue')
        
    def peak(self) :
        print(f'{self.queue[0]} is peak value')
    