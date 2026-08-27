class Node :
    def __init__(self, val):
        self.val = val 
        self.prev = None 
        self.next = None 

class DoubleLinkedList :
    def __init__(self):
        self.head = None
        self.size 
        
    def insertion(self,val) :
        new_node = Node(val)
        
        if not self.head :
            self.head = new_node
            self.size += 1
        else :
            curr = self.head 
            
            while curr :
                curr = curr.next 
                
            curr.next = new_node
            new_node.prev = curr
            self.size += 1
            