def next_great_num(arr) :
    stack = []
    res = [-1] * len(arr)
    for idx , num in enumerate(arr[::-1]) :
        while  stack and stack[-1] <= num :
            stack.pop()
        if stack :
            res[idx] = stack[-1]
        
        stack.append(num)
        
    return res[::-1]

arr = [4, 5, 2, 25, 7, 8, 1, 20, 11, 3, 12, 6]

print(next_great_num(arr))

print([5, 25, 25, -1, 8, 20, 20, -1, 12, 12, -1, -1])