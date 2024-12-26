"""
Given : 4 ----> 5 ------>6 ----->8
output: 8 ---->6------->5  ------>4
"""

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def reverse_linked_list(head: Node):
    """
    Need to assign the removed linked to temp before removing it.
    :param head:
    :return:
    """
    current = head
    prev = None
    while current:
        temp = current.next
        current.next = prev
        prev = current
        current = temp
    return prev
