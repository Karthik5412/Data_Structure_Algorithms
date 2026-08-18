def selection_sort(arr : list[int]) -> list[int] :

    l = len(arr)
    is_sorting = True
    for i in range(l-1) :
        min_idx = i
        

        for j in range(i+1,l) :
            if arr[min_idx] > arr[j] :
                min_idx= j
                is_sorting = False

        if is_sorting :
            break
        
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

    return arr

def bubble_sort(arr : list[int]) -> list[int] :

    for i in range(0,len(arr)) :
        flag = True
        for j in range(0,len(arr)-1-i) :
            if arr[j] > arr[j+1] :
                arr[j], arr[j+1] = arr[j+1], arr[j]
                flag = False

        if flag :
            break

    return arr

def insertion_sort(arr : list[int]) -> list[int] :
    l = len(arr)
    
    for i in range(1,l) :
        pick = arr[i]
        j = i-1
        
        while j >= 0 and arr[j] > pick :
            if arr[j] > arr[j+1] :
                arr[j+1],arr[j] = arr[j], arr[j+1]
                j -= 1
        arr[j+1] = pick 
        
        return arr

def merge_sort(arr : list[int]) -> list[int] :
    if len(arr) <= 1 :
        return arr 
    
    mid = len(arr) // 2 
    
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    
    merge(left,right)

def merge(left, right) :
    i = j = 0
    ans = []
    while i < len(left) and j < len(right):
        if left[i] < right[j] :
            ans.append(left[i])
            i+=1
        else :
            ans.append(right[j])
            j+= 1
            
    ans.extend(left[i:])
    ans.extend(right[j:])
    
    return ans 

n1 = [8,3,2,9,6,12,1]
n2 = [8,3,2,9,6,12,1]
n3 = [8,3,2,9,6,12,1]
n4 = [8,3,2,9,6,12,1]

selection = selection_sort(n1)
bubble = bubble_sort(n2)
insertion = insertion_sort(n3)

print(f'bubble sort    --> {bubble}')
print(f'selection sort --> {selection}')
print(f'insertion sort --> {insertion}')

