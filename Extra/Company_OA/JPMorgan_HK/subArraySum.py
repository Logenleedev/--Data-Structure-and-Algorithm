import sys

n = int(sys.stdin.readline().strip())  # read first line
temp = []
for _ in range(n):
    data = int(input())
    temp.append(data)


def SubArraySum(arr, n):
    result = 0
 
    # computing sum of subarray
    # using formula
    for i in range(0, n):
        result += (arr[i] * (i+1) * (n-i))
 
    # return all subarray sum
    return result

print(SubArraySum(temp, n))