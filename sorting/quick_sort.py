def bubble(arr) :
    n = len(arr) 
    for i in range(n) :
        flag = True
        for j in range(n-i-1) :
            if arr[j] > arr[j+1] :
                arr[j], arr[j+1] = arr[j+1], arr[j]
                flag = False 
                
        if flag :
            break
                
    return arr
    
def selection(arr) :
    n = len(arr)
    for i in range(n) :
        flag = True
        idx = i 
        for j in range(i+1, n) :
            if arr[idx] > arr[j] :
                idx = j 
                flag = False 
                
        if flag or idx == i:
            continue
        arr[i], arr[idx] = arr[idx], arr[i]
        
    return arr 

def insretion(arr) :
    n = len(arr) 
    
    for i in range(1,n) :
        pick = arr[i]
        j = i-1 
        
        while j >= 0 and arr[j] > pick :
            arr[j+1] = arr[j]
            j -= 1
            
        arr[j+1] = pick 
        
    return arr 

def merge() :
    pass 

arr = [8,3,2,6,12,1] 

print(arr)
print(insretion(arr))