# LC187.Repeated_DNA_Sequences.py
# Topics: Hash Table, Big Manipulation
# All DNA is composed of a series of nucleotides abbreviated as 'A', 'C', 'G', and 'T', for example: "ACGAATTCCG". When studying DNA, it is sometimes useful to identify repeated sequences within the DNA.

# Write a function to find all the 10-letter-long sequences (substrings) that occur more than once in a DNA molecule.

 

# Example 1:

# Input: s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
# Output: ["AAAAACCCCC","CCCCCAAAAA"]

def findRepeatedDnaSequences(s):
        import collections
        if len(s) <= 10:
            return []
        
        sub_strings = {}
        
        sequence_length = 10
        
        for i in range(len(s)-sequence_length+1):
            sub_string = s[i:i+sequence_length] 
            if sub_string in sub_strings:
                sub_strings[sub_string] += 1
            else:
                sub_strings[sub_string] = 1
        
        return [i for i in sub_strings if sub_strings[i] > 1]