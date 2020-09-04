
# Brute force Sudoku solver

# In Sudoku, the board is a 9x9 grid of SQUARES.
# There are 9 ROWS and 9 COLUMNS, there are also 9
# 3x3 BOXES.  Rows, columns and boxes are all UNITs.
# So there are 27 units.
#
# The idea of the game is to fill each square with
# a Natural[1, 9] such that no unit contains a duplicate
# number.

# =================
# Data definitions:


# Val is Natural[1, 9]

# Board is List(Val|False)   that is 81 elements long
# interp.
#  Visually a board is a 9x9 array of squares, where each square
#  has a row and column number (r, c).  But we represent it as a
#  single flat list, in which the rows are layed out one after
#  another in a linear fashion. (See interp. of Pos below for how
#  we convert back and forth between (r, c) and position in a board.)

# Pos is Natural[0, 80]
# interp.
#  the position of a square on the board, for a given p, then
#    - the row    is (p // 9)
#    - the column is (p %  9)


# Convert 0-based row and column to Pos
def row_col_to_pos(r, c):
    return r * 9 + c  # helpful for writing tests


# Unit is List(Pos) of length 9
# interp. 
#  The position of every square in a unit. There are
#  27 of these for the 9 rows, 9 columns and 9 boxes.


# =================
# Constants:

ALL_VALS = [1, 2, 3, 4, 5, 6, 7, 8, 9]

B = False  # B stands for blank


BD1 =  [B, B, B, B, B, B, B, B, B,
        B, B, B, B, B, B, B, B, B,
        B, B, B, B, B, B, B, B, B,
        B, B, B, B, B, B, B, B, B,
        B, B, B, B, B, B, B, B, B,
        B, B, B, B, B, B, B, B, B,
        B, B, B, B, B, B, B, B, B,
        B, B, B, B, B, B, B, B, B,
        B, B, B, B, B, B, B, B, B]

BD2 =  [1, 2, 3, 4, 5, 6, 7, 8, 9,
        B, B, B, B, B, B, B, B, B,
        B, B, B, B, B, B, B, B, B,
        B, B, B, B, B, B, B, B, B,
        B, B, B, B, B, B, B, B, B,
        B, B, B, B, B, B, B, B, B,
        B, B, B, B, B, B, B, B, B,
        B, B, B, B, B, B, B, B, B,
        B, B, B, B, B, B, B, B, B]

BD3 =  [1, B, B, B, B, B, B, B, B,
        2, B, B, B, B, B, B, B, B,
        3, B, B, B, B, B, B, B, B,
        4, B, B, B, B, B, B, B, B,
        5, B, B, B, B, B, B, B, B,
        6, B, B, B, B, B, B, B, B,
        7, B, B, B, B, B, B, B, B,
        8, B, B, B, B, B, B, B, B,
        9, B, B, B, B, B, B, B, B]

#easy
BD4 =  [2, 7, 4, B, 9, 1, B, B, 5,
        1, B, B, 5, B, B, B, 9, B,
        6, B, B, B, B, 3, 2, 8, B,
        B, B, 1, 9, B, B, B, B, 8,
        B, B, 5, 1, B, B, 6, B, B,
        7, B, B, B, 8, B, B, B, 3,
        4, B, 2, B, B, B, B, B, 9,
        B, B, B, B, B, B, B, 7, B,
        8, B, B, 3, 4, 9, B, B, B]

#solution to 4
BD4s = [2, 7, 4, 8, 9, 1, 3, 6, 5,
        1, 3, 8, 5, 2, 6, 4, 9, 7,
        6, 5, 9, 4, 7, 3, 2, 8, 1,
        3, 2, 1, 9, 6, 4, 7, 5, 8,
        9, 8, 5, 1, 3, 7, 6, 4, 2,
        7, 4, 6, 2, 8, 5, 9, 1, 3,
        4, 6, 2, 7, 5, 8, 1, 3, 9,
        5, 9, 3, 6, 1, 2, 8, 7, 4,
        8, 1, 7, 3, 4, 9, 5, 2, 6]

#hard
BD5 =  [5, B, B, B, B, 4, B, 7, B,
        B, 1, B, B, 5, B, 6, B, B,
        B, B, 4, 9, B, B, B, B, B,
        B, 9, B, B, B, 7, 5, B, B,
        1, 8, B, 2, B, B, B, B, B,
        B, B, B, B, B, 6, B, B, B,
        B, B, 3, B, B, B, B, B, 8,
        B, 6, B, B, 8, B, B, B, 9,
        B, B, 8, B, 7, B, B, 3, 1]

