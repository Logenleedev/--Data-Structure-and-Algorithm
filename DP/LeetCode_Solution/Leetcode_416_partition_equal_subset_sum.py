class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        target = sum(nums)
        nums = sorted(nums)

        # 做最初的判断
        if target % 2 != 0:
            return False

        # 找到 target value 可以认为这个是背包的体积
        target = target // 2

        row = len(nums)
        col = target + 1

        # 定义 dp table
        dp = [[0 for _ in range(col)] for _ in range(row)] 

        # 初始 dp value
        for i in range(row):
            dp[i][0] = 0
        
        for j in range(1, target):
            if nums[0] <= j:
                dp[0][j] = nums[0]

        # 遍历 先遍历物品再遍历背包
        for i in range(1, row):

            cur_weight = nums[i]
            cur_value = nums[i]

            for j in range(1, col):
                if cur_weight > j:
                    dp[i][j] = dp[i - 1][j]
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - cur_weight] + cur_value)
            
        # 输出结果
        return dp[-1][col - 1] == target   