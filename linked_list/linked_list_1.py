class Node :
    def __init__(self, data):
        self.data = data 
        self.next = None 
        
class Linked_List :
    def __init__(self) :
        self.head = None 
    
    def insertion(self,data) :
        new_node = Node(data) 
        
        if not self.head :
            self.head = new_node 
            
        else :
            current = self.head 
            
            while current.next != None :
                current = current.next 
                
            current.next = new_node 
            
    def display(self) :
        if not self.head :
            print('Noting')
            
        else :
            current = self.head 
            while current.next :
                print(f'{current.data}->',end='')
                current = current.next 
            print(current.data)
        
l1 = Linked_List()

l1.display()
l1.insertion(10)
l1.insertion(20)
l1.insertion(30)
l1.display()
        