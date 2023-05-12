def array_of_array_products(arr):
    
    left_product = 1 
    right_product = 1
    
    left = [1] * len(arr)
    right = [1] * len(arr)
    ans = [1] * len(arr)
    
    for i in range(len(arr) - 1):
        left_product *= arr[i]
        left[i + 1] = left_product 
        
    for j in range(len(arr) - 1, 0, -1):
        right_product *= arr[j]
        right[j - 1] = right_product 
        
    for i in range(len(ans)):
        ans[i] = left[i] * right[i]
    

    return ans 
    
print(array_of_array_products([2, 7, 3,4 ]))

# Time Complexity: O(n)
# Space Complexity: O(n)