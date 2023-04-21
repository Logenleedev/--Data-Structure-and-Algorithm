# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def __init__(self):
        self.res = []
    def reversePrint(self, head: ListNode) -> List[int]:
        if head == None:
            return []

        self.reversePrint(head.next)
        self.res.append(head.val)
        return self.res 

# Time Complexity: O(n)
# Space Complexity: O(n)