#solution to 5
BD5s = [5, 3, 9, 1, 6, 4, 8, 7, 2,
        8, 1, 2, 7, 5, 3, 6, 9, 4,
        6, 7, 4, 9, 2, 8, 3, 1, 5,
        2, 9, 6, 4, 1, 7, 5, 8, 3,
        1, 8, 7, 2, 3, 5, 9, 4, 6,
        3, 4, 5, 8, 9, 6, 1, 2, 7,
        9, 2, 3, 5, 4, 1, 7, 6, 8,
        7, 6, 1, 3, 8, 2, 4, 5, 9,
        4, 5, 8, 6, 7, 9, 2, 3, 1]

#hardest ever? (Dr Arto Inkala)
BD6 =  [B, B, 5, 3, B, B, B, B, B,
        8, B, B, B, B, B, B, 2, B,
        B, 7, B, B, 1, B, 5, B, B,
        4, B, B, B, B, 5, 3, B, B,
        B, 1, B, B, 7, B, B, B, 6,
        B, B, 3, 2, B, B, B, 8, B,
        B, 6, B, 5, B, B, B, B, 9,
        B, B, 4, B, B, B, B, 3, B,
        B, B, B, B, B, 9, 7, B, B]

#no solution
BD7 =  [1, 2, 3, 4, 5, 6, 7, 8, B,
        B, B, B, B, B, B, B, B, 2,
        B, B, B, B, B, B, B, B, 3,
        B, B, B, B, B, B, B, B, 4,
        B, B, B, B, B, B, B, B, 5,
        B, B, B, B, B, B, B, B, 6,
        B, B, B, B, B, B, B, B, 7,
        B, B, B, B, B, B, B, B, 8,
        B, B, B, B, B, B, B, B, 9]


# Positions of all the rows, columns and boxes:

ROWS = [[ 0,  1,  2,  3,  4,  5,  6,  7,  8],  # positions for first row in a list
        [ 9, 10, 11, 12, 13, 14, 15, 16, 17],  # positions for second row in a list
        [18, 19, 20, 21, 22, 23, 24, 25, 26],
        [27, 28, 29, 30, 31, 32, 33, 34, 35],
        [36, 37, 38, 39, 40, 41, 42, 43, 44],
        [45, 46, 47, 48, 49, 50, 51, 52, 53],
        [54, 55, 56, 57, 58, 59, 60, 61, 62],
        [63, 64, 65, 66, 67, 68, 69, 70, 71],
        [72, 73, 74, 75, 76, 77, 78, 79, 80]]

COLS = [[0,  9, 18, 27, 36, 45, 54, 63, 72],  # positions for first column in a list
        [1, 10, 19, 28, 37, 46, 55, 64, 73],  # positions for second column in a list
        [2, 11, 20, 29, 38, 47, 56, 65, 74],
        [3, 12, 21, 30, 39, 48, 57, 66, 75],
        [4, 13, 22, 31, 40, 49, 58, 67, 76],
        [5, 14, 23, 32, 41, 50, 59, 68, 77],
        [6, 15, 24, 33, 42, 51, 60, 69, 78],
        [7, 16, 25, 34, 43, 52, 61, 70, 79],
        [8, 17, 26, 35, 44, 53, 62, 71, 80]]

BOXES = [[0,  1,  2,  9, 10, 11, 18, 19, 20],  # positions for first box in a list
        [ 3,  4,  5, 12, 13, 14, 21, 22, 23],  # positions for second box in a list
        [ 6,  7,  8, 15, 16, 17, 24, 25, 26],
        [27, 28, 29, 36, 37, 38, 45, 46, 47],
        [30, 31, 32, 39, 40, 41, 48, 49, 50],
        [33, 34, 35, 42, 43, 44, 51, 52, 53],
        [54, 55, 56, 63, 64, 65, 72, 73, 74],
        [57, 58, 59, 66, 67, 68, 75, 76, 77],
        [60, 61, 62, 69, 70, 71, 78, 79, 80]]

UNITS = ROWS + COLS + BOXES


# =================
# Functions:

# Board -> Boolean
# produce True if board is solved
# Assume: board is valid, so it is solved if it is full
def is_solved(bd):
    return all(bd) # (andmap number? bd)) 

