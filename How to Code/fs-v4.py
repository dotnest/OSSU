class Element:

	def __init__(self, name, data, subs):
		self.name = name
		self.data = data
		self.subs = subs

# ;; Element is (make-elt String Integer ListOfElement)
# ;; interp. An element in the file system, with name, and EITHER data or subs.
# ;;         If data is 0, then subs is considered to be list of sub elements.
# ;;         If data is not 0, then subs is ignored.

F1 = Element("F1", 1, [])
F2 = Element("F2", 2, [])
F3 = Element("F3", 3, [])
D4 = Element("D4", 0, [F1, F2])
D5 = Element("D5", 0, [F3])
D6 = Element("D6", 0, [D4, D5])
# illustrated in fs-v1-used-example.png


# PROBLEM

# Design a function that consumes Element and produces the sum of all the file data in 
# the tree.

def sumData(e):
    def sumDataE(e: Element):
        return e.data + sumDataLoE(e.subs)

    def sumDataLoE(loe):
        if loe == []:
            return 0
        return sumDataE(loe[0]) + sumDataLoE(loe[1:])
    
    return sumDataE(e)

assert sumData(F1) == 1
assert sumData(D4) == 3
assert sumData(D5) == 3
assert sumData(D6) == 6
print("passed sumData")


# PROBLEM

# Design a function that consumes Element and produces a list of the names of all the elements in 
# the tree. 

def allNames(e):
    def allNamesE(e: Element):
        return [e.name] + allNamesLoE(e.subs)

    def allNamesLoE(loe):
        if loe == []:
            return []
        return allNamesE(loe[0]) + allNamesLoE(loe[1:])

    return allNamesE(e)

assert allNames(F1) == ["F1"]
assert allNames(D4) == ["D4", "F1", "F2"]
assert allNames(D5) == ["D5", "F3"]
assert allNames(D6) == ["D6"] + ["D4", "F1", "F2"] + ["D5", "F3"]
print("passed allNames")


# PROBLEM

# Design a function that consumes String and Element and looks for a data element with the given 
# name. If it finds that element it produces the data, otherwise it produces false.

def find(e, s):
    def findE(e: Element, s):
        if e.name == s:
            return e.data
        return findLoE(e.subs, s)

    def findLoE(loe, s):
        if loe == []:
            return False
        return findE(loe[0], s) or findLoE(loe[1:], s)

    return findE(e, s)

assert find(F1, "") == False
assert find(F1, "D1") == False
assert find(F1, "F1") == 1
assert find(D4, "F2") == 2
assert find(D6, "D3") == False
assert find(D6, "F3") == 3
print("passed find")