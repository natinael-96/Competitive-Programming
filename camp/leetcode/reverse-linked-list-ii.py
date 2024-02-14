# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        
        if left == right:
            return head
        dummy = ListNode()
        dummy.next = head
        prev = dummy
        curr = head
        cnt = 0

        #find the left
        while prev and curr and cnt < left-1:
            prev = prev.next
            curr = curr.next
            cnt += 1


        revStr = prev.next
        revEnd = curr
        prev.next = None

        while curr and cnt < right :
            nxtNode = curr.next
            curr.next = prev.next
            prev.next = curr
            curr = nxtNode
            cnt += 1

        #connect to teh rest
        revStr.next = curr
        return dummy.next
