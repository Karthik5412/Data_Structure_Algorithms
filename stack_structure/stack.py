class Stack :
    def __init__(self) :
        self.stack = []
        
    def push(self,ele) :
        self.stack.append(ele)
        print(f'{ele} is added to stack')
        
    
    
    
stack = Stack()