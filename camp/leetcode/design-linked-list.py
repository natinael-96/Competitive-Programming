class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


class MyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0
        

    def get(self, index: int) -> int:
        if index >= self.length:
            return -1
        
        cur = self.head
        while index:
            cur = cur.next
            index -= 1
        return cur.val
        
    def addAtHead(self, val: int) -> None:
        dummy = Node(val)
        self.head, dummy.next = dummy, self.head
        if not self.tail:
            self.tail = self.head

        self.length += 1
        

    def addAtTail(self, val: int) -> None:
        dummy = Node(val)
        if self.head:
            self.tail.next, self.tail = dummy, dummy
        else:
            self.head = self.tail = dummy

        self.length += 1

    def addAtIndex(self, index: int, val: int) -> None:
        if index > self.length:
            return
        elif index == self.length:
            self.addAtTail(val)
        elif index == 0:
            self.addAtHead(val)
        else:
            cur = self.head
            index -= 1
            while index:
                cur = cur.next
                index -= 1

            dummy = Node(val)
            cur.next, dummy.next = dummy, cur.next

            self.length += 1
        

    def deleteAtIndex(self, index: int) -> None:
        if index >= self.length:
            return
        elif index == 0:
            self.head = self.head.next
        else:
            cur = self.head
            i = index - 1
            while i:
                cur = cur.next
                i -= 1
        
            cur.next = cur.next.next
            if index == self.length - 1:
                self.tail = cur

        self.length -= 1
        if self.length == 0:
            self.head = self.tail = None


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)