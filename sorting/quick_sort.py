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

def insretion() :
    pass 

def merge() :
    pass 

arr = [8,3,2,6,12,1] 

print(arr)
print(selection(arr))