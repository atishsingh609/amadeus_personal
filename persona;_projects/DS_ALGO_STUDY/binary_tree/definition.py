"""
Binary Tree is defined as a Tree data structure with at most 2 children. Since each element in a binary tree can have
only 2 children, we typically name them the left and right child.
common terms:
root,
parent,
child,
leaf node : node which does not have any child node
internal node - Nodes other than leaf node.

Binary Search Tree:
Binary search tree is a pattern in which all the left node has lower value than the parent node and all right nodes
have higher values than parent nodes.



"""

class Node:
    def __init__(self, val):
        self.left = self.right = None
        self.val = val


def build_tree(root: Node):
    print("enter data ")
    data = int(input())
    root  = Node(data)
    if data == -1:
        return
    print(f"Enter data to insert left of {data} ")
    build_tree(root.left)
    print(f"Enter data to insert right of {data} ")
    build_tree(root.right)
    return root



root = Node(1)

root = build_tree(root)

# root = Node(1)
# root.left = Node(2)
# root.right = Node(3)
# root.left.left = Node(4)

"""
Traversals of a binary tree

"""



def traversals(node):
    if node == None:
        return
    print(node.val)
    traversals(node.left)
    traversals(node.right)

traversals(root)


