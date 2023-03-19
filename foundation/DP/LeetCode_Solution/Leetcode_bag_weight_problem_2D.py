def test_2_wei_bag_problem1(bag_size, weight, value):
    row = len(weight)
    col = bag_size + 1


    dp = [[0 for _ in range(col)] for _ in range(row)]

    for i in range(row):
        dp[i][0] = 0

    for j in range(1, col):
        if weight[0] <= j:
            dp[0][j] = value[0]
    
    # 先遍历物品
    for i in range(1, row):

        cur_weight = weight[i]
        cur_value = value[i]

        for j in range(1, col):

            if cur_weight > j:
                dp[i][j] = dp[i - 1][j]
            else:
                dp[i][j] = max(dp[i - 1][j - cur_weight] + cur_value, dp[i - 1][j])
    print(dp)






if __name__ == "__main__": 
	bag_size = 4
	weight = [1, 3, 4]
	value = [15, 20, 30]
	test_2_wei_bag_problem1(bag_size, weight, value)