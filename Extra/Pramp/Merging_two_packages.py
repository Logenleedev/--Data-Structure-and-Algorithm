"""
Merging 2 Packages

Given a package with a weight limit limit and an array arr of item weights, 
implement a function getIndicesOfItemWeights that finds two items whose sum of weights equals the weight limit limit. 
Your function should return a pair [i, j] of the indices of the item weights, ordered such that i > j. 
If such a pair doesn’t exist, return an empty array.


input:  arr = [4, 6, 10, 15, 16],  lim = 21

output: [3, 1] # since these are the indices of the
               # weights 6 and 15 whose sum equals to 21
               
"""

# Method 1: Brute force
def merge_package_1(arr, limit):
    ans = []

    for i in range(len(arr) - 1):
        for j in range(i + 1, len(arr)):
            if arr[i] + arr[j] == limit:
                ans = [i, j]
                return ans 

    return ans 




# Method 2: Hash
def merge_package_2(arr, limit):

    ref = {}
    
    ans = []

    for i in range(len(arr)):
        if limit - arr[i] not in ref.keys():
            ref[arr[i]] = i 
        else:
            ans.append(i)
            ans.append(ref[limit - arr[i]])
    return ans  
print(merge_package_2([4, 6, 10, 15, 16], 25))
# Time Complexity: O(n)
# Space Complexity: O(n)