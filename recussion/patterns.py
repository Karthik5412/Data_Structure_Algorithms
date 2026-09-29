def pattern_1(row,col=0) :
    
    if row == 0 :
        return 
    
    if col < row :
        print('*',end=' ')
        return pattern_1(row,col+1)
    else :
        print()
        return pattern_1(row-1,0)

def pattern_2(row,col=0) :
    if row == 0 :
        return 
    
    if col < row :
        pattern_2(row,col+1)
        print('*',end=' ')
    else :
        pattern_2(row-1,0)
        print()
    

pattern_1(5)
pattern_2(5)
pattern_2(5)
pattern_1(5)