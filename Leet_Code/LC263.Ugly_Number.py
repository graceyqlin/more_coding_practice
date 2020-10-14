# LC263.Ugly_Number.py
# Topic: Math
# Write a program to check whether a given number is an ugly number.

# Ugly numbers are positive numbers whose prime factors only include 2, 3, 5.

# Example 1:

# Input: 6
# Output: true
# Explanation: 6 = 2 × 3

def isUgly(num):
    # if num <= 0:
    #     return False
    
    # if num == 1:
    #     return True
    
    # allowed_factors = [2,3,5]
    
    # while num > 1:
    #     change = False
    #     for factor in allowed_factors:
    #         divider = num // factor
    #         mode = num % factor
    #         if mode == 0:
    #             num = divider
    #             change = True
                
    #     if not change:
    #         return False
        
    # return True
        
        #Another solution:
    if num <= 0:
        return False
    
    allowed_factors = [2,3,5]
    
    for factor in allowed_factors:
        while num%factor == 0:
            num/=factor
        
    return num == 1
    
        
