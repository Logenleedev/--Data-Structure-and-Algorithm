# Method 1 - Brute Force 

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        current = head
        while(current != None):
            temp = current.next
            current.next = prev
            prev = current
            current = temp
        return prev

# Method 2 - Recursion 
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        

        def reverse(pre,cur):
            if not cur:
                return pre
                
            tmp = cur.next
            cur.next = pre

            return reverse(cur,tmp)
        
        return reverse(None,head)

# Time Complexity: O(n)
# Space Complexity: O(1)