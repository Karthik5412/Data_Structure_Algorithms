def bubble_sort(arr,idx=0,n=1) :
    
    if idx >= len(arr) :
        return arr 
    
    if n < len(arr):
        if arr[idx] > arr[n] :
            arr[idx],arr[n] = arr[n], arr[idx]
            
        return bubble_sort(arr,idx,n+1)
    else :
        return bubble_sort(arr,idx+1,idx+1)
    
    
op = bubble_sort([4,3,2,100,1,6,7])

print(op)