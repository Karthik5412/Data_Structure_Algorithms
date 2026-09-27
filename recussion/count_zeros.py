def count_zeros(n,count = 0) :
    if n < 10  :
        return count if n != 0 else count +1
    
    if n % 10 == 0 :
        count += 1
        
    return count_zeros(n // 10 , count)


# print(count_zeros(120320520))