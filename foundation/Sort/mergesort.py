def merge_sort(arr):
    if len(arr) > 1:
        left_arr = arr[:len(arr) // 2]
        right_arr = arr[len(arr) // 2 :]
        # recursion
        merge_sort(left_arr)
        merge_sort(right_arr)



        # merge
        
        i = 0  # leftmost index
        j = 0  # rightmost index
        k = 0 # merge array index 
        while i < len(left_arr) and j < len(right_arr):
            if left_arr[i] < right_arr[j]:
                arr[k] = left_arr[i]
                i += 1
                k += 1
            else:
                arr[k] = right_arr[j]
                j += 1
                k += 1

        while i < len(left_arr):
            arr[k] = left_arr[i]
            i += 1
            k += 1

        while j < len(right_arr):
            arr[k] = right_arr[j]
            j += 1
            k += 1



a = [3, 1, 2, 3, 1, 3]
merge_sort(a)
print(a)

    






# Time complexity: Onlog(n)

# Step 1: split the array in half
# Step 2: call merge sort on eac half to sort them recursively
# Step 3: Merge both sorted halves into one sorted array