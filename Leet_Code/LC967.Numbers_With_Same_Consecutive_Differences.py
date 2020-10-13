#LC967.Numbers_With_Same_Consecutive_Differences.py
# Topic: DFS
# Return all non-negative integers of length n such that the absolute difference between every two consecutive digits is k.

# Note that every number in the answer must not have leading zeros except for the number 0 itself. For example, 01 has one leading zero and is invalid, but 0 is valid.

# You may return the answer in any order.

# Example 1:

# Input: n = 3, k = 7
# Output: [181,292,707,818,929]
# Explanation: Note that 070 is not a valid number, because it has leading zeroes.

class Solution:
    def numsSameConsecDiff(self, n: int, k: int) -> List[int]:
        if n == 1:
            return [i for i in range(1, 10)]
        
        ans = []
        def dfs(remain_digit, cur_num):
            if remain_digit == 0:
                ans.append(cur_num)
                return 
            
            next_digits = set([cur_num%10 +k, cur_num%10 -k])
            
            for next_digit in next_digits:
                if next_digit >=0 and next_digit <=9:
                    # remain_digit -= 1
                    # cur_num = cur_num*10 + next_digit
                    dfs(remain_digit -1, cur_num*10 + next_digit)
                    
        for cur_num in range(1,10):
            dfs(n-1, cur_num)
        
        return ans
            
        