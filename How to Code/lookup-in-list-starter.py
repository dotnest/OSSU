# PROBLEM:

# Complete the design of the lookup-name function below. Note that because this is a search function 
# it will sometimes 'fail'. This happens if it is called with an account number that does not exist
# in the accounts list it is provided. If this happens the function should produce false.

class Account:

	def __init__(self, num, name):
		self.num = num
		self.name = name

ACS1 = []
ACS2 = [Account(1, "abc"), Account(4, "dcj"), Account(3, "ilk"), Account(7, "ruf")]

def lookup(accs, n):
    if not accs:
        return False
    if accs[0].num == n:
        return accs[0].name
    else:
        return lookup(accs[1:], n)

assert lookup(ACS1, 1) == False
assert lookup(ACS2, 2) == False
assert lookup(ACS2, 4) == "dcj"
print("passed")