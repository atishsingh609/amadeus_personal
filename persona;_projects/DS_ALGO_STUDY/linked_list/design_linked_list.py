class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


class MyLinkedList(object):

    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def get(self, index):
        """
        :type index: int
        :rtype: int
        """
        if index >= self.size:
            return -1
        temp = self.head
        while index > 0:
            temp = temp.next
            index -= 1
        return temp.val

    def addAtHead(self, val):
        """
        :type val: int
        :rtype: None
        """
        if self.head == None:
            self.head = self.tail = Node(val)
        else:
            self.head = Node(val, self.head)
        self.size += 1

    def addAtTail(self, val):
        """
        :type val: int
        :rtype: None
        """
        if not self.head:
            self.head = self.tail = Node(val)
        else:
            new_node = Node(val)
            self.tail.next = new_node
            self.tail = new_node
        self.size += 1

    def addAtIndex(self, index, val):
        """
        :type index: int
        :type val: int
        :rtype: None
        """
        if index > self.size:
            return -1
        if index == 0:
            self.addAtHead(val)
        elif index == self.size:
            self.addAtTail(val)
        else:
            current = self.head
            for _ in range(index - 1):
                current = current.next
            new_node = Node(val, current.next)
            current.next = new_node
            self.size += 1

    def deleteAtIndex(self, index):
        """
        :type index: int
        :rtype: None
        """

        if index < 0 or index >= self.size:
            return -1
        if index == 0:
            self.head = self.head.next
            if self.size == 1:  # If it was the only node
                self.tail = None
        else:
            current = self.head
            for _ in range(0, index - 1):
                current = current.next
            current.next = current.next.next
            if index == self.size - 1:
                self.tail = current

        self.size -= 1

# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)