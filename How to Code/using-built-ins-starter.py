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

# ;; Image -> Boolean
# ;; produce True if image is wide/tall/square
def is_wide(img):
    return img.width > img.height
def is_tall(img):
    return img.width < img.height
def is_square(img):
    return img.width == img.height

assert is_wide(I1) == False
assert is_wide(I2) == True
assert is_tall(I3) == True
assert is_tall(I4) == False
assert is_square(I1) == False
assert is_square(I2) == False
assert is_square(I5) == True


# ;; Image -> Number
# ;; produce area of image
def area(img):
    return img.width * img.height

assert area(I1) == 200
assert area(I2) == 600

# ; In addition to map and filter there are several other useful abstract 
# ; list functions built into ISL.  These are listed on the Language page
# ; of the course web site. Examples of their use are shown below:

assert list(map(lambda x: x>0, [1, -2, 3, -4])) == [True, False, True, False]

assert list(filter(lambda x: x<0, [1, -2, 3, -4])) == [-2, -4]

# assert foldr + 0 [1, 2, 3] [+ 1, 2, 3, 0]   # ;foldr is abstraction
# assert foldr * 1 [1, 2, 3] [* 1, 2, 3, 1]   # ;of sum and product          

assert list(range(6)) == [0, 1, 2, 3, 4, 5]

assert [i**2 for i in range(4)] == [0, 1, 4, 9]


# ; PROBLEM: 
# ; 
# ; Complete the design of the following functions by coding them using a 
# ; built-in abstract list function.

# ;; (listof Image) -> (listof Image)
# ;; produce list of only those images that are wide?
def wide_only(loi):
    return list(filter(is_wide, loi))

assert wide_only([I1, I2, I3, I4, I5]) == [I2, I4]

# ;; (listof Image) -> Boolean
# ;; are all the images in loi tall?
def all_tall(loi):
    return all(map(is_tall, loi))

assert all_tall(LOI1) == False


# ;; (listof Number) -> Number
# ;; sum the elements of a list
def sum_list(lon):
    return sum(lon)

assert sum_list([1, 2, 3, 4]) == 10


# ;; Natural -> Natural
# ;; produce the sum of the first n natural numbers
def sum_to(n):
    return sum(range(n))

assert sum_to(3) == (0 + 1 + 2)

print("passed all")