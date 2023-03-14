# Method 1: Brute force

class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        current = head

        while current != None and current.next != None:
            if current.val == current.next.val:
                temp = current.next.next
                current.next = temp
                
            else:
                current = current.next 

        return head



# Method 2: Double pointer 
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None:
            return head 

        slow = head
        fast = head


        while fast != None:
            if fast.val != slow.val:
                slow.next = fast
                slow = slow.next 

            fast = fast.next
        slow.next = None
        return head 