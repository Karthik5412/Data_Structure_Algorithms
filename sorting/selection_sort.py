def selection_sort(arr : list[int]) -> list[int] :

    l = len(arr)

    for i in range(l-1) :
        min_idx = i
        is_sorting = False

        for j in range(i+1,l) :
            if arr[min_idx] > arr[j] :
                min_idx= j
                is_sorting = True

        if not is_sorting :
            break
        if min_idx != i :
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


nums = [8,3,2,9,6,12,1]

selection = selection_sort(nums)
bubble = bubble_sort(nums)
insertion = insertion_sort(nums)

print(f'bubble sort    --> {bubble}')
print(f'selection sort --> {selection}')
print(f'insertion sort --> {insertion}')

