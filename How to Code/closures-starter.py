# ;; Some setup data and functions to enable more interesting examples
# ;; below

class Rectangle():

    def __init__(self, width, height, filling, color):
        self.width = width
        self.height = height
        self.filling = filling
        self.color = color

I1 = Rectangle(10, 20, "solid", "red")
I2 = Rectangle(30, 20, "solid", "yellow")
I3 = Rectangle(40, 50, "solid", "green")
I4 = Rectangle(60, 50, "solid", "blue")
I5 = Rectangle(90, 90, "solid", "orange")

LOI1 = [I1, I2, I3, I4, I5]

# ;; NOTE: Unlike using-built-ins-starter.rkt this file does not define
# ;; the functions tall? wide? square? and area.

# ; PROBLEM: 
# ; 
# ; Complete the design of the following functions by completing the body
# ; which has already been templated to use a built-in abstract list function. 

# ;; (listof Image) -> (listof Image)
# ;; produce list of only those images that have width >= height
def wide_only(loi):
    def wide(i):
        return i.width > i.height
    return list(filter(wide, loi))

assert wide_only([I1, I2, I3, I4, I5]) == [I2, I4]


# ;; Number (listof Image) -> (listof Image)
# ;; produce list of only those images in loi with width >= w
def wider_than_only(w, loi):
    def wider_than(i):
            return i.width > w
    return list(filter(wider_than, loi))

assert wider_than_only(40, LOI1) == [I4, I5]


# ;; (listof Number) -> (listof Number)
# ;; produce list of each number in lon cubed
def cube_all(lon):
    def cube(x):
        return x**3
    return list(map(cube, lon))

assert cube_all([1, 2, 3]) == [(1 * 1 * 1), (2 * 2 * 2), (3 * 3 * 3)]


# ;; String (listof String) -> (listof String)
# ;; produce list of all elements of los prefixed by p
def prefix_all(p, los):
    def add_prefix(elem):
        return p + elem
    return list(map(add_prefix, los))

assert prefix_all("accio ", ["portkey", "broom"]) == ["accio portkey", "accio broom"]

print("passed all")