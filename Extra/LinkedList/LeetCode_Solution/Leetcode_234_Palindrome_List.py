class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        ref = []

        cur = head 

        while cur:
            ref.append(cur.val)

            cur = cur.next

        if ref == ref[::-1]:
            return True 
        return False 

# Time Complexity: O(n)
# Space Complexity: O(n)