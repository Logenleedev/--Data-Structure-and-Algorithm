# Brute Force
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        ans = [0] * len(temperatures)


        for i in range(len(temperatures) - 1):
            for j in range(i + 1, len(temperatures)):
                if temperatures[j] > temperatures[i]:
                    ans[i] = j - i 
                    break

        return ans 

# Mono
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        ans = [0] * len(temperatures)
        stack = []

        for i in range(len(temperatures)):
            while len(stack) > 0 and temperatures[i] > temperatures[stack[-1]]:
                # 只要是比栈口元素要大的话
                # 记录答案
                # i - stack[-1] 表示隔着的天数
                ans[stack[-1]] = i - stack[-1]
                # 单调栈是记录已经遍历的元素，没有必要保留了
                stack.pop()
            stack.append(i)

        return ans 

