class Node :
    def __init__(self, val):
        self.val = val 
        self.prev = None 
        self.next = None 

class DoubleLinkedList :
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0
        
    def insertion(self,val) :
        new_node = Node(val)
        
        if not self.head :
            self.head = new_node
            self.tail = new_node
            self.size += 1
        else :
            curr = self.head 
            
            while curr.next != None:
                curr = curr.next 
                
            curr.next = new_node
            new_node.prev = curr
            self.tail = new_node
            self.size += 1
    
    def insert_at_front(self,val)  :
        new_node = Node(val)
        
        if not self.head :
            self.head = self.tail = new_node 
        else :
            new_node.next = self.head 
            self.head = new_node
            
        self.size += 1
    
    def insert_at_middle(self,val) :
        pass
    
    def display(self,reverse = False) :
        
        if not self.head :
            print('Empty')
            return
        
        if reverse :
            curr = self.tail 
            
            while curr.prev :
                print(f'{curr.val} <=>', end=' ')
                curr = curr.prev
            print(curr.val)
            
            
        else :
            curr = self.head 
            
            while curr.next :
                print(f'{curr.val} <=>', end=' ')
                curr = curr.next
            print(curr.val)




dl = DoubleLinkedList()


dl.insert_at_front(100)
print(dl.tail.val)
print(dl.head.val)

dl.insertion(10)
dl.insertion(20)
dl.insertion(30)
dl.insertion(40)
print(dl.tail.val)

dl.display(reverse=True)