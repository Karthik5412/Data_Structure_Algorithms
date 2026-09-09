def composite_nums(limit : int) :
    nums = [True] * (limit+1)
    
    nums[0] = nums[1] = False 
    
    for n in range(2,limit+1) :
        if nums[n] == True :
            for i in range(n*n , limit+1, n) :
                nums[i] = False 
                
    return [i for i, val in enumerate(nums[2:], 2) if  not val] 


print(composite_nums(100)) 
