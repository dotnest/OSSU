import math

def area(r):
    return (math.pi * r * r)

area(4)  # ;(* pi (sqr 4)) ;area of circle radius 4
area(6)  # ;(* pi (sqr 6)) ;area of circle radius 6



# ;; ListOfString -> Boolean
# ;; produce True if los includes "UBC"
def contains(s, los):
    if los == []:
        return False
    if los[0] == s:
        return True
    return contains(s, los[1:])

def containsUBC(los):
    return contains("UBC", los)

assert containsUBC([]) == False
assert containsUBC(["McGill"]) == False
assert containsUBC(["UBC"]) == True
assert containsUBC(["McGill", "UBC"]) == True

# ;; ListOfString -> Boolean
# ;; produce True if los includes "McGill"
def containsMcGill(los):
    return contains("McGill", los)

assert containsMcGill([]) == False
assert containsMcGill(["UBC"]) == False
assert containsMcGill(["McGill"]) == True
assert containsMcGill(["UBC", "McGill"]) == True



# ;; ListOfNumber -> ListOfNumber
# ;; produce list of sqr of every number in lon
def map2(fn, lon):
    if lon == []:
        return []
    return [fn(lon[0])] + map2(fn, lon[1:])

def squares(lon):
    return map2(lambda x: x**2, lon)
# def squares(lon):
#     return [i**2 for i in lon]

assert squares([]) == []
assert squares([3, 4]) == [9, 16]

# ;; ListOfNumber -> ListOfNumber
# ;; produce list of sqrt of every number in lon
def squareRoots(lon):
    return map2(math.sqrt, lon)

assert squareRoots([]) == []
assert squareRoots([9, 16]) == [3, 4]



# ;; ListOfNumber -> ListOfNumber
# ;; produce list with only positive? elements of lon
def filter2(fltr, lon):
    if lon == []:
        return []
    if fltr(lon[0]):
        return [lon[0]] + filter2(fltr, lon[1:])
    else:
        return filter2(fltr, lon[1:])

def positiveOnly(lon):
    return filter2(lambda x: x>0, lon)

assert positiveOnly([]) == []
assert positiveOnly([1, -2, 3, -4]) == [1, 3]

# ;; ListOfNumber -> ListOfNumber
# ;; produce list with only negative? elements of lon
def negativeOnly(lon):
    return filter2(lambda x: x<0, lon)

assert negativeOnly([]) == []
assert negativeOnly([1, -2, 3, -4]) == [-2, -4]

print("passed all")