def is_sorted(arr,n=None) :
    
    if n == None :
        n = len(arr) - 1
        
    
    if n == 1 :
        return True
    elif arr[n] < arr[n-1] :
            return False 
    
    return arr[n] >= arr[n-1] and is_sorted(arr,n-1)

print(is_sorted([1]))