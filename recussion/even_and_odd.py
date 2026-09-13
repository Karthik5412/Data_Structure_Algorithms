def even_num(end,curr = 0,res=[]) :
    if curr > end :
        return res 
    
    res.append(curr)
    
    return even_num(end,curr + 2,res)


print(even_num(100))