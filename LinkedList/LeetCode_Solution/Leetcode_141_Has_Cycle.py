# Method 1 - Brute Force 
################################################################
# Time Complexity: O(n)
# Space Complexity: O(n)
################################################################


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:

            
            node_list = set()
    
            while (head != None):
                if (head in node_list):
                    return True
                node_list.add(head)
                head = head.next
            return False

# Method 2 - Fast Slow Pointer
################################################################
# Time Complexity: O(n)
# Space Complexity: O(1)
################################################################
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:

            slow, fast = head, head

            while fast and fast.next:
                slow = slow.next
                fast = fast.next.next
                if slow == fast:
                    return True
                
            return False