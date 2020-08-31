# ; In this problem set you will represent information about descendant family
# ; trees from Harry Potter and design functions that operate on those trees.
# ;
# ; To make your task much easier we suggest two things:
# ;   - you only need a DESCENDANT family tree
# ;   - read through this entire problem set carefully to see what information
# ;     the functions below are going to need. Design your data definitions to
# ;     only represent that information.
# ;   - you can find all the information you need by looking at the individual
# ;     character pages like the one we point you to for Arthur Weasley.

# ; PROBLEM 1:
# ;
# ; Design a data definition that represents a family tree from the Harry Potter
# ; wiki, which contains all necessary information for the other problems.  You
# ; will use this data definition throughout the rest of the homework.

class Person:

	def __init__(self, name, children, patronus, wand):
		self.name = name
		self.children = children
		self.patronus = patronus
		self.wand = wand

# children is a list of Person objects


# ; PROBLEM 2:
# ;
# ; Define a constant named ARTHUR that represents the descendant family tree for
# ; Arthur Weasley. You can find all the infomation you need by starting
# ; at: http://harrypotter.wikia.com/wiki/Arthur_Weasley.
# ;
# ; You must include all of Arthur's children and these grandchildren: Lily,
# ; Victoire, Albus, James.
# ;
# ; Note that on the Potter wiki you will find a lot of information. But for some
# ; people some of the information may be missing. Enter that information with a
# ; special value of "" (the empty string) meaning it is not present. Don't forget
# ; this special value when writing your interp.

Lily = Person("Lily", [], "", "Cherry")
Victoire = Person("Victoire", [], "", "Yew")
Albus = Person("Albus", [], "", "Cherry")
James = Person("James", [], "", "Cherry")
Bill = Person("Bill", [Victoire], "Non-corporeal", "Oak")
Ginny = Person("Ginny", [James, Albus, Lily], "Horse", "Yew")
Arthur = Person("Arthur",  [Bill, Ginny], "Weasel", "Oak")

# ; PROBLEM 3:
# ;
# ; Design a function that produces a pair list (i.e. list of two-element lists)
# ; of every person in the tree and his or her patronus. For example, assuming
# ; that HARRY is a tree representing Harry Potter and that he has no children
# ; (even though we know he does) the result would be: (list (list "Harry" "Stag")).
# ;
# ; You must use ARTHUR as one of your examples.

def personFun(p: Person):
	return [[p.name, p.patronus]] + childrenFun(p.children)

def childrenFun(loc):
	if loc == []:
		return []
	return personFun(loc[0]) + childrenFun(loc[1:])


assert childrenFun([]) == []
assert personFun(Lily) == [["Lily", ""]]
assert personFun(Bill) == [["Bill", "Non-corporeal"], ["Victoire", ""]]
assert personFun(Arthur) == [["Arthur", "Weasel"],
							["Bill", "Non-corporeal"],
							["Victoire", ""],
							["Ginny", "Horse"],
							["James", ""],
							["Albus", ""],
							["Lily", ""]]
print("passed")

# ; PROBLEM 4:
# ;
# ; Design a function that produces the names of every person in a given tree
# ; whose wands are made of a given material.
# ;
# ; You must use ARTHUR as one of your examples.

def personWand(p, w):
	if p.wand == w:
		return [p.name] + childrenWand(p.children, w)
	else:
		return childrenWand(p.children, w)

def childrenWand(lop, w):
	if lop == []:
		return []
	return personWand(lop[0], w) + childrenWand(lop[1:], w)

assert childrenWand([], "Oak") == []
assert personWand(Lily, "Cherry") ==  ["Lily"]
assert personWand(Lily, "Oak") == []
assert personWand(Bill, "Oak") ==  ["Bill"]
assert personWand(Bill, "Yew") ==  ["Victoire"]
assert personWand(Arthur, "Cherry") ==  ["James", "Albus", "Lily"]
print("passed")