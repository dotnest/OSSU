# ; Problem 1:
# ; 
# ; Suppose you have rosters for players on two opposing tennis team, and each
# ; roster is ordered by team rank, with the best player listed first. When both 
# ; teams play, the best players of each team play one another,
# ; and the second-best players play one another, and so on down the line. When
# ; one team has more players than the other, the lowest ranking players on
# ; the larger team do not play.
# ; 
# ; Design a function that consumes two rosters, and produces true if all players 
# ; on both teams will play if the teams play each other. 
# ; No marks will be given to solution that do not use a cross product table. 

# ;; Player is String
# ;; interp.  the name of a tennis player.
P0 = "Maria"
P2 = "Serena"

# ;; Roster is one of:
# ;; - empty
# ;; - (cons Player Roster)
# ;; interp.  a team roster, ordered from best player to worst.
R0 = []
R1 = ["Eugenie", "Gabriela", "Sharon", "Aleksandra"]
R2 = ["Maria", "Nadia", "Elena", "Anastasia", "Svetlana"]

class Match:

    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
    
    def __repr__(self):
        return f"A match between {self.p1} and {self.p2}"
    
    def __eq__(self, other):
        try:
            return (self.p1, self.p2) == (other.p1, other.p2)
        except AttributeError:
            return NotImplemented


# ;; Match is (make-match Player Player)
# ;; interp.  a match between player p1 and player p2, with same team rank
M0 = Match("Eugenie", "Maria")
M1 = Match("Gabriela", "Nadia")

# ;; ListOfMatch is one of:
# ;; - empty
# ;; - (cons Match ListOfMatch)
# ;; interp. a list of matches between one team and another.
LOM0 = []
LOM1 = [Match("Eugenie", "Maria"), Match("Gabriela", "Nadia")]

# ;; Roster Roster -> Boolean
# ;; returns true if all players on both teams will play if the teams play each other, else false
def allPlay(r1, r2):
    if not r1 and not r2:
        return True
    if not r1 or not r2:
        return False
    return allPlay(r1[1:], r2[1:])

assert allPlay(R0, R0) == True
assert allPlay(R1, R0) == False
assert allPlay(R0, R1) == False
assert allPlay(R1, R2) == False
assert allPlay(R2, R2) == True
print("passed allPlay")

# ; Problem 2:
# ; 
# ; Now write a function that, given two teams, produces the list of tennis matches
# ; that will be played. 
# ; 
# ; Assume that this function will only be called if the function you designed above
# ; produces true. In other words, you can assume the two teams have the same number
# ; of players. 

# ;; Roster Roster -> ListOfMatch
# ;; produces the list of tennis matches that will be played between two rosters/teams
def matches(r1, r2):
    if r1 == []:
        return []
    return [Match(r1[0], r2[0])] + matches(r1[1:], r2[1:])

R3 = ["Eugenie"]
R4 = ["Maria"]
R5 = ["Eugenie", "Gabriela", "Sharon", "Aleksandra"]
R6 = ["Maria", "Nadia", "Elena", "Anastasia"]

assert matches([], []) == []
assert matches(R3, R4) == [Match("Eugenie", "Maria")] + []
assert matches(R5, R6) == [Match("Eugenie", "Maria"),
                            Match("Gabriela", "Nadia"),
                            Match("Sharon", "Elena"),
                            Match("Aleksandra", "Anastasia")]
print("passed matches")