def merge_sort(arr) :
    
    if len(arr) == 1 :
        return arr 
    
    mid = len(arr) // 2
    
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    
    return merge(left,right)

def merge(left,right) :
    i = j = 0
    res = []
    
    while i < len(left) and j < len(right) :
        if left[i] < right[j] :
            res.append(left[i])
            i += 1
            
        else :
            res.append(right[j])
            j += 1
            
    if i != len(left) :
        res.extend(left[i:])
        
    if j != len(right) :
        res.extend(right[j:])
        
    return res 

    

def quick_sort(arr) :
    if len(arr) < 2 :
        return arr 
    
    pivot = arr[-1] 
    
    left = []
    right = []
    
    for i in arr[:-1] :
        if i <= pivot :
            left.append(i)
        else :
            right.append(i)
            
    return merge_sort(left) + [pivot] + merge_sort(right)


arr1 = [4,2,3,5,1]

print(merge_sort(arr1))