# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def list_to_num_str(self, l, num_str):
        cur = l

        while cur:
            num_str += str(cur.val)
            cur = cur.next 
        # reverse the number 
        return num_str[::-1]

    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # 添加/删除链表常规操作

        dummyhead = ListNode()

        cur = dummyhead



        num_1 = ""
        num_2 = ""

        num_1 = self.list_to_num_str(l1, num_1)
        num_2 = self.list_to_num_str(l2, num_2)
        total = int(num_1) + int(num_2)
        # find the sum and then reverse the number 
        total_str = str(total)[::-1]

        i = 0 

        # create the linked list 
        while i < len(total_str):
            cur.next = ListNode(val = int(total_str[i]))
            cur = cur.next 
            i += 1

        return dummyhead.next 




# Time Complexity: O(len(l1) + len(l2))
# Space Complexity: O(len(l1) + len(l2))