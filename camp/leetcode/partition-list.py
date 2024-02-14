# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        
        before = ListNode(0)
        after = ListNode(0)

        bfrDumm, aftDumm = before,after

        while head:
            if head.val < x:
                bfrDumm.next = head
                bfrDumm = head
            else:
                aftDumm.next = head
                aftDumm = head
            head = head.next
        aftDumm.next = None

        bfrDumm.next = after.next

        return before.next