# LC1446.Consecutive_Characters.py
# Topics: String

# Given a string s, the power of the string is the maximum length of a non-empty substring that contains only one unique character.

# Return the power of the string.

 

# Example 1:

# Input: s = "leetcode"
# Output: 2
# Explanation: The substring "ee" is of length 2 with the character 'e' only.

def maxPower(self, s: str) -> int:
        if len(s) == 0:
            return 0
        if len(s) == 1:
            return 1
        
        cur = s[0]
        cnt = 1
        ans = 1
        
        for i in range(1, len(s)):
            if s[i] == cur:
                cnt += 1
                ans = max(ans, cnt)
                
            else:
                # ans = max(ans, cnt)
                cnt = 1
                cur = s[i]
                
        return ans
            
