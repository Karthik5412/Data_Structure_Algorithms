def search(arr,target,left=0,right = None) :
    if right == None :
        right = len(arr)-1
    
    if left <= right :
        mid = left + (right - left) // 2 
        
        if arr[mid] == target :
            return mid 
        
        if arr[left] <= arr[mid] :
            
            if (arr[left] <=  target) and (arr[mid] >= target ) :
            
                return search(arr,target,left,mid-1)
        
            else :
                return search(arr,target,mid+1,right)
        
        if (target >= arr[mid]) and (target <= arr[right]) :
                return search(arr,target,mid+1,right)
            
        else :
            return search(arr,target,left,mid-1) 
        
    return -1


arr = [4,5,6,7,1,2,3]


print(search(arr,3))