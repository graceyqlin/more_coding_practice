# when finding max/ min window length: ans = max(ans, end - start + 1)
# when finding max/ min array numbers: ans += end - start + 1

# when finding max window at most k target, we can use regular max template. 
# when finding max window equal k target, we need to use function(k) - function(k-1)


# 1. when finding minimal window length with sum greater than target
## initiate hash_map, find a valid window, then shrink to find the smallest valid window. 

# 209. Minimum Size Subarray Sum
# Given an array of positive integers nums and a positive integer target, 
# return the minimal length of a contiguous subarray [numsl, numsl+1, ..., numsr-1, numsr] 
# of which the sum is greater than or equal to target. If there is no such subarray, 
# return 0 instead.

# Example 1:

# Input: target = 7, nums = [2,3,1,2,4,3]
# Output: 2
# Explanation: The subarray [4,3] has the minimal length under the problem constraint.

class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        start = 0
        end = 0
        min_sub_len = len(nums) + 1
        cur_total = 0
        
        while end < len(nums):
            cur_total += nums[end]
            # first find valid conditions
            while cur_total >= s and start <= end:
                if end - start + 1 < min_sub_len:
                    min_sub_len = end - start + 1
                # then shrink the window to find minimal window to satisfy the condition
                cur_total -= nums[start]
                start += 1
            end += 1
        
        if min_sub_len == len(nums) + 1:
            return 0
        else:
            return min_sub_len


# 2. when finding max window length with cost less than k
## initiate hash_map, find a invalid condition, then shrink to find the largets window satisfy the condition

# 1208. Get Equal Substrings Within Budget
# You are given two strings s and t of the same length and an integer maxCost.
# You want to change s to t. Changing the ith character of s to ith character of 
# t costs |s[i] - t[i]| (i.e., the absolute difference between the ASCII values of the characters).

# Return the maximum length of a substring of s that can be changed to be 
# the same as the corresponding substring of t with a cost less than or equal to maxCost. 
# If there is no substring from s that can be changed to its corresponding substring from t, return 0.

# Example 1:
# Input: s = "abcd", t = "bcdf", maxCost = 3
# Output: 3
# Explanation: "abc" of s can change to "bcd".
# That costs 3, so the maximum length is 3.


class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        start = 0
        end = 0
        cur_cost = 0
        max_substring_len = 0
        s_ascii = [ord(i) for i in s]
        t_ascii = [ord(i) for i in t]
        
        while end < len(s):
            cur_cost += abs(t_ascii[end] - s_ascii[end])
            # first using invalid condition then shrink the window to find largest valid window
            while start <= end and cur_cost > maxCost:
                cur_cost -= abs(t_ascii[start] - s_ascii[start])
                start += 1
            if cur_cost <= maxCost:
                max_substring_len = max(max_substring_len, end - start + 1)
            end += 1
        
        return max_substring_len

# 3. finding max array number with product less than k

# 713. Subarray Product Less Than K
# Given an array of integers nums and an integer k, return the number of contiguous subarrays 
# where the product of all the elements in the subarray is strictly less than k.

# Example 1:

# Input: nums = [10,5,2,6], k = 100
# Output: 8
# Explanation: The 8 subarrays that have product less than 100 are:
# [10], [5], [2], [6], [10, 5], [5, 2], [2, 6], [5, 2, 6]
# Note that [10, 5, 2] is not included as the product of 100 is not strictly less than k.

class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k == 0:
            return 0
        
        max_sub_array = 0
        start = 0
        end = 0
        current_product = 1
        
        while end < len(nums):
            current_product *= nums[end]
            # invalid condition then shrink the window
            while current_product >= k and start <= end:
                current_product /= nums[start]
                start += 1
            if current_product < k:
                # using this to get the array number
                max_sub_array += end - start + 1
            end += 1
        
        return max_sub_array


#4. finding max subarray number with target equal to k. Need to call sub function.

#930. Binary Subarrays With Sum
# Given a binary array nums and an integer goal, return the number of non-empty subarrays 
# with a sum goal.
# A subarray is a contiguous part of the array.

# Example 1:

# Input: nums = [1,0,1,0,1], goal = 2
# Output: 4
# Explanation: The 4 subarrays are bolded and underlined below:
# [1,0,1,0,1]
# [1,0,1,0,1]
# [1,0,1,0,1]
# [1,0,1,0,1]

class Solution:
    def numSubarraysWithSum(self, A: List[int], S: int) -> int:
        return self.numSubarraysWithSumAtMostS(A, S) - self.numSubarraysWithSumAtMostS(A, S-1)
    
    def numSubarraysWithSumAtMostS(self, A: List[int], S: int) -> int:
        if S < 0:
            return 0
        
        max_sub_array = 0
        start = 0
        end = 0
        current_total = 0
        
        while end < len(A):
            current_total += A[end]
            while start <= end and current_total > S:
                current_total -= A[start]
                start += 1
            if current_total <= S:
                max_sub_array += end - start + 1
            end += 1
        
        return max_sub_array


#5. max window at most k distinct characters. need to use counter and track frequency. 
# 340. Longest Substring with At Most K Distinct Characters

# Given a string s and an integer k, return the length of the longest substring of s that 
# contains at most k distinct characters.
# Example 1:

# Input: s = "eceba", k = 2
# Output: 3
# Explanation: The substring is "ece" with length 3.

class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        if k == 0 or len(s) == 0:
            return 0
        
        start = 0
        end = 0
        max_sub_len = 0
        location_dict = dict()
        
        while end < len(s) and start <= end:
            if s[end] not in location_dict:
                if len(location_dict.keys()) >= k:
                    min_index = min(location_dict.values())
                    start = min_index + 1
                    location_dict.pop(s[min_index])
            location_dict[s[end]] = end
            max_sub_len = max(max_sub_len, end - start + 1)
            end += 1
        
        return max_sub_len