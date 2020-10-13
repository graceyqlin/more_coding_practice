# 859.Buddy_Strings.py
# Topics: strings

# Given two strings A and B of lowercase letters, return true if you can swap two letters in A so the result is equal to B, otherwise, return false.

# Swapping letters is defined as taking two indices i and j (0-indexed) such that i != j and swapping the characters at A[i] and A[j]. For example, swapping at indices 0 and 2 in "abcd" results in "cbad".

def buddyStrings(A: str, B: str):
    import collections
    if len(A) != len(B):
        return False
    
    if len(A) == 0:
        return False
    
    if A == B and len(A) > len(set(A)):
        return True
    
    diffs = [i for i in range(len(A)) if A[i] != B[i]]
    
    
    return len(diffs) == 2 and A[diffs[0]] == B[diffs[1]] and A[diffs[1]] == B[diffs[0]]

A = "abcaa"
B = "abcbb"

print(buddyStrings(A, B))