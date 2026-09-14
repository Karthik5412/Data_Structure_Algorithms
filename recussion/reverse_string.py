def reverse_string(s,left=0,right=None) -> str:
    if right is None :
        right = len(s) - 1
        
    if left < right :
        s[left], s[right] = s[right],s[left] 
        
        reverse_string(s,left+1,right-1)
        
    
    return ''.join(s)
    
print(reverse_string(list('hello')))