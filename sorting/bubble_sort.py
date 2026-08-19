def bubble_sort(nums : list[int]) -> list[int]:
    n = len(nums)
    
    for i in range(n):
        flag = False
        for j in range(0,n-1-i) :
            if nums[j] > nums[j+1] :
                nums[j], nums[j+1] = nums[j+1], nums[j]
                flag = True
                
        if not flag :
            break
                
    return nums

def selection_sort(nums : list[int]) -> list[int]:
    n = len(nums) 
    is_sorted = True 
    for i in range(n) :
        idx = i 
        
        for j in range(i+1, n) :
            if nums[idx] > nums[j] :
                idx= j
                is_sorted = False
                
        if is_sorted :
            break
        nums[i],nums[idx] = nums[idx],nums[i]
        
    return nums

def insertion_sort(nums : list[int]) -> list[int]:
    
    l = len(nums)
    
    for i in range(1, l) :
        pick = nums[i]
        j = i-1
        
        while j>= 0 and nums[j] > pick :
            nums[j+1] = nums[j]
            j-=1
            
        nums[j+1] = pick 
        
    return nums

def merge_sort(nums : list[int]) -> list[int] :
    if len(nums) <= 1 :
        return nums 
    
    mid = len(nums)//2
    
    left = merge_sort(nums[:mid])
    right = merge_sort(nums[mid:])
    
    return merge(left,right)

def merge(left,right) :
    arr = []
    i = j = 0
    
    while i < len(left) and j < len(right) :
        if left[i] < right[j] :
            arr.append(left[i])
            i+= 1
        else :
            arr.append(right[j])
            j+= 1
            
    arr.extend(left[i:])
    arr.extend(right[j:])
    
    return arr 

def quick_sort(arr: list[int]) :
    if len(arr) <= 1 :
        return arr 
    
    pivot = arr[-1]
    
    left = [x for x in arr[:-1] if x <= pivot]
    right = [x for x in arr[:-1] if x > pivot] 
    
    return quick_sort(left) + [pivot] + quick_sort(right)

def main(): 
    n1 = [8,3,2,6,12,1]
    n2 = [8,3,2,6,12,1]
    n3 = [8,3,2,6,12,1]
    n4 = [8,3,2,6,12,1]
    n5 = [8,3,2,6,12,1]
    bubble = bubble_sort(n1)
    selection = selection_sort(n2)
    insertion = insertion_sort(n3)
    m1 = merge_sort(n4)
    quick = quick_sort(n5)
    print('bubble    -->',bubble)
    print('selection -->', selection) 
    print('insertion -->', insertion) 
    print('merge     -->', m1) 
    print('quick     -->', quick) 

if __name__ == '__main__' :
    main() 