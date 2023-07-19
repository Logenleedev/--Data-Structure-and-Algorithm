'''

第一道是找出String中(包含多个words)的最长的even length的单词. 

Example
sentence = "Time to write great code"
The lengths of the words are 4, 2, 5, 5, 4, in order, The longest even length words are "Time" and "code". The one that occurs first is "Time", which is the answer to return.


'''
'''
# ACM 加入 

import sys

s = sys.stdin.readline().strip() 
'''

def solution(arr):
    arr = arr.split(" ")
    ans = []
    temp = []
    res = 0
    for i in range(len(arr)):
        length = len(arr[i])
        if length % 2 == 0:
            temp.append([length, arr[i]])
            res = max(res, length)

    temp = sorted(temp, key=lambda x: -x[0])
    
    for j in range(len(temp)):
        if temp[j][0] == res:
            print(res)
            ans.append(temp[j][1])

    return ans

print(solution("Timeed to write great code"))



