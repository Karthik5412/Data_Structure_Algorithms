def get_series(num : int) -> list :
    res =[0] * num 
    res[1] = 1
    
    for i in range(2,num) :
        
        res[i] = res[i-1] + res[i-2]
        
    return res 
        
        
print(get_series(10))


print(get_series(100))

print(get_series(120))