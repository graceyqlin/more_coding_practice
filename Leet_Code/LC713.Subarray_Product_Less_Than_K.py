#LC713.Subarray_Product_Less_Than_K.py
#Topics: Two Pointers, Array
# Your are given an array of positive integers nums.

# Count and print the number of (contiguous) subarrays where the product of all the elements in the subarray is less than k.

# Example 1:
# Input: nums = [10, 5, 2, 6], k = 100
# Output: 8
# Explanation: The 8 subarrays that have product less than 100 are: [10], [5], [2], [6], [10, 5], [5, 2], [2, 6], [5, 2, 6].
# Note that [10, 5, 2] is not included as the product of 100 is not strictly less than k.

class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        #time complexity:O(n)
        #topics: two pointer, array
        start = 0
        end = 0
        ans = 0
        cur_num = 1
        for end in range(len(nums)):
            cur_num *= nums[end]
            while cur_num >= k and start <= end:
                cur_num /= nums[start]
                start += 1
            ans += (end - start + 1)
        return ans
                
            