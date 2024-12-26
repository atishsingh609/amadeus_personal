class Solution:
    """

    Inorder trasversal represented by LNR - left print right
    """
    ans = []

    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        lis = []
        self.helper(root, lis)
        return lis

    def helper(self, root, lst):
        if root is None:
            return
        self.helper(root.left, lst)
        lst.append(root.val)
        self.helper(root.right, lst)