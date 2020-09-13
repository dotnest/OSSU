# Problem:
# 
# Starting with the following data definition for a binary tree (not a binary search tree) 
# design a tail-recursive function called contains that consumes a key and a binary tree 
# and produces True if the tree contains the key.

class Node:

    def __init__(self, key, value, left, right):
        self.key = key
        self.value = value
        self.left = left
        self.right = right

# BT is one of:
#  - False
#  - Node(Integer, String, BT, BT)
# Interp. A binary tree, each node has a key, value and 2 children
BT1 = False
BT2 = Node(1, "a", Node(6, "f", Node(4, "d", False, False),
                                False),
                    Node(7, "g", False, False))


# Integer BT -> Boolean
# Produce True if the tree contains the given key
def contains(k, bt):
    # todo: List(BT); the list of so far univisited right branches
    def contains_one(bt, todo):
        if bt == False:
            return contains_list(todo)
        if bt.key == k:
            return True
        return contains_one(bt.left, [bt.right] + todo)
            
    def contains_list(todo):
        if todo == []:
            return False
        return contains_one(todo[0], todo[1:])
        
    return contains_one(bt, [])

# This alternative is also good. It puts both branches on the todo. Note the change
# in contains_one(as well as the change in the accumulator invariant
# <template from BT + accumulator>
def contains_2(k, bt):
    # todo: List(BT); the list of so far univisited right branches
    def contains_one(bt, todo):
        if bt == False:
            return contains_list(todo)
        if bt.key == k:
            return True
        return contains_list([bt.left] + [bt.right] + todo)

    def contains_list(todo):
        if todo == []:
            return False
        return contains_one(todo[0], todo[1:])
        
    return contains_one(bt, [])

assert contains(1, BT1) == False
assert contains(1, BT2) == True
assert contains(3, BT2) == False
assert contains(7, BT2) == True
assert contains_2(1, BT1) == False
assert contains_2(1, BT2) == True
assert contains_2(3, BT2) == False
assert contains_2(7, BT2) == True

print("passed all")