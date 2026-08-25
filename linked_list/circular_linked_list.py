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
    
    def delete_index(self,idx : int) :
        if idx == 0 :
            self.delete_head_node()
            return 
        
        if idx >= self.size :
            return 
        
        curr = self.head 
        for _ in range(idx-1) :
            curr = curr.next 
            
        curr.next = curr.next.next
    
    def delete_this_node(self,data) :
            if not self.head :
                print('This is an empty list')
            else :
                if self.head.data == data :
                    curr = self.head 
                    
                    while curr.next != self.head :
                        curr = curr.next 
                        
                    curr.next = self.head.next
                    
                    self.head = self.head.next 
                    self.size -= 1 
                    
                else :
                    prev = self.head 
                    current = self.head.next
                    while current.next != self.head :
                        if current.data == data :
                            prev.next = current.next 
                            self.size -= 1
                            break 
                        else :
                            prev = prev.next
                            current = current.next 
    
    def reverse_the_list(self) :
            if not self.head or self.head.next  == self.head:
                if self.head :
                    print(self.head.data ) 
                else :
                    print("None")
            else :
                curr = self.head 
                prev = None 
                
                while curr.next != self.head :
                    next_node = curr.next 
                    curr.next = prev 
                    prev = curr 
                    curr = next_node 
                
                curr.next = prev
                self.head.next = curr
                self.head = curr
                
                self.display()
    
    def search(self, data) :
            
            curr = self.head 
            count = 0
            
            while curr.next != self.head :
                if curr.data == data :
                    print(f'Value found in the index of {count}')
                    return 
                else :
                    curr = curr.next 
                    count += 1
            else :
                print(f'Unknown Value')
                return 
    
    def sort_the_list(self) :
            if not self.head or self.head.next == self.head :
                return 
            
            arr = []
            curr = self.head 
            while curr.next != self.head:
                arr.append(curr.data) 
                curr = curr.next 
            op = self.quick(arr)
            
            head = Node(op[0])
            curr = head 
            
            for i in op[1:] :
                curr.next = Node(i)
                curr = curr.next
            self.head = head 
            curr.next = self.head
    
    def quick(self, arr) :
            if len(arr) <= 1 :
                return arr 
            
            pivot = arr[-1]
            left = [x for x in arr[:-1] if x <= pivot]
            right = [x for x in arr[:-1] if x > pivot] 
            
            return self.quick(left) + [pivot] + self.quick(right)
    
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

cl.reverse_the_list()

cl.insertion(10)

cl.reverse_the_list()

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

cl.search(500)
cl.display()

cl.insert_at_index(300,5)
cl.insert_at_index(300,25)

cl.delete_node()
cl.delete_node()

cl.display()

cl.delete_this_node(500)

cl.display()

cl.reverse_the_list()

cl.sort_the_list()

cl.display()
print(cl.size)


c2 = Circular_Linked_List()

c2.insertion(100)
c2.insertion(30)
c2.insertion(40)
c2.insertion(50)
c2.insertion(20)

print('-'*80)

c2.display()
c2.delete_index(16)
c2.display()