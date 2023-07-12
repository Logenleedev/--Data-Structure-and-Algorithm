'''
求1 to n 的和 且 不加 5与7的倍数
'''
import sys
s = sys.stdin.readline().strip()

def solution(n):
    sum = 0 
    for i in range(1, n + 1):
        if i % 5 != 0 and i % 7 != 0:
            sum += i
            
    return sum

print(solution(int(s)))

