class Solution:
    def miceAndCheese(self, reward1: List[int], reward2: List[int], k: int) -> int:
        total = 0
        diff = []

        for i in range(len(reward1)):
            diff.append(reward1[i] - reward2[i])

        diff = sorted(diff, reverse = True)
        total = sum(reward2) + sum(diff[:k])


        return total 

# 1. 假设所有的芝士都分给 mice 2
# 2. 然后决定 i 个芝士分给 mice 1
# 3. create diff array: reward1[i] - reward2[i]
# 4. 逆序排序然后取数

# Time Complexity: O(n)
# Space Complexity: O(n)

# 优化版本
class Solution:
    def miceAndCheese(self, reward1: List[int], reward2: List[int], k: int) -> int:
        total = 0
   

        for i in range(len(reward1)):
            reward1[i] = (reward1[i] - reward2[i])

        reward1 = sorted(reward1, reverse = True)
        total = sum(reward2) + sum(reward1[:k])


        return total 
 
 # Time Complexity: O(n)
 # Space Complexity: O(1)
 