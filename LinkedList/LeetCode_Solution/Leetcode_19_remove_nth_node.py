# Time Complexity: O(n)
# Space Complexity: O(1)


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummyhead = ListNode(next = head)
        slow, fast = dummyhead, dummyhead

        while n >= 0:
            fast = fast.next
            n -= 1
        
        while fast != None:
            fast = fast.next
            slow = slow.next

        slow.next = slow.next.next

        return dummyhead.next