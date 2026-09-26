def n_sum(n) :
    if n == 0 :
        return 0
    
    return n + n_sum(n-1)

def n_pro(n) :
    if n == 1 :
        return 1
        
    return n * n_sum(n-1) 

print(n_sum(12))
print(n_pro(12))