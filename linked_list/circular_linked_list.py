class Node :
    def __init__(self, data):
        self.data = data 
        self.next = None 
        
class Circular_Linked_List :
    def __init__(self):
        self.head = None
        self.size = 0
        
    def insertion(self,data) :
            new_node = Node(data) 
            
            if not self.head :
                self.head = new_node 
                self.head.next = self.head 
                self.size += 1
                
            else :
                new_node.next = self.head 
                current = self.head 
                
                while current.next != self.head :
                    current = current.next 
                    
                current.next = new_node 
                
                self.size += 1
                
    def display(self) :
            if not self.head :
                print('Noting')
                
            else :
                current = self.head 
                while current.next != self.head :
                    print(f'{current.data} ->',end=' ')
                    current = current.next 
                print(current.data)
            
            
cl = Circular_Linked_List()

cl.insertion(10)
cl.insertion(20)
cl.insertion(30)
cl.insertion(40)

cl.display()