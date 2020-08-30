import math

def area(r):
    return (math.pi * r * r)

area(4)  # ;(* pi (sqr 4)) ;area of circle radius 4
area(6)  # ;(* pi (sqr 6)) ;area of circle radius 6



# ;; String (listof String) -> Boolean
def contains(s, los):
    """produce True if los includes s"""
    if los == []:
        return False
    if los[0] == s:
        return True
    return contains(s, los[1:])

def containsUBC(los):
    """produce True if los includes 'UBC'"""
    return contains("UBC", los)

assert containsUBC([]) == False
assert containsUBC(["McGill"]) == False
assert containsUBC(["UBC"]) == True
assert containsUBC(["McGill", "UBC"]) == True

def containsMcGill(los):
    """produce True if los includes 'McGill'"""
    return contains("McGill", los)

assert containsMcGill([]) == False
assert containsMcGill(["UBC"]) == False
assert containsMcGill(["McGill"]) == True
assert containsMcGill(["UBC", "McGill"]) == True

assert contains("UBC", []) == False
assert contains("UBC", ["McGill"]) == False
assert contains("UBC", ["UBC"]) == True
assert contains("UBC", ["McGill", "UBC"]) == True
assert contains("McGill", []) == False
assert contains("McGill", ["UBC"]) == False
assert contains("McGill", ["McGill"]) == True
assert contains("McGill", ["UBC", "McGill"]) == True



# ;; (X -> Y) (listof X) -> (listof Y)
def map2(fn, lon):
    """produce list of fn(n) for every n in lon"""
    if lon == []:
        return []
    return [fn(lon[0])] + map2(fn, lon[1:])

def squares(lon):
    """produce list of square of every number in lon"""
    return map2(lambda x: x**2, lon)
# def squares(lon):
#     return [i**2 for i in lon]

assert squares([]) == []
assert squares([3, 4]) == [9, 16]

def squareRoots(lon):
    """produce list of math.sqrt of every number in lon"""
    return map2(math.sqrt, lon)

assert squareRoots([]) == []
assert squareRoots([9, 16]) == [3, 4]

assert map2(lambda x: x**2, []) == []
assert map2(lambda x: x**2, [3, 4]) == [9, 16]
assert map2(math.sqrt, []) == []
assert map2(math.sqrt, [9, 16]) == [3, 4]



# ;; (X -> Boolean) (listof X) -> (listof X)
def filter2(fltr, lon):
    """produce list with only those elements of lon which produce true for fltr(n)"""
    if lon == []:
        return []
    if fltr(lon[0]):
        return [lon[0]] + filter2(fltr, lon[1:])
    else:
        return filter2(fltr, lon[1:])

def positiveOnly(lon):
    """produce list with only positive elements of lon"""
    return filter2(lambda x: x>0, lon)

assert positiveOnly([]) == []
assert positiveOnly([1, -2, 3, -4]) == [1, 3]

def negativeOnly(lon):
    """produce list with only negative elements of lon"""
    return filter2(lambda x: x<0, lon)

assert negativeOnly([]) == []
assert negativeOnly([1, -2, 3, -4]) == [-2, -4]

assert filter2(lambda x: x>0, []) == []
assert filter2(lambda x: x>0, [1, -2, 3, -4]) == [1, 3]
assert filter2(lambda x: x<0, []) == []
assert filter2(lambda x: x<0, [1, -2, 3, -4]) == [-2, -4]

print("passed all")