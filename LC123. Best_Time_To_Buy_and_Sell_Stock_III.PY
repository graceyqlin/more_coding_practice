#LC123. Best Time To Buy and Sell Stock III
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