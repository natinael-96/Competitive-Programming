# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        
        fast = head
        slow = head

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        rev = None
        cur = slow

        while cur:
            nxt = cur.next
            cur.next = rev
            rev = cur
            cur = nxt
        
        while rev:
            if head.val != rev.val:
                return False
            head = head.next
            rev = rev.next
        return True

        
