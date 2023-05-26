def contprofit(arr, k):
    profits = 0
    for i in range(len(arr) - k):
        window = sum(arr[i : i + k])


        for j in range(i + k, len(arr)):
            nextwindow = sum(arr[j : j + k])


            if j + k > len(arr) - 1:
                diff = (j + k) - len(arr)
                nextwindow += sum(arr[0:diff])
            profits = max(profits, window + nextwindow)
    return profits
        
print(contprofit([1, 5, 1, 3, 7, -3], 2))