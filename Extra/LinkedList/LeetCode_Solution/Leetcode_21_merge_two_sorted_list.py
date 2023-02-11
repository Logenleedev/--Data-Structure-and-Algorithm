# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        curA = list1
        curB = list2

        dummyhead = ListNode(next = None)
        cur = dummyhead


        # 分类讨论
        # 1. curA != None and curB != None
        # 2. curA == None and curB != None
        # 3. curA != None and curB == None
        while curA or curB:
            if curA and curB:
                if curB.val >= curA.val:
                    cur.next = curA
                    cur = cur.next
                    curA = curA.next
                elif curA.val >= curB.val:
                    cur.next = curB
                    cur = cur.next 
                    curB = curB.next 
            else:
                if curA:
                    cur.next = curA
                    cur = cur.next
                    curA = curA.next 
                else:
                    cur.next = curB
                    cur = cur.next
                    curB = curB.next 
        
        return dummyhead.next 

# Time Complexity: O(m + n)
# Time Complexity: O(m + n)