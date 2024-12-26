class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def take_inputs(root):
    input_num = input("Enter yout input: ")
    for i in input_num.split(","):
        root = insert_into_BST(root, int(i))
    return root


def insert_into_BST(root, input_num: int):
    if root is None:
        root = Node(input_num)
        return root

    if input_num < root.val:
        root.left = insert_into_BST(root.left, input_num)
    if input_num > root.val:
        root.right = insert_into_BST(root.right, input_num)
    return root


def inorder_traversal(root):
    if not root:
        return
    inorder_traversal(root.left)
    print(root.val)
    inorder_traversal(root.right)



roots = None
root = take_inputs(roots)

inorder_traversal(root)


"""

Same Solution can be used to insert any value if BST already exit


"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:

        if root is None:
            root = TreeNode(val)
            return root
        if val > root.val:
            root.right = self.insertIntoBST(root.right, val)
        if val < root.val:
            root.left = self.insertIntoBST(root.left, val)
        return root 