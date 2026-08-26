class Stack :
    def __init__(self) :
        self.stack = []
        
    def push(self,ele) :
        self.stack.append(ele)
        print(f'{ele} is added to stack')
        
    
    def peak(self) :
        if self.stack :
            print(f"peak element is {self.stack[-1]}")
        else :
            print('stack is empty')
    
    
stack = Stack()

stack.peak()

stack.push(10)
stack.push(20)
stack.peak()

stack.push(30)
stack.push(40)
stack.peak()

stack.push(50)

stack.peak()
