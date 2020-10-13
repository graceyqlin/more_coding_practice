#LC496.Next_Greater_Element_I.py
# Topics:stack
# very similar to daily temperature question
# You are given two arrays (without duplicates) nums1 and nums2 where nums1’s elements are subset of nums2. Find all the next greater numbers for nums1's elements in the corresponding places of nums2.

# The Next Greater Number of a number x in nums1 is the first greater number to its right in nums2. If it does not exist, output -1 for this number.

# Example 1:
# Input: nums1 = [4,1,2], nums2 = [1,3,4,2].
# Output: [-1,3,-1]
# Explanation:
#     For number 4 in the first array, you cannot find the next greater number for it in the second array, so output -1.
#     For number 1 in the first array, the next greater number for it in the second array is 3.
#     For number 2 in the first array, there is no next greater number for it in the second array, so output -1.

class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        next_greater_element = {}
        
        for i in range(len(nums2)-1, -1, -1):
            if len(stack) == 0:
                stack.append(nums2[i])
                
            while stack and nums2[i] >= stack[-1]:
                stack.pop()
            
            if stack:
                next_greater_element[nums2[i]] = stack[-1]
            else:
                next_greater_element[nums2[i]] = -1
            
            stack.append(nums2[i])
                
        return [next_greater_element.get(num) for num in nums1]
                
            
        