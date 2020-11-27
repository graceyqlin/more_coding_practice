# LC159.Longest_Substring_with_At_Most_Two_Distinct_Characters.py
# Topics: hash table, two pointers, string, sliding window
# Given a string s , find the length of the longest substring t  that contains at most 2 distinct characters.

# Example 1:

# Input: "eceba"
# Output: 3
# Explanation: t is "ece" which its length is 3.

def lengthOfLongestSubstringTwoDistinct(s):
        if len(s) == 0:
            return 0
        if len(s) == 1:
            return 1
        
        location_dict = {}
        start = 0
        ans = 0
        max_distinct_char = 2
        
        for end in range(len(s)):
            current_length = 0
            if s[end] not in location_dict:
                if len(location_dict.keys()) >= max_distinct_char:
                    first_character_index = min(location_dict.values())
                    start = first_character_index + 1
                    location_dict.pop(s[first_character_index])
                    
            location_dict[s[end]] = end     
            current_length = end - start + 1
            ans = max(ans,current_length)
            
        
        return ans