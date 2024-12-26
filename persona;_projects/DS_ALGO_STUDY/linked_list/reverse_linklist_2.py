"""
92. Reverse Linked List II
Medium
Topics
Companies
Given the head of a singly linked list and two integers left and right where left <= right, reverse the nodes of the list from position left to position right, and return the reversed list.



Example 1:


Input: head = [1,2,3,4,5], left = 2, right = 4
Output: [1,4,3,2,5]
Example 2:

Input: head = [5], left = 1, right = 1
Output: [5]
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:

        dummy_node = ListNode(0, head)

        left_prev, cur = dummy_node, head
        for i in range(left-1):
            left_prev, cur = cur, cur.next
        #left_prev point to node previous to left.
        # cur now point to left node, from where reverse operation will start
        prev = None
        # right - left +1 = 4-2 + 1 = 3 --> 3 nodes to reverse
        for i in range(right-left+1):
            temp = cur.next
            cur.next = prev
            prev = cur
            cur = temp
        # now left node point still pointing to none, so need to change it.
        # it should now point to right which is cur node in this case.
        # left_prev should point to node just before right which is prev node.

        left_prev.next.next = cur
        left_prev.next = prev
        return dummy_node.next