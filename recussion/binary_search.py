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

nums = [1,2,3,4,5,6,7]

op = binary_search(nums,4)

print(op)
    
    