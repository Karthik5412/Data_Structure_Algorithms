def linear_search(arr,target,idx=0) :
    
    if idx == len(arr) :
        return -1
    
    if arr[idx] == target :
        return idx
    
    return linear_search(arr,target,idx+1)
    
    
def search(arr,target) :
    
    def ls(idx) :
        if idx >= len(arr) :
            return -1 
        
        if arr[idx] == target :
            return idx 
        
        
        return ls(idx+1)
    
    return ls(0)

n1 = [8,3,2,6,12,1] 

print(linear_search(n1,12))

res = search(n1,12)

print(res)



