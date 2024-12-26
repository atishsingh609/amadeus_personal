"""
traverse a singly create link list
"""

"""
Below class NOde and LinkList is used to create a linkedlist. method insert, search and delete is being implemented.
"""


class Node:
    """
    A node in the link list has two attributes one is Data and the next refrence.
    """
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    """
    head - is to track the first element of link list
    tail - to track the newly created node.
    """
    def __init__(self):
        self.head = None
        self.tail = None

    def insert(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

    def search(self, value):
        ptr = self.head
        while ptr:
            if ptr.data == value:
                return "true"
            ptr = ptr.next
        return "false"

    def delete_node(self, value):
        ptr = self.head
        prev = None

        if ptr and ptr.data == value:
            self.head = ptr.next
            return
        while ptr and ptr.data != value:
            prev = ptr
            ptr = ptr.next
        prev.next = ptr.next

        if not ptr:
            return


linked_list = LinkedList()
linked_list.insert(1)
linked_list.insert(2)
linked_list.insert(3)

# linked_list.delete_node(2)
print("searching the value in liklist", linked_list.search(2))