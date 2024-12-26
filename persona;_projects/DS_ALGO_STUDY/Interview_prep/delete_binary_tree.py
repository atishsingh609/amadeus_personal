# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:

        if not root:
            return root
        elif root.val > key:
            root.left = self.deleteNode(root.left, key)
        elif root.val < key:
            root.right = self.deleteNode(root.right, key)
        else:
            # delete logic
            # case 1 no child node
            if root.left is None and root.right is None:
                root = None
            elif root.left and root.right is None:
                root = root.left

            elif root.left is None and root.right:
                root = root.right

            else:
                # mini = self.get_min(root.right).val
                # root.val = mini
                # root.right = self.deleteNode(root.right, mini)
                max = self.get_max(root.left).val
                root.val = max
                root.left = self.deleteNode(root.left, max)
        return root

    def get_min(self, root):
        temp = root
        while temp.left:
            temp = temp.left
        return temp

    def get_max(self, root):
        temp = root
        while temp.right:
            temp = temp.right
        return temp