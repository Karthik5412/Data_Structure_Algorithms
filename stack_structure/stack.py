class Stack :
    def __init__(self) :
        self.stack = []
        
    def push(self,ele) :
        self.stack.append(ele)
        print(f'{ele} is added to stack')
        
    
    
    
stack = Stack()

stack.push(10)
stack.push(20)
stack.push(30)
stack.push(40)
stack.push(50)

