def bubble(arr) :
    n = len(arr) 
    for i in range(n) :
        flag = True
        for j in range(n-i-1) :
            if arr[j] > arr[j+1] :
                arr[j], arr[j+1] = arr[j+1], arr[j]
                flag = False 
                
        if flag :
            break
                
    return arr
    
def selection(arr) :
    n = len(arr)
    for i in range(n) :
        flag = True
        idx = i 
        for j in range(i+1, n) :
            if arr[idx] > arr[j] :
                idx = j 
                flag = False 
                
        if flag or idx == i:
            continue
        arr[i], arr[idx] = arr[idx], arr[i]
        
    return arr 

def insretion(arr) :
    n = len(arr) 
    
    for i in range(1,n) :
        pick = arr[i]
        j = i-1 
        
        while j >= 0 and arr[j] > pick :
            arr[j+1] = arr[j]
            j -= 1
            
        arr[j+1] = pick 
        
    return arr 

def merge(arr) :
    if len(arr) <= 1 :
        return arr 
    
    mid = len(arr) // 2
    
    left = merge(arr[:mid])
    right = merge(arr[mid:])
    
    return algo(left,right)

def algo(left,right) :
    i = j = 0 
    res = []
    
    while i < len(left) and j < len(right) :
        if left[i] < right[j] :
            res.append(left[i])
            i += 1
            
        else :
            res.append(right[j])
            j += 1
    res.extend(left[i:])
    res.extend(right[j:])
    return res 
    
def quick(arr) :
    if len(arr) <= 1 :
        return arr 
    
    pivot = arr[-1]
    
    left = [x for x in arr[:-1] if x <= pivot]
    right = [x for x in arr[:-1] if x > pivot]
    
    return quick(left) + [pivot] + quick(right) 

a1 = [8,3,2,6,12,1] 
a2 = [8,3,2,6,12,1] 
a3 = [8,3,2,6,12,1] 
a4 = [8,3,2,6,12,1] 
a5 = [8,3,2,6,12,1] 

print(f'Bubble Sort    -->{bubble(a1)}')
print(f'Selection Sort -->{selection(a2)}')
print(f'Insertion Sort -->{insretion(a3)}')
print(f'Merge Sort     -->{merge(a4)}')
print(f'Quick Sort     -->{quick(a5)}')