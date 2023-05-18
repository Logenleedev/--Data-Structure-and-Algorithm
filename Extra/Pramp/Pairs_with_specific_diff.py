"""
Pairs with Specific Difference

Given an array arr of distinct integers and a nonnegative integer k, 
write a function findPairsWithGivenDifference that returns an array of all pairs [x,y] in arr, such that x - y = k. 
If no such pairs exist, return an empty array.

Note: the order of the pairs in the output array should maintain the order of the y element in the original array.


input:  arr = [0, -1, -2, 2, 1], k = 1
output: [[1, 0], [0, -1], [-1, -2], [2, 1]]

input:  arr = [1, 7, 5, 3, 32, 17, 12], k = 17
output: []

"""


def find_pairs_with_given_difference_brute(arr, k):
  
    ans = []

    for i in range(len(arr) - 1):
        for j in range(1, len(arr)):
            if arr[i] - arr[j] == k:
                if [arr[i], arr[j]] not in ans:
                    ans.append([arr[i], arr[j]])
            elif arr[j] - arr[i] == k:
                if [arr[j], arr[i]] not in ans:
                    ans.append([arr[j], arr[i]])

    return ans 


# like two sum 
# if complement not in -> 把自己加进去
# if complement in -> 操作。 弄到答案数组

def find_pairs_with_given_difference(arr, k):
    complement = set()
    ans = []

    for i in range(len(arr)):
        x = arr[i] + k 
        y = arr[i] - k

        if x in complement:
            ans.append([x , arr[i]])
        if y in complement:
            ans.append([arr[i], y])
     

        complement.add(arr[i])
        

    return ans 


print(find_pairs_with_given_difference([0, -1, -2, 2, 1], 1))
        