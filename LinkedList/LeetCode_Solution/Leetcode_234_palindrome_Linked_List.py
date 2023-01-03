#n Method 1: traversal 


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        stack = []

        cur = head 

        while cur != None:
           
            stack.append(cur.val)
            cur = cur.next
            
        return stack == stack[::-1]



# Method 2: stack 
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        stack = []

        cur = head 

        while cur != None:
           
            stack.append(cur.val)
            cur = cur.next

        cur = head 

        while cur != None:
            if cur.val != stack.pop():
                return False
            cur = cur.next 
            
        return True 



