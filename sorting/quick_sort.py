def bubble(arr) :
    n = len(arr) 
    
    for i in range(n) :
        for j in range(n-i-1) :
            if arr[j] > arr[j+1] :
                arr[j], arr[j+1] = arr[j+1], arr[j]
                
    return arr
    
def selection() :
    pass

def insretion() :
    pass 

def merge() :
    pass 

arr = [8,3,2,6,12,1] 

print(bubble(arr))