
'''
Two strings are considered "almost equivalent" if they have the same length AND for each lowercase letter x, the number of occurrences of 
x in the two strings differs by no more than 3. 也就是给定2个, String, 判断这2个String是不是"almost equivalent".
'''
'''
# ACM 加入 

import sys

s1 = sys.stdin.readline().strip() 
s2 = sys.stdin.readline().strip() 
'''

def solution(word1, word2):
    ref1 = [0] * 26
    ref2 = [0] * 26

    if len(word1) != len(word2):
        return False
        
    for char in word1:
        ref1[ord(char) - ord("a")] += 1

    for char in word2:
        ref2[ord(char) - ord("a")] += 1

    for j in range(26):
        if abs(ref1[j] - ref2[j]) > 3:
            return False
            
    return True 

print(solution("aaaa", "bcb"))

