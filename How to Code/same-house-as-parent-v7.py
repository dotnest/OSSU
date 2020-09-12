
# PROBLEM:
# 
# In the Harry Potter movies, it is very important which of the four houses a
# wizard is placed in when they are at Hogwarts. This is so important that in
# most families multiple generations of wizards are all placed in the same family.
# 
# Design a representation of wizard family trees that includes, for each wizard,
# their name, the house they were placed in at Hogwarts and their children. We
# encourage you to get real information for wizard families from:
#    http://harrypotter.wikia.com/wiki/Main_Page
# 
# The reason we do this is that designing programs often involves collection
# domain information from a variety of sources and representing it in the program
# as constants of some form. So this problem illustrates a fairly common scenario.
# 
# That said, for reasons having to do entirely with making things fit on the
# screen in later videos, we are going to use the following wizard family tree,
# in which wizards and houses both have 1 letter names. (Sigh)

# Data definitions:

class Wizard:

    def __init__(self, name, house, kids):
        self.name = name
        self.house = house
        self.kids = kids

# Wizard is Wizard(String String (listof Wizard))
# interp. A wizard, with name, house and list of children.

Wa = Wizard("A", "S", [])
Wb = Wizard("B", "G", [])
Wc = Wizard("C", "R", [])
Wd = Wizard("D", "H", [])
We = Wizard("E", "R", [])
Wf = Wizard("F", "R", [Wb])
Wg = Wizard("G", "S", [Wa])
Wh = Wizard("H", "S", [Wc, Wd])
Wi = Wizard("I", "H", [])
Wj = Wizard("J", "R", [We, Wf, Wg])
Wk = Wizard("K", "G", [Wh, Wi, Wj])


# template, arb-arity-tree, encapsulated w/ local
# def fn_for_wiz(w):
#
#     def fn_for_wiz(w):
#         w.name
#         w.house
#         fn_for_low(w.kids, w)
#
#     def fn_for_low(low):
#         if low == []:
#             pass
#         fn_for_wiz(low[0])
#         fn_for_low(low[1:])
#
#     fn_for_wiz(w)


# Functions:

# PROBLEM:
# 
# Design a function that consumes a wizard and produces the names of every 
# wizard in the tree that was placed in the same house as their immediate
# parent. 

# Wizard -> List(string)
# Produce the names of every descendant in the same house as their parent.
# template from Wizard plus lost context accumulator ("" for root of the tree)
def same_house_as_parent(w):

    # parent-house is String, the house of wizard's immediate parent
    def fn_for_wiz(w, parent_house):
        if parent_house == w.house:
            return [w.name] + fn_for_low(w.kids, w.house)
        return fn_for_low(w.kids, w.house)

    def fn_for_low(low, parent_house):
        if low == []:
            return []
        return fn_for_wiz(low[0], parent_house) + fn_for_low(low[1:], parent_house)
    
    return fn_for_wiz(w, "")

assert same_house_as_parent(Wa) == []
assert same_house_as_parent(Wh) == []
assert same_house_as_parent(Wg) == ["A"]
assert same_house_as_parent(Wk) == ["E", "F", "A"]


def same_house_as_parent_tail(w):
    # todo is (listof ...), a worklist accumulator
    # rsf is (listof String), a result-so-far accumulator
    class WLE:
        
        # WLE (worklist entry) is (make-wle Wizard String)
        # interp. a worklist entry with the wizard to pass to fn_for_wiz
        #         and that wizard's parent house
        def __init__(self, w, ph):
            self.w = w
            self.ph = ph

    def fn_for_wiz(todo, w, ph, rsf):
        if w.house == ph:
            rsf = [w.name] + rsf
        return fn_for_low(list(map(lambda k: WLE(k, w.house), w.kids)) + todo, rsf)

    def fn_for_low(todo, rsf):
        if todo == []:
            return rsf
        return fn_for_wiz(todo[1:], todo[0].w, todo[0].ph, rsf)

    return fn_for_wiz([], w, "", [])

assert same_house_as_parent_tail(Wa) == []
assert same_house_as_parent_tail(Wh) == []
assert same_house_as_parent_tail(Wg) == ["A"]
assert same_house_as_parent_tail(Wk) == ["A", "F", "E"]

# PROBLEM:
# 
# Design a new function definition for same_house_as_parent that is tail
# recursive. You will need a worklist accumulator.

# PROBLEM:
# 
# Design a function that consumes a wizard and produces the number of wizards
# in that tree (including the root). Your function should be tail recursive.


# Wizard -> Natural
# produces the number of wizards in that tree (including the root)

# (define (count w) 0)

# template: from Wizard (arb-arity + local)
#           add result so far accumulator for tail recursion
#           add worklist accumulator for tail recursion

def count(w):   
    # rsf is Natural; the number of wizards seen so far
    # todo is (listof Wizard) ; wizards we still need to visit with fn_for_wiz
    # (count Wk)
    # (fn_for_wiz Wk 0)
    # (fn_for_wiz Wh 1)
    # (fn_for_wiz Wc 2)
    def fn_for_wiz(w, todo, rsf):
        return fn_for_low(w.kids + todo, rsf + 1)

    def fn_for_low(todo, rsf):
        if todo == []:
            return rsf
        return fn_for_wiz(todo[0], todo[1:], rsf)

    return fn_for_wiz(w, [], 0)

assert count(Wa) == 1
assert count(Wk) == 11

print("passed all")