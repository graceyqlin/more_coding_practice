# LC245.Shortest_Word_Distance_III.py
# Topics: Array

# Given a list of words and two words word1 and word2, return the shortest distance between these two words in the list.

# word1 and word2 may be the same and they represent two individual words in the list.

# Example:
# Assume that words = ["practice", "makes", "perfect", "coding", "makes"].

# Input: word1 = “makes”, word2 = “coding”
# Output: 1
# Input: word1 = "makes", word2 = "makes"
# Output: 3



def shortestWordDistance(words, word1, word2):
        index1 = len(words)
        index2 = len(words)
        ans = len(words)
        
        if word1 != word2: 
            for i, word in enumerate(words):
                if word == word1:
                    index1 = i
                    ans = min(ans, abs(index1- index2))
                    
                if word == word2:
                    index2 = i
                    ans = min(ans, abs(index1 - index2))
        
        else:
            for i, word in enumerate(words):
                if word == word1:
                    index1 = i
                    ans = min(ans, abs(index1- index2))
                    index2 = i
        
        
        return ans