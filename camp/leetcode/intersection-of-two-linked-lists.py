# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        
        if headA == headB:
            return headA
        
        dummy1 = headA
        dummy2 = headB

        lengA = 1
        lengB = 1

        while dummy1 and dummy1.next:
            lengA += 1
            dummy1 = dummy1.next

        while dummy2 and dummy2.next:
            lengB += 1
            dummy2 = dummy2.next

        n = abs(lengA - lengB)
        dum1 = headA
        dum2 = headB

        while n and dum1 and dum2:
            n -= 1
            if lengA > lengB:
                dum1 = dum1.next
            else:
                dum2 = dum2.next

        while dum1 and dum2:
            if dum1 == dum2:
                return dum2
            dum1 = dum1.next
            dum2 = dum2.next
        return None
