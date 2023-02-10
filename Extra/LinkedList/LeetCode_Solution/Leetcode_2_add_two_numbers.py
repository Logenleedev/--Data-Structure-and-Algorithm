# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        ref1 = []
        ref2 = [] 

        cur1 = l1
        cur2 = l2
        # iterate list 1
        while cur1:
            ref1.append(str(cur1.val))
            cur1 = cur1.next

        # iterate list 2
        while cur2:
            ref2.append(str(cur2.val))
            cur2 = cur2.next
        
        num1 = int("".join(ref1)[::-1])
        num2 = int("".join(ref2)[::-1])

        result = list(str(num1 + num2))
        result = result[::-1]


        head = ListNode(int(result[0]))
        cur3 = head
        pointer = 1

        while pointer < len(result):
            cur3.next = ListNode(int(result[pointer]))
            pointer += 1
            cur3 = cur3.next 

        return head 
            

