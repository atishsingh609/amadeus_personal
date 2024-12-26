class Solution:

    def get_hight(self, root):

        if not root:
            return 0
        left_hight = self.get_hight(root.left)
        right_hight  = self.get_hight(root.right)
        ans = max(left_hight, right_hight) + 1
        return ans
