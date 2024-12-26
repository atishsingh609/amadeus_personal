""""
For a doubly linked list, the one Node has refrence of two Nodes i.e next Node as well as Previous None.
"""


class Node:
    def __init__(self, data):
        self.data = data
        self.previous = None
        self.next = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_node(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = self.tail = new_node
            self.head.previous = None
            self.tail.next = None
        else:
            self.tail.next = new_node
            new_node.previous = self.tail
            self.tail = new_node
            self.tail.next = None

    def search_node(self, value):
        ptr = self.head
        if not ptr:
            return "Node does not exit"
        while ptr:
            if ptr.data == value:
                return "Node found"
            ptr = ptr.next
        return "Node does not Exist"

    def delete_node(self, value):
        ptr = self.head
        if not ptr:
            print("Doubly linked list is empty")
            return
        while ptr:
            if ptr.data == value:

                if ptr == self.head:
                    self.head = ptr.next
                    return
                if ptr.next != None:
                    ptr.next.previous = ptr.previous
                if ptr.previous !=None:
                    ptr.previous.next = ptr.next
                break
            ptr = ptr.next





d_l_l = DoublyLinkedList()
d_l_l.add_node(1)
d_l_l.add_node(2)
d_l_l.add_node(3)

# d_l_l.delete_node(1)
print("searching nodes in doubly linked list", d_l_l.search_node(1))
