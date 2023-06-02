# Method 1:

from collections import defaultdict
class Solution:
    def judgeCircle(self, moves: str) -> bool:
        ref = defaultdict(int)


        for i in range(len(moves)):
            ref[moves[i]] += 1


        for key in ref.keys():
            if key == 'U':
                if ref[key] != ref['D']:
                    return False 

            elif key == 'D':
                if ref[key] != ref['U']:
                    return False 

            elif key == 'L':
                if ref[key] != ref['R']:
                    return False

            elif key == 'R':
                if ref[key] != ref['L']:
                    return False 

        return True 

# Time Complexity: O(n): n -> length of the string
# Space Complexity: O(4) -> O(1)

# Method 2:
from collections import defaultdict
class Solution:
    def judgeCircle(self, moves: str) -> bool:
        ref = defaultdict(int)


        for i in range(len(moves)):
            ref[moves[i]] += 1


        if ref.get('L', 0) != ref.get('R', 0) or ref.get('D', 0) != ref.get('U', 0):
            return False 
        return True 


