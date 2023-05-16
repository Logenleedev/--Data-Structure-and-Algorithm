"""
Getting a Different Number

Given an array arr of unique nonnegative integers, implement a function getDifferentNumber that finds the smallest nonnegative integer that is NOT in the array.

input:  arr = [0, 1, 2, 3]
output: 4 

input:  arr = [0, 2, 3]
output: 1
"""

def get_array(num):
    for i in range(len(num)):
        if num[i] != i:
            return i 

    return len(num)

print(get_array([1, 2, 3]))

# Time Complexity: O(n)
# Space Complexiy: O(1)
    