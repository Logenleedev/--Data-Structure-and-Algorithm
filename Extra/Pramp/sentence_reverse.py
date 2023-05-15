def reverse(arr, i, j):
    # [left, right] interval

    while i <= j:

        arr[i], arr[j] = arr[j], arr[i]

        i += 1
        j -= 1
   


    

def main(arr):

    start = 0 
    end = 0 


    while end <= len(arr):
      
        if end == len(arr):
            reverse(arr, start, end - 1)
            
            break 
        if arr[end] == ' ':
            reverse(arr, start, end - 1)
            start = end + 1
            end += 1
        else:
            end += 1
      
        
        
    reverse(arr, 0, len(arr) - 1)


    return arr

print(main(['a', 'b', ' ', 'b', 'c', ' ', 'd', 'e']))

# Time Complexity: O(n)
# Space Complexity: O(1)