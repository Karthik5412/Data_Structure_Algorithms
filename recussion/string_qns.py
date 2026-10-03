def eleminate_ele(s:str,ele:chr,idx=0) :
    
    if idx < len(s) :
        if s[idx] != ele :
            
            return s[idx] + eleminate_ele(s,ele,idx+1)
        else :
            return eleminate_ele(s,ele,idx+1)
        
    else :
        return ""
    
    
def eleminate_word(s:str,word:str,idx=0) :
    
    if idx < len(s) :
        if s[idx] == word[0] :
            count = 0
            for i in range(1,len(word)) :
                if s[idx + i] == word[i] :
                    count += 1
                else :
                    return s[idx:idx+count+1] + eleminate_word(s,word,idx+count+1)
                
            return ""+ eleminate_word(s,word,idx+count+1)
        else :
            return s[idx] + eleminate_word(s,word,idx+1)
        
    return ""



def eleminate_word_portion(s:str,word:str,idx=0) :
    
    if idx < len(s) :
        if s[idx] == word[0] :
            count = 0
            for i in range(1,len(word)) :
                if s[idx + i] == word[i] :
                    count += 1
                    
            if count > 2 :
                return ""+ eleminate_word(s,word,idx+count+1)
            else :
                return s[idx:idx+count+1] + eleminate_word(s,word,idx+count+1)
            
            
        else :
            return s[idx] + eleminate_word(s,word,idx+1)
        
    return ""


print(eleminate_ele('baccad','a'))
print(eleminate_ele('baccad','b'))
print(eleminate_ele('baccad','k'))

print(eleminate_word('baccapplegraped','grape'))

print(eleminate_word_portion('apple_mango1_grape','mango'))

