def max_profit(arr, k):
    temp = []


    num = arr[::-1]
    
    for i in range(len(arr) // k):
        ans = 0 

        # side one 

        ans += sum(arr[i : i + k])
        ans += sum(num[i : i + k])

        print("side1", arr[i : i + k])
        print("side2", num[i : i + k])

        temp.append(ans)

    return max(temp)
        
print(max_profit([1, 5, 1, 3, 7, -3], 3))