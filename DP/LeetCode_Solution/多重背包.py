# 先遍历物品，再遍历背包

def test_complete_pack1():
    weight = [1, 3, 4]
    value = [15, 20, 30]
    bag_weight = 4

    dp = [0]*(bag_weight + 1)

    for i in range(len(weight)):
        for j in range(weight[i], bag_weight + 1):
            
            dp[j] = max(dp[j], dp[j - weight[i]] + value[i])
            print(dp)
    


if __name__ == '__main__':
    test_complete_pack1()
    