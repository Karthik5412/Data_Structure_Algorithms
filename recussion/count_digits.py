def count_digits(n,count=0) :
    if n < 10 :
        return count+1 
    
    n //=10
    count += 1
    
    return count_digits(n,count)

print(count_digits(1234567890))