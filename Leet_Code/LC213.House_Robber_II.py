# LC213.House_Robber_II.py
# Topic: Dymanic Programming
# You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed. All houses at this place are arranged in a circle. That means the first house is the neighbor of the last one. Meanwhile, adjacent houses have a security system connected, and it will automatically contact the police if two adjacent houses were broken into on the same night.

# Given a list of non-negative integers nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.

 

# Example 1:

# Input: nums = [2,3,2]
# Output: 3
# Explanation: You cannot rob house 1 (money = 2) and then rob house 3 (money = 2), because they are adjacent houses.

def rob(nums):
    if not nums:
        return 0
    
    if len(nums) == 1:
        return nums[0]
    
    if len(nums) == 2:
        return max(nums[0], nums[1])
    
    def max_rob(nums):
        dp = [0] * len(nums)
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
        for i in range(2, len(nums)):
            dp[i] = max(dp[i-2]+ nums[i], dp[i-1])
        return dp[-1]
    
    dp1 = max_rob(nums[:-1])
    
    dp2 = max_rob(nums[1:])
    
    return max(dp1, dp2)