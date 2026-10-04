def subsets(p,up):
    if up == "" :
        return [p]
        
        return

    left = subsets(p+up[0],up[1:])
    right = subsets(p,up[1:])
    
    return left + right 
    


def sub_sets(arr) :
    res = []
    
    def backtrack(start,path) :
        res.append(path[:])
        
        for i in range(start,len(arr)) :
            path.append(arr[i])
            
            backtrack(i+1,path)
            path.pop()
            
            
    backtrack(0,[])
    return res 
        
        



print(subsets('','abc'))
print(sub_sets(['a','b','c']))