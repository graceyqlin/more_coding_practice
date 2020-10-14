# LC264.Ugly_Number_II.py
#Topics: Dymanic Programming, Math, Heap
# Write a program to find the n-th ugly number.

# Ugly numbers are positive numbers whose prime factors only include 2, 3, 5. 

# Example:

# Input: n = 10
# Output: 12
# Explanation: 1, 2, 3, 4, 5, 6, 8, 9, 10, 12 is the sequence of the first 10 ugly numbers.
# Note:  

# 1 is typically treated as an ugly number.
# n does not exceed 1690.

def nthUglyNumber(n):
        #time complexity:O(n)
        #space complexity:O(n)
        
        if n == 1:
            return 1
        
        dp = [0] * n
        
        dp[0] = 1
        power_2 = 0
        power_3 = 0
        power_5= 0
        
        for i in range(1, n):
            
            dp[i] = min(dp[power_2]*2, dp[power_3]*3, dp[power_5] * 5)
            
            if dp[i] == dp[power_2]*2:
                power_2 += 1
                
            if dp[i] == dp[power_3]*3:
                power_3 += 1
                
            if dp[i] == dp[power_5]*5:
                power_5 += 1
                
        return dp[-1]
                
