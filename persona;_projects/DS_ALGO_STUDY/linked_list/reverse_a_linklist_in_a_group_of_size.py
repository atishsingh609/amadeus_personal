"""
Given a linked list, reverse the nodes of a linked list k at a time and return its modified list in Time Complexity O(n).

"""

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None


def reverse_linked_list(head: Node, k: int):
    cur: Node = head
    prev = None
    next = None
    count = 0
    while count < k and cur:
        next = cur.next
        cur.next = prev
        prev = cur
        cur = next
        count = count + 1
    if next != None:
        head.next = reverse_linked_list(next, 3)
    return prev

