# 测试斜率
# 如果有两个那么显然 return True
# else 根据前两个点推断是否在同一个线上

class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        x0, y0 = coordinates[0][0], coordinates[0][1]
        x1, y1 = coordinates[1][0], coordinates[1][1]

        for coordinate in coordinates:
            x, y = coordinate[0], coordinate[1]
            if (y - y0) * (x1 - x0) != (y1 - y0) * (x - x0) :
                return False 

        return True
# Time Complexity: O(n)
# Space Complexity: O(1)