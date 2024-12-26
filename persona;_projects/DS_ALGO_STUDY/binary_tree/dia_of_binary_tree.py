class Solution(object):

    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0
        opt1 = self.diameterOfBinaryTree(root.left)
        opt2 = self.diameterOfBinaryTree(root.right)
        opt3 = self.hight(root.left) + self.hight(root.right)
        ans = max(opt1, opt2, opt3)
        return ans

    def hight(self,root):
        if root is None:
            return 0
        left = self.hight(root.left)
        right = self.hight(root.right)
        ans = max(left, right) + 1
        return ans