# PROBLEM:

# Design a function that consumes a list of numbers and doubles every number 
# in the list.

lon1 = []
lon2 = [1]
lon3 = [1, 2, 3]
lon4 = [4, -2.2, 0, 1.3]

def doubleAll(lon):
    if lon == []:
        return []
    return [2*lon[0]] + doubleAll(lon[1:])

assert doubleAll(lon1) == []
assert doubleAll(lon2) == [2]
assert doubleAll(lon3) == [2, 4, 6]
assert doubleAll(lon4) == [8, -4.4, 0, 2.6]
print("passed")