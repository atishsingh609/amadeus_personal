import math


class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def call_validate_fun(root: Node):

    validate_binary_search(-math.inf, root, math.inf)


def validate_binary_search(lower, root, upper):
    if root is None:
        return True
    if not(lower < root.val < upper):
        return False
    else:
        ans_1 = validate_binary_search(lower, root.left, root.val)
        ans_2 = validate_binary_search(root.val, root.right, upper)
        return ans_1 and ans_2