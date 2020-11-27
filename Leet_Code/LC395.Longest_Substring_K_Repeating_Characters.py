# LC395.Longest_Substring_K_Repeating_Characters.py

# Topics: devide and conquer, recursion, sliding window

# Given a string s and an integer k, return the length of the longest substring of s such that the frequency of each character in this substring is greater than or equal to k.

 

# Example 1:

# Input: s = "aaabb", k = 3
# Output: 3
# Explanation: The longest substring is "aaa", as 'a' is repeated 3 times.


def longestSubstring(s, k):
    import collections
    s_counter = collections.Counter(s)
    for c in set(s):
        if s_counter[c]<k:
            max_lengh = max(
                [self.longestSubstring(sub, k) for sub in s.split(c) if len(sub) >=k] or [0])
            return max_lengh
                            
    return len(s)
