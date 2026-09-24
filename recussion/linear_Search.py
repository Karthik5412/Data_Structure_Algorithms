def linear_search(arr,target,idx=0) :
    
    if idx == len(arr) :
        return -1
    
    if arr[idx] == target :
        return idx
    
    return linear_search(arr,target,idx+1)
    

n1 = [8,3,2,6,12,1] 

print(linear_search(n1,8))



