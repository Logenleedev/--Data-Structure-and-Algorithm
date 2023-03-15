# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        dummy_small = ListNode(next = None)
        cur_small = dummy_small

        dummy_big = ListNode(next = None)
        cur_big = dummy_big

        cur = head 

        while cur != None:
            if cur.val < x:
                cur_small.next = cur
                cur_small = cur_small.next 
            else:
                cur_big.next = cur 
                cur_big = cur_big.next 
            
            cur = cur.next 
        
        cur_small.next = dummy_big.next 
        # 很重要的一步！要不然链表有可能成环
        cur_big.next = None
        
        return dummy_small.next 
        
