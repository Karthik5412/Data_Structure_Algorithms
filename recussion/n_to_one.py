def n_to_one(n,res=[]) :
    if n < 1 :
        return res
    
    res.append(n)
    
    return n_to_one(n-1,res)


print(n_to_one(12))