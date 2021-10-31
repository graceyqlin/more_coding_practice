# LC243.Shortest_Word_Distance.py
# Topics: Array

# Given a list of words and two words word1 and word2, return the shortest distance between these two words in the list.

# Example:
# Assume that words = ["practice", "makes", "perfect", "coding", "makes"].

# Input: word1 = “coding”, word2 = “practice”
# Output: 3
# Input: word1 = "makes", word2 = "coding"
# Output: 1

# Best Solution:
# Don't iterate all over

# Time complexity: O(n)

def get_distance(words, word1, word2):
	min_distance = len(words)
	word1_index = len(words)
	word2_index = len(words)

	for i, word in enumerate(words):
		if word == word1:
			word1_index = i
			min_distance = min(min_distance, abs(word1_index - word2_index))

		elif word == word2:
			word2_index = i
			min_distance = min(min_distance, abs(word1_index - word2_index))

	return min_distance

word1 = 'coding'
word2 = 'practice'
words = ["practice", "makes", "perfect", "coding", "makes"]

print(get_distance(words, word1, word2))




