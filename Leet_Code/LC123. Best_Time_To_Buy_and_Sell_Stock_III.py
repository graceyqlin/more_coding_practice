#LC123. Best Time To Buy and Sell Stock III

## Topic: DP, Array

# Say you have an array for which the ith element is the price of 
# a given stock on day i.

# Design an algorithm to find the maximum profit. 
# You may complete at most two transactions.

# Note: You may not engage in multiple transactions at the same time
 # (i.e., you must sell the stock before you buy again).

# Input: prices = [3,3,5,0,0,3,1,4]
# Output: 6
# Explanation: Buy on day 4 (price = 0) and sell on day 6 (price = 3), 
# profit = 3-0 = 3.
# Then buy on day 7 (price = 1) and sell on day 8 (price = 4), 
# profit = 4-1 = 3.


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # inspired by:
        # https://www.youtube.com/watch?v=gsL3T9bI1RQ&ab_channel=HuifengGuan
        
        hold1 = float(-inf)
        sold1 = 0
        hold2 = float(-inf)
        sold2 = 0
        
        for p in prices:
            hold1 = max(hold1, 0-p)
            sold1 = max(sold1, hold1 + p)
            hold2 = max(hold2, sold1 - p)
            sold2 = max(sold2, hold2 + p)
        
        return max(sold1, sold2)