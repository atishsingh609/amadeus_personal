class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root is None:
            return True
        left = self.isBalanced(root.left)
        right = self.isBalanced(root.right)

        diff = abs(self.hight(root.left) - self.hight(root.right)) <= 1

        if left and right and diff:
            return 1
        else:
            return False

    def hight(self, root):
        if root is None:
            return 0
        left = self.hight(root.left)
        right = self.hight(root.right)
        ans = max(left, right) + 1
        return ans