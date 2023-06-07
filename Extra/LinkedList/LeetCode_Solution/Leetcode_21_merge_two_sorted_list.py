# Brute Force
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

# heap

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import heapq
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        pri_que = []

        cur = list1

        while cur:
            heapq.heappush(pri_que, cur.val)
            cur = cur.next 

        cur = list2

        while cur:
            heapq.heappush(pri_que, cur.val)
            cur = cur.next 

        pointer = 0     

        dummy = ListNode()
        cur = dummy 

        while pri_que:
            element = heapq.heappop(pri_que)
            cur.next = ListNode(element)
            pointer += 1
            cur = cur.next 

        return dummy.next 

# Time Complexity: O((n + m)* log(n + m))
# Space Complexity: O((n + m))