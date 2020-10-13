#LC179.Largest_Number_Bobble_Sort.py

##Topic: Sort

# Given a list of non negative integers, arrange them such 
# that they form the largest number.

# Example 1:

# Input: [10,2]
# Output: "210"

class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        str_nums = list(map(str, nums))
        for i in range(len(str_nums), 0, -1):
            for j in range(i-1):
                if str_nums[j] + str_nums[j+1] <= str_nums[j+1] + str_nums[j]:
                    str_nums[j], str_nums[j+1] = str_nums[j+1], str_nums[j]
        return str(int(''.join(str_nums)))
        
