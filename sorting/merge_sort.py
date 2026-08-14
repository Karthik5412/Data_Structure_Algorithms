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
    
    
class selection_sort :
    def algo(self, arr : list[int]) -> list[int] :
        n = len(arr)
        
        for i in range(n) :
            min_idx = i 
            
            for j in range(i,n):
                if arr[min_idx] > arr[j] :
                    min_idx = i 
                    
            arr[i] = arr[min_idx]
            
        return arr

arr = [8,3,2,6,12,1]

a = bubble_sort()
b = selection_sort()

op1 = a.algo(arr)
op2 = b.algo(arr)

print(op1)
print(op2)