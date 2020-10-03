# LC532.K-diff_Pairs_in_an_Array.py
# Topics: array, two pointer, hash table

# Given an array of integers nums and an integer k, return the number of unique k-diff pairs in the array.

# A k-diff pair is an integer pair (nums[i], nums[j]), where the following are true:

# 0 <= i, j < nums.length
# i != j
# a <= b
# b - a == k

# Example 1:

# Input: nums = [3,1,4,1,5], k = 2
# Output: 2
# Explanation: There are two 2-diff pairs in the array, (1, 3) and (3, 5).
# Although we have two 1s in the input, we should only return the number of unique pairs.

class Solution:
    def findPairs(self, nums):
        # time complexity O(n). because dictionary look up is a O(1) operation!
        import collections
        cnt = collections.Counter(nums)
        
        ans = 0
        
        for num in cnt:
            if k != 0:
                if num + k in cnt:
                    ans += 1
            else:
                if cnt[num] > 1:
                    ans += 1
                    
        return ans