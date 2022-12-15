# Method 1: Hash


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:


        currentA = headA
        currentB = headB

        ref = set()

        while currentA != None:
            ref.add(currentA)
            currentA = currentA.next
        
        while currentB != None:
            if currentB in ref:
                return currentB
            else:
                currentB = currentB.next
        
        return None

# Method 2: double pointer
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:


        currentA = headA
        currentB = headB

        A_length = 0
        B_length = 0

        while currentA != None:
            A_length += 1
            currentA = currentA.next

        while currentB != None:
            B_length += 1
            currentB = currentB.next
        
        curA, curB = headA, headB
        if B_length > A_length:
            n = (B_length - A_length)
            while n > 0 and curB != None:
                curB = curB.next
                n -= 1
            while curA != None and curB != None:
                if curA == curB:
                    return curA
                else:
                    curA = curA.next
                    curB = curB.next
            return None
        else: 
            n = (A_length - B_length)
            while n > 0 and curA != None:
                curA = curA.next
                n -= 1

            while curA != None and curB != None:
                if curA == curB:
                    return curA
                else:
                    curA = curA.next
                    curB = curB.next
            return None
        
