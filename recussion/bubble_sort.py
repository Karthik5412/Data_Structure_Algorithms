def bubble_sort(arr,idx=0,n=1) :
    
    if idx >= len(arr) :
        return arr 
    
    if n < len(arr):
        if arr[idx] > arr[n] :
            arr[idx],arr[n] = arr[n], arr[idx]
            
        return bubble_sort(arr,idx,n+1)
    else :
        return bubble_sort(arr,idx+1,idx+1)
    
    
    
def sort2(arr, i= None,j= 0) :
    if i is None :
        i = len(arr)-1
    
    if i == 0 :
        return arr 
    
    if j < i :
        
        if arr[j] > arr[j+1] :
            arr[j], arr[j+1] = arr[j+1], arr[j]
            
        return sort2(arr,i,j+1)
    else :
        return sort2(arr,i-1,j=0)


op = bubble_sort([4,3,2,100,1,6,7])

res = sort2([4,3,2,100,1,6,7])

print(op)
print(res)