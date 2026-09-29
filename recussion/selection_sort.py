def sel1(arr,i=None,j=1,idx=0) :
    
    if i is None :
        i = len(arr)-1
    
    if i == 0 :
        return arr 
    
    if j <= i :
        
        if arr[idx] < arr[j] :
            idx = j
        
        
        return sel1(arr,i,j+1,idx) 
        
    else :
        arr[i],arr[idx] = arr[idx], arr[i]
        
        return sel1(arr,i-1,0,0)
        
        
print(sel1([4,3,2,1,5,6]))
    