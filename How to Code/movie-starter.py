# PROBLEM A:

# Design a data definition to represent a movie, including  
# title, budget, and year released.

# To help you to create some examples, find some interesting movie facts below: 
# "Titanic" - budget: 200000000 released: 1997
# "Avatar" - budget: 237000000 released: 2009
# "The Avengers" - budget: 220000000 released: 2012

class Movie:

    def __init__(self, title, budget, year):
        self.title = title
        self.budget = budget
        self.year = year

m1 = Movie("Titanic", 200000000, 1997)
m2 = Movie("Avatar", 237000000, 2009)
m3 = Movie("The Avengers", 220000000, 2012)

# PROBLEM B:

# You have a list of movies you want to watch, but you like to watch your 
# rentals in chronological order. Design a function that consumes two movies 
# and produces the title of the most recently released movie.

# Note that the rule for templating a function that consumes two compound data 
# parameters is for the template to include all the selectors for both 
# parameters.

def recent(ma, mb):
    if ma.year > mb.year:
        return ma.title
    return mb.title

assert recent(m1, m2) == "Avatar"
assert recent(m2, m3) == "The Avengers"
assert recent(m3, m1) == "The Avengers"
print("passed")