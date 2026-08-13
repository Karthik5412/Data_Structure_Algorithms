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
        nums[i] = nums[idx]
        
    return nums

def insertion_sort(nums : list[int]) -> list[int]:
    
    l = len(nums)
    
    for i in range(1, l) :
        pick = nums[i]
        j = i-1
        
        while j>= 0 and nums[j] > pick :
            nums[j+1] = j
            j-=1
            
        nums[j+1] = pick 
        
    return nums

def main(): 
    nums = [8,3,2,6,12,1]
    bubble = bubble_sort(nums)
    selection = selection_sort(nums)
    insertion = insertion_sort(nums)
    print('bubble    -->',bubble)
    print('selection -->', selection) 
    print('insertion -->', insertion) 

if __name__ == '__main__' :
    main() 