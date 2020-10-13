
#LC969.Pancake_Sorting.py
# Given an array of integers arr, sort the array by performing a series 
# f pancake flips.

# In one pancake flip we do the following steps:

# Choose an integer k where 1 <= k <= arr.length.
# Reverse the sub-array arr[1...k].
# For example, if arr = [3,2,1,4] and we performed a pancake flip 
# choosing k = 3, we reverse the sub-array [3,2,1], so arr = [1,2,3,4] 
# after the pancake flip at k = 3.

# Return the k-values corresponding to a sequence of pancake flips that 
# ort arr. Any valid answer that sorts the array within 10 * arr.length
# flips will be judged as correct.


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
        