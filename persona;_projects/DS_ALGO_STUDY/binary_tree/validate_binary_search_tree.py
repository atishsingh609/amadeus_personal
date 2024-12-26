import math


class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """

        def comp(node, low, high):
            if not node:
                return True
            if not (low < node.val < high):
                return False

            ans = comp(node.left, low, node.val) and comp(node.right, node.val, high)

            return ans

        return comp(root, -math.inf, math.inf)