assert is_solved(BD1) == False
assert is_solved(BD4) == False
assert is_solved(BD4s) == True

# Board Pos Val -> Board
# produce new board with val at given position
def fill_square(bd, p, nv):
    return bd[:p] + [nv] + bd[p+1:]

assert fill_square(BD1, 0, 1) == [1] + BD1[1:]

# Board -> Pos
# produces the position of the first blank square
# ASSUME: the board has at least one blank square
def find_blank(bd):
    if bd == []:
        raise Exception("The board didn't have a blank space.")
    if bd[0] == False:
        return 0
    return 1 + find_blank(bd[1:])  

assert find_blank(BD1) == 0
assert find_blank([2] + BD1[1:]) == 1
assert find_blank([2, 4] + BD1[2:]) == 2


# Board -> Boolean
# produce True if no unit on the board has the same value twice; False otherwise
def is_valid_board(bd):

    def are_valid_units(lou):
        return all(map(is_valid_unit, lou))
    
    def is_valid_unit(u):
        values = [bd[i] for i in u if bd[i] > 0]
        return len(set(values)) == len(values)  # has_no_duplicates(keep_only_naturals(read_unit(u)))

    # def read_unit(u):
    #     return [bd[i] for i in u]

    # def read_pos(p):
    #     return bd[p]

    # def keep_only_naturals(lovf):
    #     return list(filter(lambda x: x > 0, lovf))

    def has_no_duplicates(lov):
        if lov == []:
            return True
        if lov[0] in lov[1:]:
            return False
        return has_no_duplicates(lov[1:])

    return are_valid_units(UNITS)

assert is_valid_board(BD1) == True
assert is_valid_board(BD2) == True
assert is_valid_board(BD3) == True
assert is_valid_board(BD4) == True
assert is_valid_board(BD5) == True
assert is_valid_board([2] + BD2[1:]) == False
assert is_valid_board([2] + BD3[1:]) == False
assert is_valid_board(fill_square(BD4, 1, 6)) == False

# (listof Board) -> (listof Board)
# produce list containing only valid boards
def keep_only_valid(lobd):
    return list(filter(is_valid_board, lobd))

assert keep_only_valid([[1, 1] + BD1[2:]]) == []

# Pos Board -> (listof Board)
# produce 9 boards, with blank filled with Natural[1, 9]
def fill_with_1_9(p, bd):
    def build_one(n):
        return fill_square(bd, p, (n + 1))
    return [build_one(i) for i in range(9)]
    
assert fill_with_1_9(0, BD1) == [[1] + BD1[1:],
                                [2] + BD1[1:],
                                [3] + BD1[1:],
                                [4] + BD1[1:],
                                [5] + BD1[1:],
                                [6] + BD1[1:],
                                [7] + BD1[1:],
                                [8] + BD1[1:],
                                [9] + BD1[1:]]

# Board -> (listof Board)
# produce list of valid next boards from board
# finds first empty square, fills it with Natural[1, 9], keeps only valid boards
def next_boards(bd):
    return keep_only_valid(fill_with_1_9(find_blank(bd), bd))

assert next_boards([1] + BD1[1:]) == [[1, 2] + BD1[2:],
                                    [1, 3] + BD1[2:],
                                    [1, 4] + BD1[2:],
                                    [1, 5] + BD1[2:],
                                    [1, 6] + BD1[2:],
                                    [1, 7] + BD1[2:],
                                    [1, 8] + BD1[2:],
                                    [1, 9] + BD1[2:]]


# Board -> Board or False
# produce a solution for bd; or False if bd is unsolvable
# Assume: bd is valid
def solve(bd):
    def solve_bd(bd):
        if is_solved(bd):
            return bd
        return solve_lobd(next_boards(bd))
            
    def solve_lobd(lobd):
        if lobd == []:
            return False
        attempt = solve_bd(lobd[0])
        if attempt:
            return attempt
        return solve_lobd(lobd[1:])
        
    return solve_bd(bd)

assert solve(BD4) == BD4s
assert solve(BD5) == BD5s
assert solve(BD7) == False

def print_bd(bd):
    for row in range(9):
        for col in range(9):
            print(bd[row_col_to_pos(row, col)] or "_", end=" ")
            if col in [2, 5]:
                print("| ", end="")
        print()
        if row in [2, 5]:
            print("-" * 21)

print_bd(BD4)
print()
print_bd(BD4s)

if __name__ == "__main__":
    print("passed all")