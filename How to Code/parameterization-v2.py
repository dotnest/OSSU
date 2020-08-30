import math

def area(r):
    return (math.pi * r * r)

area(4)  # ;(* pi (sqr 4)) ;area of circle radius 4
area(6)  # ;(* pi (sqr 6)) ;area of circle radius 6



# ;; ListOfString -> Boolean
# ;; produce True if los includes s
def contains(s, los):
    if los == []:
        return False
    if los[0] == s:
        return True
    return contains(s, los[1:])

def containsUBC(los):
    return contains("UBC", los)

def containsMcGill(los):
    return contains("McGill", los)

assert contains("UBC", []) == False
assert contains("UBC", ["McGill"]) == False
assert contains("UBC", ["UBC"]) == True
assert contains("UBC", ["McGill", "UBC"]) == True
assert contains("McGill", []) == False
assert contains("McGill", ["UBC"]) == False
assert contains("McGill", ["McGill"]) == True
assert contains("McGill", ["UBC", "McGill"]) == True



# ;; ListOfNumber -> ListOfNumber
# ;; produce list of fn(n) for every n in lon
def map2(fn, lon):
    if lon == []:
        return []
    return [fn(lon[0])] + map2(fn, lon[1:])

def squares(lon):
    return map2(lambda x: x**2, lon)
# def squares(lon):
#     return [i**2 for i in lon]

def squareRoots(lon):
    return map2(math.sqrt, lon)

assert map2(lambda x: x**2, []) == []
assert map2(lambda x: x**2, [3, 4]) == [9, 16]
assert map2(math.sqrt, []) == []
assert map2(math.sqrt, [9, 16]) == [3, 4]



# ;; ListOfNumber -> ListOfNumber
# ;; produce list with only those elements of lon which produce true for fltr(n)
def filter2(fltr, lon):
    if lon == []:
        return []
    if fltr(lon[0]):
        return [lon[0]] + filter2(fltr, lon[1:])
    else:
        return filter2(fltr, lon[1:])

def positiveOnly(lon):
    return filter2(lambda x: x>0, lon)

def negativeOnly(lon):
    return filter2(lambda x: x<0, lon)

assert filter2(lambda x: x>0, []) == []
assert filter2(lambda x: x>0, [1, -2, 3, -4]) == [1, 3]
assert filter2(lambda x: x<0, []) == []
assert filter2(lambda x: x<0, [1, -2, 3, -4]) == [-2, -4]

print("passed all")