class Node :
    def __init__(self, data):
        self.data = data 
        self.next = None 
        
class Linked_List :
    def __init__(self) :
        self.head = None 
        self.size = 0
    
    def insertion(self,data) :
        new_node = Node(data) 
        
        if not self.head :
            self.head = new_node 
            self.size += 1
            
        else :
            current = self.head 
            
            while current.next != None :
                current = current.next 
                
            current.next = new_node 
            self.size += 1
            
    def insert_at_front(self,data) :
        new_node = Node(data) 
        self.size += 1
        if not self.head :
            self.head = new_node
        else :
            new_node.next = self.head 
            
            self.head = new_node 
    
    def insert_at_middle(self,data) :
        new_node = Node(data)
        
        if not self.head :
            self.head =new_node
            self.size += 1
        else :
            current = self.head 
            place = self.size // 2
            
            while place > 0 :
                current = current.next 
                place -= 1
            
            new_node.next = current.next
            current.next = new_node 
            self.size += 1
    
    def display(self) :
        if not self.head :
            print('Noting')
            
        else :
            current = self.head 
            while current.next :
                print(f'{current.data} ->',end=' ')
                current = current.next 
            print(current.data)
        
l1 = Linked_List()

l1.display()
print(l1.size)
l1.insert_at_middle(10)
l1.insertion(20)
l1.insertion(30)
print(l1.size)
l1.insert_at_front(40)
l1.insertion(50)
l1.insertion(60)
l1.insertion(70)
l1.insert_at_middle(80)
l1.insert_at_middle(90)
l1.insert_at_middle(100)
print(l1.size)
l1.display()
        