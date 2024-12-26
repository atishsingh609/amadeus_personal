class Node:
    """
    this class will create a node having value as value and address of next node as null.
    """
    def __init__(self, value):
        self.value = value
        self.next = None

"""
insertion at head 
"""


def insertion_at_head(head : Node, value):
    temp = Node(value)
    temp.next = head
    head = temp
    return head


def insert_at_tail(tail: Node, value):
    temp = Node(value)
    tail.next = temp
    tail = temp
    return tail

def insert_at_position(head, position, value):

    temp = head
    count = 1
    while count < position-1:
        temp = temp.next
        count = count + 1
    new_node = Node(value)
    new_node.next = temp.next
    temp.next = new_node
    return head


def deleteNode(head, position):
    if position == 1:
        head = head.next
    else:
        cur = head
        prev =  None
        count = 1
        while count < position:
            prev = cur
            cur = cur.next
            count = count + 1
        prev.next = cur.next

    return head

def print_nodes(head:Node):
    temp = head
    while temp:
        print(temp.value)
        temp = temp.next


head = Node(5)
# head = insertion_at_head(head_1, 10)
# head = insertion_at_head(head, 12)
# head = insertion_at_head(head, 14)
# head = insertion_at_head(head, 16)
# head = insertion_at_head(head, 18)
# head = insertion_at_head(head, 20)

tail = head
tail = insert_at_tail(tail, 10)
tail = insert_at_tail(tail, 12)
tail = insert_at_tail(tail, 14)
tail = insert_at_tail(tail, 16)
tail = insert_at_tail(tail, 18)

insert_at_position(head, 3, 100)
# deleteNode(head, 3)
# deleteNode(head, 4)
# deleteNode(head, 5)
# deleteNode(head, 6)
# deleteNode(head, 7)
head = deleteNode(head, 1)
print_nodes(head)



