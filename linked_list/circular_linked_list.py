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
            
    def insert_at_front(self,data) :
            new_node = Node(data) 
            self.size += 1
            if not self.head :
                self.head = new_node
                self.head.next = self.head 
            else :
                new_node.next = self.head 
                
                curr = self.head 
                
                while curr.next != self.head  :
                    curr = curr.next 
                
                curr.next = new_node 
                self.head = new_node 
    
    def insert_at_middle(self,data) :
            new_node = Node(data)
            
            if not self.head :
                self.head =new_node
                self.head.next = self.head
                self.size += 1
            else :
                current = self.head 
                place = (self.size // 2) -1
                
                while place > 0 :
                    current = current.next 
                    place -= 1
                
                new_node.next = current.next
                current.next = new_node 
                self.size += 1
    
    def insert_at_index(self,data,idx) :
            new_node = Node(data )
            
            
            if idx == 0 or not self.head :
                new_node.next = self.head 
                
                curr = self.head 
                while curr.next != self.head :
                    curr = curr.next
                
                self.head = new_node
                curr.next = self.head
                
                self.size += 1
            else :
                prev = self.head 
                current = self.head.next 
                
                if idx >= self.size :
                    self.insertion(data) 
                    return 
                pointer = idx-1
                
                while current.next != self.head  :
                    if pointer == 0 :
                        prev.next = new_node
                        new_node.next = current
                        break 
                    prev = prev.next 
                    current = current.next 
                    pointer -= 1
                
                self.size += 1
    
    def delete_node(self) :
            if not self.head :
                print('Linked List is empty')
            elif self.head.next == self.head :
                self.head = None 
                self.size -= 1
                
            else :
                current = self.head 
                
                while current.next.next != self.head:
                    current = current.next 
                    
                current.next = self.head 
                self.size -= 1
    
    def delete_head_node(self) :
            if not self.head :
                print("No Head Node")
            else :
                curr = self.head 
                while curr.next != self.head :
                    curr = curr.next 
                    
                curr.next = self.head.next 
                self.head = self.head.next 
                self.size -= 1
    
    def display(self) :
            if not self.head :
                print('Noting')
                
            else :
                current = self.head 
                while current.next != self.head :
                    print(f'{current.data} ->',end=' ')
                    current = current.next 
                print(current.data,' <->', end=' ')
                print(current.next.data)
            
            
cl = Circular_Linked_List()

cl.delete_node()
cl.insertion(10)
cl.delete_node()

cl.display()

cl.insertion(20)
cl.insertion(30)
cl.insertion(40)

cl.insert_at_front(120)

cl.insertion(50)
cl.insertion(60)
cl.insertion(70)
cl.insert_at_front(80)

cl.insert_at_middle(500)
cl.insert_at_middle(250)

cl.insert_at_index(300,5)
cl.insert_at_index(300,25)

cl.delete_node()
cl.delete_node()

cl.display()

cl.delete_head_node()

cl.display()
print(cl.size)