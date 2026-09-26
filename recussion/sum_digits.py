def sum_digits(n) :
    
    if n < 10 :
        return n
    
    rem = n % 10 
    
    return rem + sum_digits(n//10)

def pro_digits(n) :
    if n < 10 :
        return n 
    
    return n % 10 * pro_digits(n//10)

print(sum_digits(10))
print(pro_digits(1120))