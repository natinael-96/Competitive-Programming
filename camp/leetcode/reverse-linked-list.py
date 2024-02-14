# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        rev = None
        dummy = head

        while dummy:
            nxtNod = dummy.next
            dummy.next = rev
            rev = dummy
            dummy = nxtNod
        return rev




            