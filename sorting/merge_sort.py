class merge_sort :
    pass

class bubble_sort :
    def algo(self, arr : list[int]) -> list[int] :
        n = len(arr)
        
        for i in range(n) :
            for j in range(n-1-i) :
                if arr[j] > arr[j+1] :
                    arr[j], arr[j+1] = arr[j+1], arr[j]
                    
        return arr 
        
arr = [8,3,2,6,12,1]

a = bubble_sort()

op = a.algo(arr)

print(op)