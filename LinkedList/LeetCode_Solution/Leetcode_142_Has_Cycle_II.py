# Method 1: Hash map set


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        ref = set()

        current = head

        while current != None:
            ref.add(current)
            if current.next in ref:
                return current.next
            current = current.next 
            
        return None

# Method 2: two pointer 

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow, fast = head, head

        while fast != None and fast.next != None:
           
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                p = head 
                q = slow
                while p != q:
                    p = p.next
                    q = q.next 
                return p
        return None

