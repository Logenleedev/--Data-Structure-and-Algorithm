
import sys

s = sys.stdin.readline().strip()
target = int(s.split(';')[1])
number_string = s.split(';')[0]

temp = []

for element in number_string.split(','):
    temp.append(int(element))

def solution(num, target):
    ref = dict()
    ans = []
    temp = []
    for i in range(len(num)):
        if target - num[i] not in ref.keys():
            ref[num[i]] = i
        else:
            ans.append([num[ref[target - num[i]]], num[i]])
           
    ans = sorted(ans, key=lambda x: x[0])
    
    for i in range(len(ans)):
        element = ans[i]
        temp.append(str(element[0]) + ',' + str(element[1]))



    return ';'.join(temp)


print(solution(temp, target))