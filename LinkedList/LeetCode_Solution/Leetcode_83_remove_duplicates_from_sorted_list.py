# Time Complexity: O(n)
# Space Complexity: O(1)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        current = head

        while current != None and current.next != None:
            if current.val == current.next.val:
                temp = current.next.next
                current.next = temp
                
            else:
                current = current.next 

        return head
