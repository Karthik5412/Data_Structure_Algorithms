def square_root(num) :
    low = 1
    high = num // 2 
    ans = 0
    
    while low <= high :
        mid = (low + high) // 2
        sqr = mid * mid
        
        if num == sqr :
            return mid
        elif sqr < num :
            ans = mid 
            low = mid + 1
        else :
            high = mid -1
            
        return ans

print(square_root(144))