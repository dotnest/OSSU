# Problem:

# Design the function merge. It consumes two lists of numbers, which it assumes are 
# each sorted in ascending order. It produces a single list of all the numbers, 
# also sorted in ascending order. 

# Your solution should explicitly show the cross product of type comments table, 
# filled in with the values in each case. Your final function should have a cond 
# with 3 cases. You can do this simplification using the cross product table by 
# recognizing that there are subtly equal answers. 

# Hint: Think carefully about the values of both lists. You might see a way to 
# change a cell content so that 2 cells have the same value.

l0 = []
l1 = [1]
l2 = [5, 9]
l3 = [1, 6, 10]
l4 = [-5, 1, 1, 3, 8]

def merge(la, lb):
    if la == lb and lb == False:
        return []
    if la == [] or lb == []:
        return la + lb
    if la[0] < lb[0]:
        return [la[0]] + merge(la[1:], lb)
    else:
        return [lb[0]] + merge(la, lb[1:])

assert merge(l0, l0) == []
assert merge(l1, l0) == l1
assert merge(l1, l2) == [1, 5, 9]
assert merge(l2, l1) == [1, 5, 9]
assert merge(l4, l3) == [-5, 1, 1, 1, 3, 6, 8, 10]
print("passed")