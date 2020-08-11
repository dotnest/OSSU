# Design a function that consumes a list of boolean values and produces true 
# if every value in the list is true. If the list is empty, your function 
# should also produce true

lob1 = []
lob2 = [False]
lob3 = [True]
lob4 = [True, True, True]
lob5 = [True, False, True]

def allTrue(lob):
    if len(lob) == 0:
        return True
    return lob[0] and allTrue(lob[1:])

assert allTrue(lob1) == True
assert allTrue(lob2) == False
assert allTrue(lob3) == True
assert allTrue(lob4) == True
assert allTrue(lob5) == False
print("passed")