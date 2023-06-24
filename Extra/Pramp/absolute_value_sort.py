"""
Absolute Value Sort

Given an array of integers arr, write a function absSort(arr), that sorts the array according to the absolute values of the numbers in arr. 
If two numbers have the same absolute value, sort them according to sign, where the negative numbers come before the positive numbers.

Examples:

input:  arr = [2, -7, -2, -2, 0]
output: [0, -2, -2, 2, -7]
"""

def solution(arr):
    arr = sorted(arr, key=lambda x: abs(x))
    
    for i in range(len(arr) - 1):
        if abs(arr[i]) == abs(arr[i + 1]) and arr[i] > 0 and arr[i + 1] < 0:
            arr[i], arr[i + 1] = arr[i + 1], arr[i]
    print(arr)

solution([2, -7, -2, -2, 0])