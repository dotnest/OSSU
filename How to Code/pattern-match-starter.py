# ; Problem:
# ; 
# ; It is often useful to be able to tell whether the first part of a sequence of 
# ; characters matches a given pattern. In this problem you will design a (somewhat 
# ; limited) way of doing this.

# ;; Pattern is one of:
# ;;  - empty
# ;;  - (cons "A" Pattern)
# ;;  - (cons "N" Pattern)
# ;; interp.
# ;;   A pattern describing certain ListOf1String. 
# ;;  "A" means the corresponding letter must be alphabetic.
# ;;  "N" means it must be numeric.  For example:
# ;;      (list "A" "N" "A" "N" "A" "N")
# ;;   describes Canadian postal codes like:
# ;;      (list "V" "6" "T" "1" "Z" "4")
# (define PATTERN1 (list "A" "N" "A" "N" "A" "N"))

# ;; ListOf1String is one of:
# ;;  - empty
# ;;  - (cons 1String ListOf1String)
# ;; interp. a list of strings each 1 long
# (define LOS1 (list "V" "6" "T" "1" "Z" "4"))

# Now design a function that consumes Pattern and ListOf1String and produces true 
# if the pattern matches the ListOf1String. For example,
# (pattern-match? (list "A" "N" "A" "N" "A" "N")
#                 (list "V" "6" "T" "1" "Z" "4"))
# should produce true. If the ListOf1String is longer than the pattern, but the 
# first part matches the whole pattern produce true. If the ListOf1String is 
# shorter than the Pattern you should produce false.       

# Treat this as the design of a function operating on 2 complex data. After your 
# signature and purpose, you should write out a cross product of type comments 
# table. You should reduce the number of cases in your cond to 4 using the table, 
# and you should also simplify the cond questions using the table.


# ;   pattern -> empty | Pattern
# ; Lo1S  -----------------------
# ; empty|       true  | false
# ;      |-------------+---------
# ; Lo1S |       true  | match?()

def match(p, s):
    if not p:
        return True
    if not s:
        return False
    if p[0] == "A":
        return s[0].isalpha() and match(p[1:], s[1:])
    else:
        return s[0].isnumeric() and match(p[1:], s[1:])

assert match(["A", "N", "A", "N", "A", "N"],
            ["V", "6", "T", "1", "Z", "4"]) == True
assert match(["A", "N", "A", "N", "A", "N"],
            ["V", "W", "T", "1", "Z", "4"]) == False
assert match(["A", "N", "A"],
            ["V", "6", "T", "1", "Z", "4"]) == True
assert match(["A", "N", "A", "N", "A", "N"],
            ["V", "6", "T"]) == False
print("passed")