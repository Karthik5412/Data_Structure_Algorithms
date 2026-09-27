from math import log10 

def rev_num(num,pow= None)  :
    if pow == None :
        pow = int(log10(num)) 
        
    if num < 10 : 
        return num
    
    return (num % 10)* 10**pow + rev_num(num // 10) 

# def rev_str(s,left = 0 , right = None) :
#     if right == None :
#         right = len(s) - 1
        
        
#     if left < right :
        
#         s[left],s[right] = s[right],s[left]
        
#         rev_str(s,left+1,right-1)
        
#     return ''.join(s)

# def pal(s,l=0, r= None) :
#     if r == None :
#         r = len(s)-1
    
#     if l < r :
        
#         if s[l] != s[r] :
#             return False 
#         else :
#             return pal(s,l+1,r-1)
        
#     return True
    
    

# print(rev_num(12345))

# print(rev_str(list('abc')))

# print(pal('cabac'))