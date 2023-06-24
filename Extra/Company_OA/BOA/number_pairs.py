

# Method 1:
def solution(num, target):
    ans = []
    for i in range(len(num) - 1):
        for j in range(i, len(num)):
            if num[i] + num[j] == target:
                ans.append(num[i])
                ans.append(num[j])
    return ans 
# Time Complexity: O(n^2)
# Space Complexity: O(n)
# print(solution([1, 2,  3, 4,  6], 5))



# Method 2:
def solution2(num, target):
    ref = dict()
    ans = []
    for i in range(len(num)):
        if target - num[i] not in ref.keys():
            ref[num[i]] = i
        else:
            ans.append(num[ref[target - num[i]]])
            ans.append(num[i])
    return ans

print(solution2([1, 2, 3, 4,  6], 5))

# Time Complexity: O(n)
# Space Complexity: O(n)
