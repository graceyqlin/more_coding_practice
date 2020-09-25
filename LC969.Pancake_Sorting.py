class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        largest = len(arr)
        results = []
        
        while largest>0:
            large_index = arr.index(largest)
            k = large_index + 1
            results.append(k)
            
            arr[:large_index+1] = arr[:large_index+1][::-1]
            
            arr[:largest] = arr[:largest][::-1]            
            
            results.append(largest)
            
            largest -= 1
        
        
        return results
        