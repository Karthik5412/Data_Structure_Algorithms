class Sorting_algos :
    def insertion_sort(self,arr : list[int]) -> list[int] :
        
        n = len(arr) 
        
        for i in range(1,n) :
            
            pick = arr[i]
            j = i-1
            
            while j >= 0 and arr[j] > pick :
                
                arr[j+1] = arr[j]
                j -= 1
                
            arr[j+1] = pick
            
        return arr
    
    def bubble_sort(self, arr:list[int]) -> list[int] :
        l = len(arr)
        
        for i in range(l) :
            flag = True
            for j in range(l-1-i) :
                if arr[j] > arr[j+1] :
                    arr[j+1] , arr[j] = arr[j], arr[j+1]
                    flag = False
            if flag :
                break 
        return arr
        
    def selection_sort(self, arr : list[int]) -> list[int] :
        l = len(arr) 
        flag = True
        for i in range(l) :
            
            min_idx = i
            for j in range(i+1,l) :
                if arr[j] < arr[min_idx] :
                    min_idx = j 
                    flag = False 
            if flag :
                break 
            arr[i],arr[min_idx] = arr[min_idx], arr[i]
            
        return arr

    def merge_sort(self, arr: list[int]) -> list[int] :
        
        if len(arr) <= 1 :
            return arr 
        
        mid = len(arr) // 2
        
        left = self.merge_sort(arr[:mid])
        right = self.merge_sort(arr[mid:])
        
        return self.merge(left,right)
    
    def merge(self, left : list[int], right : list[int]) ->  list[int] :
        i=j=0 
        res = [] 
        
        while i < len(left) and j < len(right) :
            if left[i] < right[j] :
                res.append(left[i])
                i+= 1
            else :
                res.append(right[j])
                j+= 1
                
        res.extend(left[i:])
        res.extend(right[j:])
        
        return res 
        
        
        
n1 = [8,3,2,6,12,1]
n2 = [8,3,2,6,12,1]
n3 = [8,3,2,6,12,1]
n4 = [8,3,2,6,12,1]
s = Sorting_algos()

print(s.insertion_sort(n1))
print(s.bubble_sort(n2))
print(s.selection_sort(n3))
print(s.merge_sort(n4))