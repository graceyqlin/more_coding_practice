# HackerRank_NLP_From_Paragraph_To_Sentences.py
# https://www.hackerrank.com/challenges/from-paragraphs-to-sentences/problem

# An Introduction to Sentence Segmentation

# Sentence segmentation, means, to split a given paragraph of text into sentences, by identifying the sentence boundaries. In many cases, a full stop is all that is required to identify the end of a sentence, but the task is not all that simple.

# This is an open ended challenge to which there are no perfect solutions. Try to break up given paragraphs into text into individual sentences. Even if you don't manage to segment the text perfectly, the more sentences you identify and display correctly, the more you will score.

# Abbreviations: Dr. W. Watson is amazing. In this case, the first and second "." occurs after Dr (Doctor) and W (initial in the person's name) and should not be confused as the end of the sentence.

# Sentences enclosed in quotes: "What good are they? They're led about just for show!" remarked another. All of this, should be identified as just one sentence.

# Questions and exclamations: Who is it? -This is a question. This should be identified as a sentence. I am tired!: Something which has been exclaimed. This should also be identified as a sentence.

# INPUT FORMAT

# You will be given a chunk of text, containing several sentences, questions, statements and exclamations- all in 1 line.

# if read from HackerRank:
# Enter your code here. Read input from STDIN. Print output to STDOUT
# import fileinput 

# temp = []  
# for f in fileinput.input(): 
#     temp.append(f)

with open('input00.txt', 'r') as text:
    textfile = text.read()
    print(textfile)


double_quote_open = False
single_quote_open = False

letter_list = list(textfile)

end_index_list = []
end_index_list.append(-2)

for i, letter in enumerate(letter_list):
    if i == 0 or i == len(letter_list) - 1:
        continue
    else:
        prev_letter = letter_list[i-1]
        after_letter = letter_list[i+1]
        
        if letter == '"' and prev_letter == ' ':
            doulbe_quote_open = True
            
        elif letter == '"' and after_letter == ' ':
            doulbe_quote_open = False
            if prev_letter == '.':
                end_index_list.append(i)
                
        elif letter == "'" and prev_letter == ' ':
            single_quote_open = True      
            
        elif letter == "'" and after_letter == ' ':
            single_quote_open = False
            if prev_letter == '.':
                end_index_list.append(i)
        
        elif (letter == '.' or letter == '?' or letter == '!') and (not double_quote_open and not single_quote_open):
            end_index_list.append(i)
            


for k in range(len(end_index_list)-1):
    start_index = end_index_list[k]+2
    end_index = end_index_list[k+1]+1
    print(textfile[start_index:end_index])

    
