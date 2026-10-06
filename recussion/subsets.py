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
        
        
def sub_set_mul(arr) :
    op = []
    
    def healper(n,res) :
        if n == [] :
            op.append(res)
            
        idx = 1 
        while idx < len(n) and n[idx] == n[idx-1] :
            idx += 1
            
        sub_set_mul(n[idx:], res+[n[0]]) 
        sub_set_mul(n[idx:],res)
    
    healper(arr,[])
    
    return op

def sub_itr(arr):
    op = [[]]
    
    for i in arr :
        n = len(op) 
        
        for j in range(n) :
            
            op.append(op[j] + [i])
            
    return op 
            

print(subsets('','abc'))
print(sub_sets(['a','b','c']))

print(sub_itr([1,2,3]))


