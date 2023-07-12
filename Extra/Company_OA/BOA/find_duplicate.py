'''
Simple coding: 找相同的数字
可选C++ / Python
input1：
1,3,4;4,5,6
output:
4
input2:
7,8,9;8,9,10
output:
8,9
'''
import sys
from collections import defaultdict

s = sys.stdin.readline().strip()

temp = []
ans = []

ref = defaultdict(int)

for i in range(len(s)):
    temp.append(s[i].split(','))


for element in temp:
    for num in element:
        ref[num] += 1

for key, value in ref.items():
    if value >= 2 and key != '':
        ans.append(key)

print(','.join(ans))



    

