def count_highly_profitable_months(stock_prices, k):

    ans = 0 

    for i in range(len(stock_prices) - k + 1):
        flag = True
        j = i 
        while j <= i + k - 2:
      
            if stock_prices[j] > stock_prices[j + 1]:
                flag = False 
            j += 1
        
        if flag:
            ans += 1

        
    
    return ans 

print(count_highly_profitable_months([5, 4,1, 2, 3], 3))

    
# Time Complexity: O((n - k) * k)
# Space Complexity: O(1)