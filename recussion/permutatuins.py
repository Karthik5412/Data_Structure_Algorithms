def permutatoins(arr : list) -> list :
    res = []
    
    def backtrack(arr,idx) :
        if idx == len(arr) :
            res.append(arr[:])
            
            return 
        
        for j in range(idx,len(arr)) :
            arr[idx] , arr[j] = arr[j], arr[idx]
            
            backtrack(arr,idx+1)
            
            arr[idx] , arr[j] = arr[j], arr[idx]
        
        
    backtrack(arr,0)
    
    return res 

op = permutatoins([1,2,3])

print(op)