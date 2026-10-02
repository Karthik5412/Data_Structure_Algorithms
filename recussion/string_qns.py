def eleminate_ele(s:str,ele:chr,idx=0) :
    
    if idx < len(s) :
        if s[idx] != ele :
            
            return s[idx] + eleminate_ele(s,ele,idx+1)
        else :
            return eleminate_ele(s,ele,idx+1)
        
    else :
        return ""
    
    
print(eleminate_ele('baccad','a'))