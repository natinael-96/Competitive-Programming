# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        dummy = ListNode()  
        dummy.next = head
        current = head.next
        sorted_tail = head

        while current:
            next_node = current.next

            if current.val < sorted_tail.val:
                prev, temp = dummy, dummy.next

                while temp and temp.val < current.val:
                    prev, temp = temp, temp.next

                prev.next = current
                current.next = temp
                sorted_tail.next = next_node
            else:
                sorted_tail = current

            current = next_node

        return dummy.next
