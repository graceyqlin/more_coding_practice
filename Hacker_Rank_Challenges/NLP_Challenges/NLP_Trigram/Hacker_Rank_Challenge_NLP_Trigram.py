# Hacker_Rank_Challenge_NLP_Trigram
# https://www.hackerrank.com/challenges/the-trigram/problem

# Given a large chunk of text, identify the most frequently occurring trigram in it. If there are multiple trigrams with the same frequency, then print the one which occurred first.

# Assume that trigrams are groups of three consecutive words in the same sentence which are separated by nothing but a single space and are case insensitive. The size of the input will be less than 10 kilobytes.

# Input: I love games. I love to code. Here "games I love" is not a trigram because all the three words in trigram should be from the same sentence.

def get_most_frequent_trigram(s):

	# when read from Hackerrank:

	# import sys
	# import re
	# s = " ".join([lines.strip().lower() for lines in sys.stdin.readlines()])

    from collections import defaultdict 
    count_dic = defaultdict(list)
    max_cnt = 0
    max_tri = ''
        
    s_list = s.split(' ')

    if len(s_list) <= 3:
        return s

    for i in range(len(s_list)-2):
        current_tri = [word.lower() for word in s_list[i:i+3]]
        combined_word = ''.join(current_tri) 
        if combined_word.isalpha():                
            if combined_word in count_dic:
                count_dic[combined_word] += 1
            else:
                count_dic[combined_word] = 1

            if count_dic[combined_word] > max_cnt:
                max_tri = ' '.join(current_tri)        
                max_cnt = count_dic[combined_word]
                
    return max_tri                    


s1 = 'I came from the moon. He went to the other room. She went to the drawing room.'
print(get_most_frequent_trigram(s1))