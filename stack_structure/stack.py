class Stack :
    def __init__(self) :
        self.stack = []
        
    def push(self,ele) :
        self.stack.append(ele)
        print(f'{ele} is added to stack')
        
    
    def peak(self) :
        if not self.is_empty :
            print(f"peak element is {self.stack[-1]}")
        else :
            print('stack is empty')
    
    def is_empty(self) :
        return len(self.stack) == 0
    
stack = Stack()

stack.peak()
print(stack.is_empty())

stack.push(10)
stack.push(20)
stack.peak()

print(stack.is_empty())

stack.push(30)
stack.push(40)
stack.peak()

stack.push(50)

stack.peak()
