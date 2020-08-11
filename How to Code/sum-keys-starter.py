# PROBLEM:

# Design a function that consumes a BST and produces the sum of all
# the keys in the BST.

class Node:

    def __init__(self, key, val, l, r):
        self.key = key
        self.val = val
        self.l = l
        self.r = r

BST0 = False
BST1 = Node(1, "abc", False, False)
BST4 = Node(4, "dcj", False, Node(7, "ruf", False, False))
BST3 = Node(3, "ilk", BST1, BST4)
BST42 = Node(42, "ily",
            Node(27, "wit", Node(14, "olp", False, False), False),
            False)
BST10 = Node(10, "why", BST3, BST42)

def bstsum(bst):
    if not bst:
        return 0
    return bst.key + bstsum(bst.l) + bstsum(bst.r)

assert bstsum(BST1) == 1
assert bstsum(BST4) == 11
assert bstsum(BST3) == 15
assert bstsum(BST42) == 83
assert bstsum(BST10) == 108
print("passed")