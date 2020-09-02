# ; PROBLEM:
# ; 
# ; Rewite each of the following function definitions using lambda. 


# ;; Number (listof Number) -> (listof Number)
# ;; produce only elements of lon > threshold
# def only_bigger(threshold, lon):
#     def pred(n):
#         return n > threshold
#     return list(filter(pred, lon))

def only_bigger(threshold, lon):
  return list(filter(lambda n: n > threshold, lon))

assert only_bigger(2, []) == []
assert only_bigger(3, [2, 4, 5]) == [4, 5]

# ;; (listof Image) -> (listof Natural)
# ;; produce list of areas of images
class Square:

    def __init__(self, size, filling, color):
        self.width = size
        self.height = size
        self.filling = filling
        self.color = color

class Rectangle:

    def __init__(self, width, height, filling, color):
        self.width = width
        self.height = height
        self.filling = filling
        self.color = color

# def all_areas(loi):
#     def area(i):
#         return i.width * i.height
#     return list(map(area, loi))

def all_areas(loi):
    return list(map(lambda i: i.width * i.height, loi))

assert all_areas([Rectangle(2, 3, "solid", "blue"), Square(10, "solid", "white")]) == [6, 100]

# ;; (listof Number)  ->  (listof Number)
# ;; produce list of numbers sorted in ASCENDING order
# ;; ASSUMPTION: lon contains no duplicates
# def qsort(lon):
#     if lon == []:
#         return []
#     p = lon[0]
#     def less_than_p(n):
#         return n < p
#     def more_than_p(n):
#         return n > p
#     return qsort(list(filter(less_than_p, lon))) + [p] + qsort(list(filter(more_than_p, lon)))

def qsort(lon):
    if lon == []: 
        return []
    p = lon[0]
    return qsort(list(filter(lambda n: n < p, lon))) + [p] + qsort(list(filter(lambda n: n > p, lon)))

assert qsort([]) == []
assert qsort([8]) == [8]
assert qsort([7, 8, 9]) == [7, 8, 9]
assert qsort([4, 3, 2, 1]) == [1, 2, 3, 4]
assert qsort([6, 8, 1, 9, 3, 7, 2]) == [1, 2, 3, 6, 7, 8, 9]

print("passed all")