```python
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        ans = [0] * len(temperatures)
        stack = []

        for i in range(len(temperatures)): 
            # 判断个子高矮
            while len(stack) > 0 and temperatures[i] > temperatures[stack[-1]]:
                (operation based on the problem setup)
                # 矮个子的走开
                stack.pop()
            # 高个子您请进
            stack.append(i)

        return ans 
```