
# ; PROBLEM:
# ; 
# ; Design a function that consumes a list of elements and produces the list
# ; consisting of only the 1st, 3rd, 5th and so on elements of its input. 
# ; 
# ;    skip1(["a", "b", "c", "d"]) should produce ["a", "c"]

def skip1(l):
    def skip1(l, pos):
        if l == []:
            return []
        if pos % 2 == 0:
            return [l[0]] + skip1(l[1:], pos + 1)
        return skip1(l[1:], pos + 1)
    
    return skip1(l, 0)

assert skip1(["a", "b", "c", "d"]) == ["a", "c"]
assert skip1([0, 1, 2, 3, 4, 5]) == [0, 2, 4]

print("passed all")
