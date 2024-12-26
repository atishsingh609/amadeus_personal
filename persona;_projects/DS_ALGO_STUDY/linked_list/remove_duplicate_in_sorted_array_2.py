"""
82. Remove Duplicates from Sorted List II
Medium
Topics
Companies
Given the head of a sorted linked list, delete all nodes that have duplicate numbers, leaving only distinct numbers from the original list. Return the linked list sorted as well.



Example 1:


Input: head = [1,2,3,3,4,4,5]
Output: [1,2,5]
Example 2:


Input: head = [1,1,1,2,3]
Output: [2,3]


"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy_node = ListNode(-1, head)
        cur, prev = head, dummy_node

        while cur:
            while cur.next and cur.val == cur.next.val:
                cur = cur.next
            if prev.next == cur:
                prev = prev.next
                cur = cur.next
            else:
                prev.next = cur.next
                cur = prev.next
        return dummy_node.next

