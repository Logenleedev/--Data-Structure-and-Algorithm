class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        longest_substring = -1 

        # 用 set 记录答案防止重复
        res = set()

        
        def dfs(string, cur_idx, cur_res, l_count, r_count):
            # modify the variable 
            nonlocal res, longest_substring

            # 如果 cur idx == len(s) base case 
            if cur_idx >= len(s):
                # double check the left and right 括号数量一样
                if l_count == r_count:
                    # 更新长度
                    if len(cur_res) > longest_substring:
                        longest_substring = len(cur_res)
                        res = set()
                        res.add(''.join(cur_res))
                    elif len(cur_res) == longest_substring:
                        res.add(''.join(cur_res))
            # 如果还没有到
            else:
                cur_char = string[cur_idx]

                # 情况1：左括号
                if cur_char == '(':
                    # 用左括号
                    cur_res.append(cur_char)
                    dfs(string, cur_idx + 1, cur_res, l_count + 1, r_count)
                    cur_res.pop()

                    # 用右括号
                    dfs(string, cur_idx + 1, cur_res, l_count, r_count)

                # 情况2：右括号
                elif cur_char == ')':
                    # 用右括号
                    if l_count > r_count:
                        # 注意这里左括号大于右括号的时候才有意义。如果是 ））那基本就不用看了
                        cur_res.append(cur_char)
                        dfs(string, cur_idx + 1, cur_res, l_count, r_count + 1)
                        cur_res.pop()
                
                    # 不用右括号
                    dfs(string, cur_idx + 1, cur_res, l_count, r_count)
                    
                # 情况3：字母
                else:
                    cur_res.append(cur_char)
                    dfs(string, cur_idx + 1, cur_res, l_count, r_count)
                    cur_res.pop()






        dfs(s, 0,[], 0, 0)

        return list(res)