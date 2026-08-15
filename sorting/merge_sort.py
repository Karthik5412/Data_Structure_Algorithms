class merge_sort :
    pass

class bubble_sort :
    def algo(self, arr : list[int]) -> list[int] :
        n = len(arr)
        for i in range(n) :
            flag = True
            for j in range(n-1-i) :
                if arr[j] > arr[j+1] :
                    arr[j], arr[j+1] = arr[j+1], arr[j]
                    flag = False
            if flag :
                break
                    
        return arr 
    
    
class selection_sort :
    def algo(self, arr : list[int]) -> list[int] :
        n = len(arr)
        
        for i in range(n) :
            min_idx = i 
            flag = True
            for j in range(i,n):
                if arr[min_idx] > arr[j] :
                    min_idx = i 
                    flag = False
                    
            if flag :
                break
            arr[i] = arr[min_idx]
            
        return arr


class insertion_sort :
    def algo(self, arr : list[int]) -> list[int]:
        n = len(arr)
        
        for i in range(1,n) :
            pick = arr[i]
            j = i-1

            while j >=0 and arr[j] > pick :
                arr[j+1] = arr[j]
                j-= 1
            arr[j+1] = pick
            
        return arr 

arr = [8,3,2,6,12,1]

bubble = bubble_sort()
selection = selection_sort()
insertion = insertion_sort()

op1 = bubble.algo(arr)
op2 = selection.algo(arr)
op3 = insertion.algo(arr)

print(op1)
print(op2)
print(op3)