import sys

n = int(sys.stdin.readline().strip())  # read first line
temp = []
for _ in range(n):
    data = int(input())
    temp.append(data)


def SubArraySum(arr, n):
    temp, result = 0, 0
 
    # Pick starting point
    for i in range(0, n):
 
        # Pick ending point
        temp = 0
        for j in range(i, n):
            
            # sum subarray between
            # current starting and
            # ending points
            temp += sum(arr[i: j + 1])
        result += temp
    return result

print(SubArraySum(temp, n))