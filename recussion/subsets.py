def subsets(p,up):
    if up == "" :
        return [p]
        
        return

    left = subsets(p+up[0],up[1:])
    right = subsets(p,up[1:])
    
    return left + right 
    




print(subsets('','abc'))