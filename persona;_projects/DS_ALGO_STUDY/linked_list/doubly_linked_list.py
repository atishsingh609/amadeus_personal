class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None


def print_linkedlist(head):
    temp = head
    while temp:
        print(temp.value, end=" ")
        temp = temp.next
    print(end="\n")


def len_of_linedlist(head):
    temp = head
    len = 0
    while temp:
        len+=1
        temp = temp.next
    return len


def insert_at_head(head, value):

    temp = Node(value)
    temp.next = head
    head.prev = temp
    head = temp
    return head


def insert_at_tail(tail, value):
    temp = Node(value)
    temp.prev = tail
    tail.next = temp
    tail = temp
    return tail


def insert_at_position(head, tail, position, value):

    """

    """
    temp = head
    node_to_insert = Node(value)
    if position == 1:
        head = insert_at_head(head, value)
    else:
        count = 1
        while count < position -1:
            temp = temp.next
            count+=1
        if temp.next is None:
            tail = insert_at_tail(tail, value)
        else:
            node_to_insert.next = temp.next
            temp.next.prev = node_to_insert
            temp.next = node_to_insert
            node_to_insert.prev = temp

    return head, tail


def delete_node(head, position):


    temp = head
    if position == 1:
        temp.next.prev = None
        head = temp.next
        temp.next = None
    else:
        count = 1
        cur = head
        prev = None
        while count < position:
            prev = cur
            cur = cur.next
            count += 1
        prev.next = cur.next
        cur.next.prev = cur.prev
        cur.prev = None
        cur.next = prev
    return head



head = tail = Node(10)
head = insert_at_head(head, 20)
head = insert_at_head(head, 30)
head = insert_at_head(head, 40)
head = insert_at_head(head, 50)
# tail = head_1
# tail = insert_at_tail(tail, 60)
# tail = insert_at_tail(tail, 70)
# tail = insert_at_tail(tail, 80)
# tail = insert_at_tail(tail, 90)
# tail = insert_at_tail(tail, 100)

head, tail = insert_at_position(head, tail, 3, 150)
head, tail = insert_at_position(head, tail, 4, 151)
head, tail = insert_at_position(head, tail, 5, 152)
head, tail = insert_at_position(head, tail, 6, 153)
head, tail = insert_at_position(head, tail, 7, 154)
head, tail = insert_at_position(head, tail, 8, 155)
head, tail = insert_at_position(head, tail, 9, 156)
head, tail = insert_at_position(head, tail, 10, 157)
head, tail = insert_at_position(head, tail, 14, 158)
print("before delete")
print_linkedlist(head)
print("len of linked list is ", len_of_linedlist(head))
print("head", head.value)
print("tail", tail.value)
head = delete_node(head, 4)
print("after delete at position 4")
print_linkedlist(head)
print("len of linked list is ", len_of_linedlist(head))
print("head", head.value)
print("tail", tail.value)
