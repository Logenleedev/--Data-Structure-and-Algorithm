"""
Word Count Engine

Implement a document scanning function wordCountEngine, which receives a string document and returns a list of all unique words in it 
and their number of occurrences, sorted by the number of occurrences in a descending order. If two or more words have the same count, 
they should be sorted according to their order in the original sentence. Assume that all letters are in english alphabet. 
You function should be case-insensitive, so for instance, the words “Perfect” and “perfect” should be considered the same word.

The engine should strip out punctuation (even in the middle of a word) and use whitespaces to separate words.


input:  document = "Practice makes perfect. you'll only
                    get Perfect by practice. just practice!"

output: [ ["practice", "3"], ["perfect", "2"],
          ["makes", "1"], ["youll", "1"], ["only", "1"], 
          ["get", "1"], ["by", "1"], ["just", "1"] ]
Important: please convert the occurrence integers in the output list to strings (e.g. "3" instead of 3).

"""

from collections import defaultdict 


def word_count_engine(document):
    arr = document.split(' ')

    ref = defaultdict(int)

    for char in arr:
        temp = ''
        for i in range(len(char)):
            if char[i].isalpha():
                temp += char[i]
        ref[temp.lower()] += 1 

    ans = []
    for key, value in ref.items():
        ans.append([key, value])

    ans = sorted(ans, key = lambda x: -x[1])

    return ans 
    
print(word_count_engine("Practice makes perfect. you'll only get Perfect by practice. just practice!"))