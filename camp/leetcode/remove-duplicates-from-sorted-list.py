class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head

        current = head

        while current and current.next:
            next_distinct = current.next

            while next_distinct and current.val == next_distinct.val:
                next_distinct = next_distinct.next

            current.next = next_distinct
            current = next_distinct

        return head
