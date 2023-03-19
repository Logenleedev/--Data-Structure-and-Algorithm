# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:

        
        dummyhead = ListNode(next=head)
        current = dummyhead 

        while current.next != None:
            if current.next.val == val:
                current.next = current.next.next
            
                 
            else:
                current = current.next 
        return dummyhead.next

# Recursion

class Solution:
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        if head is None:
            return None
        head.next = self.removeElements(head.next, val)
        return head.next if head.val == val else head

                        