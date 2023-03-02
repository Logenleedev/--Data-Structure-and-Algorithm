from collections import deque
class Solution:

    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        if root == None:
            return []

        count = 0

        que = deque([root])
        results = []

        while que:

            size = len(que)
            result = []

            for _ in range(size):
                node = que.popleft()
                result.append(node.val)

                if node.left:
                    que.append(node.left)

                if node.right:
                    que.append(node.right)
            
            if count % 2 != 0:
                results.append(result[::-1])
            else:
                results.append(result)
            count += 1

        return results

# Time Complexity: O(n)
# Space Complexiy: O(n)
