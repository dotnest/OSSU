
# PROBLEM:
# 
# Design a function that consumes a list of elements lox and a natural number
# n and produces the list formed by including the first element of lox, then 
# skipping the next n elements, including an element, skipping the next n 
# and so on.
# 
#  skipn(["a", "b", "c", "d", "e", "f"], 2) should produce ["a", "d"]

# List(X) Natural -> List(X)
# produce list containing 1st element of lox, then skip next n, then include...
def skipn_v1(lox0, n):

    # acc: Natural, the number of elements to skip before including next one
    # skipn(["a", "b", "c", "d"], 0)  ; include
    # skipn([     "b", "c", "d"], 2)  ; don't include
    # skipn([          "c", "d"], 1)  ; don't include
    # skipn([               "d"], 0)  ; include
    # skipn([                  ], 2)
    def skipn(lox, acc):
        if lox == []:
            return []
        if acc == 0:
            return [lox[0]] + skipn(lox[1:], n)
        return skipn(lox[1:], acc - 1)

    return skipn(lox0, 0)

assert skipn_v1([], 0) == []
assert skipn_v1(["a", "b", "c", "d", "e", "f"], 0) == ["a", "b", "c", "d", "e", "f"]
assert skipn_v1(["a", "b", "c", "d", "e", "f"], 1) == ["a", "c", "e"]
assert skipn_v1(["a", "b", "c", "d", "e", "f"], 2) == ["a", "d"]

# List(X) -> List(X)
# produce list containing 1st element of lox, then skip next n, then include one, then...
def skipn_v2(lox0, n):

    # acc: Natural, 1-based position of (first lox) in lox0
    def skipn(lox, n, acc):
        if lox == []:
            return []
        if acc % (n + 1) == 0:
            return [lox[0]] + skipn(lox[1:], n, acc + 1)
        return skipn(lox[1:], n, acc + 1)

    return skipn(lox0, n, 0)

assert skipn_v2([], 1) == []
assert skipn_v2(["a", "b", "c", "d"], 1) == ["a", "c"]
assert skipn_v2([1, 2, 3, 4, 5, 6, 7, 8, 9], 2) == [1, 4, 7]
assert skipn_v2([1, 2, 3, 4], 0) == [1, 2, 3, 4]
assert skipn_v2(["a", "b", "c", "d", "e", "f"], 2) == ["a", "d"]

print("passed all")