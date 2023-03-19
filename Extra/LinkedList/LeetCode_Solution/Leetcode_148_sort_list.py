# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        # append value in a list 

        value = []

        cur = head 

        while cur:
            value.append(cur.val)
            cur = cur.next 

        value = sorted(value)

        # create dummyhead 

        dummyhead = ListNode(next = None)
        cur_2 = dummyhead

        for i in range(len(value)):
            cur_2.next = ListNode(val = value[i])
            cur_2 = cur_2.next 

        return dummyhead.next 


# Time Complexity: O(n)
# Space Complexity: O(n)