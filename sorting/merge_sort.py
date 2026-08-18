class merge_sort :
    def merge(self,left,right) :
        sorted_arr = []
        i = j = 0
        while i<len(left) and j < len(right) :
            if left[i] < right[j] :
                sorted_arr.append(left[i])
                i+= 1
            else :
                sorted_arr.append(right[j])
                j+= 1
                
        sorted_arr.extend(left[i:])
        sorted_arr.extend(right[j:])
        
        return sorted_arr
    
    def algo(self,arr) :
        if len(arr) <= 1 :
            return arr 
        
        mid = len(arr)//2 
        
        left = self.algo(arr[:mid])
        right = self.algo(arr[mid:])
        
        return self.merge(left,right)

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

a1 = [8,3,2,6,12,1]
a2 = [8,3,2,6,12,1]
a3 = [8,3,2,6,12,1]
a4 = [8,3,2,6,12,1]

bubble = bubble_sort()
selection = selection_sort()
insertion = insertion_sort()
merge = merge_sort()

op1 = bubble.algo(a1)
op2 = selection.algo(a2)
op3 = insertion.algo(a3)
op4 = merge.algo(a4) 

print(op1)
print(op2)
print(op3)
print(op4)