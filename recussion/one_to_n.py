def one_to_n(n,curr = 1,res= None) :
    if res is None :
        res = []
        curr = 1
    
    if n < curr :
        return res
    
    res.append(curr)
    
    
    return one_to_n(n,curr+1,res)


print(one_to_n(5))