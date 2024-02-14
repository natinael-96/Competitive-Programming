# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        oddHead = ListNode()
        odd = oddHead
        evenHead = ListNode()
        even = evenHead
        cnt = 1
        while head:
            if cnt % 2 == 1:

                odd.next = head
                odd = odd.next
            else:
                even.next = head
                even = even.next
            
            head = head.next
            cnt += 1
        odd.next = evenHead.next
        even.next = None
        return oddHead.next
        
            