
# PROBLEM:
# 
# (A) Consider the following function that consumes a list of numbers and produces
#     the sum of all the numbers in the list. Use the stepper to analyze the behavior 
#     of this function as the list gets larger and larger. 
#     
# (B) Use an accumulator to design a tail-recursive version of sum.

# List(Number) -> Number
# produce sum of all elements of lon
def sum_1(lon):
    if lon == []:
        return 0
    return lon[0] + sum_1(lon[1:])

assert sum_1([]) == 0
assert sum_1([2, 4, 5]) == 11

def sum_2(lon0):
    # acc: Number, the sum of elements of lon0 seen so far
    # sum_2([2, 4, 5])
    # sum_2([2, 4, 5])  0)
    # sum_2([   4, 5])  2)
    # sum_2([      5])  6)
    # sum_2([       ]) 11)
    def sum_2(lon, acc):
        if lon == []:
            return acc
        return sum_2(lon[1:], (acc + lon[0]))

    return sum_2(lon0, 0)

assert sum_2([]) == 0
assert sum_2([2, 4, 5]) == 11

print("passed all")

sum_2([2, 4, 5]) # use debugger step-by-step to see the difference