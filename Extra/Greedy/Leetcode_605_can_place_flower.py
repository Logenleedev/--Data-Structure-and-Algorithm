class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        flowerbed = [0] + flowerbed + [0]

        # 大体思路：只要碰到 [0, 0, 0] 就栽花就可以了
        count = 0 
        for i in range(len(flowerbed)):
            # 如果碰到花
            if flowerbed[i] == 1:
                # count 清 0 
                count = 0 
            # 如果碰到花盆
            elif flowerbed[i] == 0:
                # if a = [0, 0, 0], then we can plant a flower at a[1]
                # notice count = 3 in a[2]. Therefore count need to be cleared to 1 instead of 0 
                count += 1
                if count == 3:
                    
                    n -= 1
                    count = 1


        return True if n <= 0 else False 
# Time Complexity: O(n)
# Space Complexity: O(1)