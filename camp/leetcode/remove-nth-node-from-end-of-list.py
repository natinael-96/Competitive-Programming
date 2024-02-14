# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head.next:
            return None
        fast = head
        slow = head

        while n:
            fast = fast.next
            n -= 1

        if not fast:
            return slow.next

        while fast.next:
            fast = fast.next

            if n > 0:
                n -= 1
            else:
                slow = slow.next
        
        slow.next = slow.next.next
        return head