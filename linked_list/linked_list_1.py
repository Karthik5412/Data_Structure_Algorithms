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
    
    def insert_at_index(self,data,idx) :
        new_node = Node(data )
        
        
        if idx == 0 or not self.head :
            new_node.next = self.head 
            self.head = new_node
            self.size += 1
        else :
            prev = self.head 
            current = self.head.next 
            
            if idx > self.size :
                self.insertion(data) 
                return 
            pointer = idx-1
            
            while current :
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
        elif not self.head.next :
            self.head = None 
            self.size -= 1
            
        else :
            current = self.head 
            
            while current.next.next :
                current = current.next 
                
            current.next = None 
            self.size -= 1
    
    def delete_head_node(self) :
        if not self.head :
            print("No Head Node")
        else :
            self.head = self.head.next 
            self.size -= 1
    
    def delete_this_node(self,data) :
        if not self.head :
            print('This is an empty list')
        else :
            if self.head.data == data :
                self.head = self.head.next 
                self.size -= 1 
                
            else :
                prev = self.head 
                current = self.head.next
                while current.next :
                    if current.data == data :
                        prev.next = current.next 
                        self.size -= 1
                        break 
                    else :
                        prev = prev.next
                        current = current.next 
    
    def reverse_the_list(self) :
        if not self.head or not self.head.next :
            if self.head :
                print(self.head.data ) 
            else :
                print("None")
        else :
            curr = self.head 
            prev = None 
            
            while curr :
                next_node = curr.next 
                curr.next = prev 
                prev = curr 
                curr = next_node 
            
            self.head = prev
            
            self.display()
    
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
l1.reverse_the_list()
l1.display()
print(l1.size)
l1.delete_node()
l1.insert_at_middle(10)
l1.reverse_the_list()
l1.insertion(20)
l1.delete_node()
l1.insertion(30)
print(l1.size)
l1.display()
l1.insert_at_front(40)
l1.display()
l1.delete_node()
l1.insertion(50)
l1.insertion(60)
l1.insertion(70)
l1.insert_at_middle(80)
l1.insert_at_middle(90)
l1.insert_at_middle(100)
l1.delete_node()
print(l1.size)
l1.display()
l1.delete_head_node()
l1.delete_head_node()
print(l1.size)
l1.display()
l1.delete_this_node(100) 
l1.display()
print(l1.size)
l1.delete_this_node(80)
l1.display()
print(l1.size)
l1.insert_at_index(120,100)
l1.display()
print(l1.size)
l1.insert_at_index(100,2)
l1.display()
print(l1.size)
l1.insert_at_index(10,0)
l1.display()
print(l1.size)
l1.reverse_the_list()
l1.display()
