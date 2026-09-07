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
    
    def pushleft(self,val) :
        self.queue = [val] + self.queue
        
        print(f'{val} added to queue')
    
    
    def peak(self) :
        print(f'{self.queue[0]} is peak value')
        
        
    def display(self) :
        print(f'Queue -> {self.queue}')
        
        
    
    
q = Deque()

q.push(10) 
q.push(20) 
q.push(30) 

q.display()
q.peak()

print()

q.pushleft(40) 
q.pushleft(50) 
q.pushleft(60) 

q.display()
q.peak()

print()

q.pop()
q.peak()
q.display()

print()

q.popleft()
q.display()

q.peak()

q.display()
q.popleft()

q.peak()