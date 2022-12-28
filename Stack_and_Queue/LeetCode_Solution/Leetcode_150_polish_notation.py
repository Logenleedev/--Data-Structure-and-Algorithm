class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        ans = []
        for item in tokens:
            if item not in {"+", "-", "*", "/"}:
                ans.append(item)
            else:
                first_item, second_item = ans.pop(), ans.pop()

                temp = int(eval(f'{second_item} {item} {first_item}'))

                ans.append(temp)
        return int(ans.pop())
