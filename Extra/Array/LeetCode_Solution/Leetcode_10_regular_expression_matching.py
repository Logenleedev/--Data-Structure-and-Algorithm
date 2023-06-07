class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        
        cache = {}

        def dfs(i, j, s, p):
            if (i, j) in cache:
                return cache[(i, j)] 
            if i >= len(s) and j >= len(p):
                return True 
            if j >= len(p):
                return False 

            match = i < len(s) and (s[i] == p[j] or p[j] == '.')
            if (j + 1) < len(p) and p[j + 1] == '*':
                # (i , j + 2) -> 用 *
                # (i + 1, j) -> 不用 * 
                cache[(i, j)] = (dfs(i, j + 2, s, p) or (match and dfs(i + 1, j, s, p)))
                return cache[(i, j)]
            
            if match:
                cache[(i, j)] = dfs(i + 1, j + 1, s, p)
                return cache[(i, j)]

            cache[(i, j)] = False
            return False 

        return dfs(0, 0, s, p)

# Time Complexity: O(m + 2^n)
# Space Complexity: O(m + n)