# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeZeroSumSublists(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(next=head)
        preSm = 0
        dicT = {preSm: dummy}

        while head:
            preSm += head.val

            if preSm in dicT:
                pntr = dicT[preSm].next
                temp = preSm

                while pntr is not head:
                    temp += pntr.val
                    pntr = pntr.next
                    dicT.pop(temp)

                dicT[preSm].next = head.next
                
            else:
                dicT[preSm] = head

            head = head.next

        return dummy.next
