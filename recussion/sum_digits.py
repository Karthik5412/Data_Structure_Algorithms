def sum_digits(n) :
    
    if n < 10 :
        return n
    
    rem = n % 10 
    
    return rem + sum_digits(n//10)

print(sum_digits(1))