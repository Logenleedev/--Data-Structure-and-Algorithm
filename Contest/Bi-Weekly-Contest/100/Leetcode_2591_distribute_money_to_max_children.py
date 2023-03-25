class Solution:
    def distMoney(self, money: int, children: int) -> int:
        money -= children

        if money < 0:
            return -1

        ans = min(children, money // 7) # ans number of children get 8 dollars
        children -= ans # remain this much of children who have only 1 dollar 
        money -= 7 * ans # remain this much of money


        # 分类讨论 (category discussion)
        if money != 0 and children == 0 or children == 1 and money == 3:
            ans -= 1

        return ans 

# Time Complexity: O(1)
# Space Complexity: O(1)