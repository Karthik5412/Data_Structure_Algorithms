def binary_search(arr,target) :
    
    def search(left,right) :
        
        if left > right :
            return -1
        
        mid = left + (right - left) // 2 
        
        if arr[mid] == target :
            return mid 
        elif arr[mid] > target :
            return search(left,mid-1)
        else :
            return search(mid+1,right)
        
    return search(0,len(arr)-1)
    
    