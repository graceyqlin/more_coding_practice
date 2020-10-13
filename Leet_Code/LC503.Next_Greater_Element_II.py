# LC503.Next_Greater_Element_II.py
# Topics: Stack
# Given a circular array (the next element of the last element is the first element of the array), print the Next Greater Number for every element. The Next Greater Number of a number x is the first greater number to its traversing-order next in the array, which means you could search circularly to find its next greater number. If it doesn't exist, output -1 for this number.

# Example 1:
# Input: [1,2,1]
# Output: [2,-1,2]
# Explanation: The first 1's next greater number is 2; 
# The number 2 can't find next greater number; 
# The second 1's next greater number needs to search circularly, which is also 2.
# Note: The length of given array won't exceed 10000.

class Solution:
    def nextGreaterElements(self, nums):
        extended_nums = nums + nums
        stack = []
        
        results = [-1] * len(extended_nums)
        for i in range(len(extended_nums)-1, -1, -1):
            
            if len(stack) == 0:
                stack.append(extended_nums[i])
                
            while stack and extended_nums[i] >= stack[-1]:
                stack.pop()
            
            if stack:
                results[i] = stack[-1]
                
            else:
                results[i] = -1
                
            stack.append(extended_nums[i])
        
        
        return results[:len(nums)]


s1 = Solution()

print(s1.nextGreaterElements([1,2,3,1]))