#LC680.Valid_Palindrome_II

# Given a non-empty string s, you may delete at most one character. 
# Judge whether you can make it a palindrome.

# Example 1:
# Input: "aba"
# Output: True

class Solution:
    def validPalindrome(self, s: str) -> bool:
        l = 0
        r = len(s) - 1
        while l<r:
            if s[l] == s[r]:
                l += 1
                r -= 1
            else:
                if self.validuntil(s, l, r-1) or self.validuntil(s, l+1, r):
                    return True
                else:
                    return False
        return True
                
    def validuntil(self, s, l, r):
        while l < r:
            if s[l] == s[r]:
                l += 1
                r -=1
            else:
                return False
        return True