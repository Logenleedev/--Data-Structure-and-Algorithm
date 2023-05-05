## Method 1: Brute force

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        temp = []

        for i in range(len(lists)):
            cur = lists[i]

            while cur != None:

                temp.append(cur.val)

                cur = cur.next 
        sorted_temp = sorted(temp)
        pointer = 0 

        dummyhead = ListNode()
        cur = dummyhead

        while pointer < len(sorted_temp):
            
            cur.next = ListNode(val = sorted_temp[pointer])

            pointer += 1
            cur = cur.next 

        return dummyhead.next 
        
# n -> list length 
# m -> average number of node per list element 
# Time Complexity: O(m * n)
# Space Complexity: O(m + n)



# Method 2: heap

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import heapq

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []
        
        for i in range(len(lists)):
            cur = lists[i]

            while cur != None:

                heapq.heappush(heap, cur.val)

                cur = cur.next 

        dummyhead = ListNode()
        cur = dummyhead

        while heap:
            
            cur.next = ListNode(val = heapq.heappop(heap))

            cur = cur.next 

        return dummyhead.next 
        
        
# n -> list length 
# m -> average number of node per list element 
# Time Complexity: O((mn)log(m * n))
# Space Complexity: O(m + n)

        