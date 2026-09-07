class Deque :
    def __init__(self) :
        self.queue = []
    
    def push(self, val) :
        self.queue.append(val)
        
        print(f"{val} added to queue")
    
    def popleft(self) :
            val = self.queue.pop(0)
        
            print(f'{val} deleted from queue')
    
    def pop(self) :
        print(f'{self.queue.pop()} deleted from queue')
    
    def pushleft(self) :
        pass 
    
    
    def peak(self) :
        print(f'{self.queue[0]} is peak value')
    