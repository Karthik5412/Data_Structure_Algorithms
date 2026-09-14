def is_sorted_asc(arr,n=None) :
    
    if n == None :
        n = len(arr) 
        
    
    if n == 1 :
        return True
    elif arr[n-1] < arr[n-2] :
            return False 
    
    return arr[n-1] >= arr[n-2] and is_sorted_asc(arr,n-1)


def is_sorted_des(arr, n=None) :
    if n == None:
        n = len(arr)
        
    if n == 1 :
        return True 
    
    return arr[n-2] >= arr[n-1] and is_sorted_des(arr,n-1)

print(is_sorted_asc([2, 4, 6, 8]))
print(is_sorted_asc([2, 4, 6, 8][::-1]))
print(is_sorted_des([2, 4, 6, 8]))
print(is_sorted_des([2, 4, 6, 8][::-1]))