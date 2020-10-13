# 704.Binary_Search.py
# Topics: Binary_Search

# Given a sorted (in ascending order) integer array nums of n elements and a target value, write a function to search target in nums. If target exists, then return its index, otherwise return -1.


# Example 1:

# Input: nums = [-1,0,3,5,9,12], target = 9
# Output: 4
# Explanation: 9 exists in nums and its index is 4

def search(nums, target):
        l = 0
        r = len(nums) - 1
        while l + 1 < r:
            m = (r-l)// 2 + l
            if nums[m] == target:
                return m
            elif nums[m] > target:
                r = m
            else:
                l = m
        if nums[r] == target:
            return r
        if nums[l] == target:
            return l
        return -1

nums = [-1,0,3,5,9,12]
target = 9
print(search(nums, target))