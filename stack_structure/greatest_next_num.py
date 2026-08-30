def next_great_num(arr) :
    stack = []
    res = [-1] * len(arr)
    for idx , num in enumerate(arr) :
        while  stack and stack[-1] <= num :
            stack.pop()
        
        res[idx] = num
        
        stack.append(num)