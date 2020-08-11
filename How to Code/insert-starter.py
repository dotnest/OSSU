# PROBLEM:

# Design a function that consumes an Integer, String and BST, and adds a node
# that has the given key and value to the tree. The node should be inserted in 
# the proper place in the tree. The function can assume there is not already 
# an entry for that number in the tree. The function should produce the new BST.

# Do not worry about keeping the tree balanced. We will come back to this later.

class Node:

    def __init__(self, key, val, l, r):
        self.key = key  #Int
        self.val = val  #String
        self.l = l      #False/Node
        self.r = r      #False/Node

BST0 = False
BST1 = Node(1, "abc", False, False)
BST4 = Node(4, "dcj", False, Node(7, "ruf", False, False))
BST3 = Node(3, "ilk", BST1, BST4)
BST42 = Node(42, "ily",
            Node(27, "wit", Node(14, "olp", False, False), False),
            False)
BST10 = Node(10, "why", BST3, BST42)

def bstInsert(k, v, bst):
    if not bst:
        return Node(k, v, False, False)
    if k < bst.key:
        return Node(bst.key, bst.val, bstInsert(k, v, bst.l), bst.r)
    else:
        return Node(bst.key, bst.val, bst.l, bstInsert(k, v, bst.r))

# TODO: pass the tests

p1 = bstInsert(2, "qwe", BST0)
p2 = Node(2, "qwe", False, False)
print(p1.key, p1.val, p1.l, p1.r)
print(p2.key, p2.val, p2.l, p2.r)
print(p1 == p2)   # ??????????
assert bstInsert(2, "qwe", BST0) == Node(2, "qwe", False, False)    # tests fail for some reason
assert bstInsert(2, "qwe", BST1) == Node(1, "abc", False, Node(2, "qwe", False, False))
print("passed")