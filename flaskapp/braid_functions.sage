

### Braidlet


#This is how you initialize braid groups/elements:

B4 = BraidGroup(4)
# x = B4([1,2,1]) # will be printed as s0*s1*s0. note the different indexing conventions (which I think can be changed). 

## IMOPRTANT: make sure the elements are in the right braid groups.
##            things get screwey if you input two braids in B4 and B5, say.


def equal(b1,b2):
	return b1 == b2



def conjugacy_problem(b1,b2):
	if b1.is_conjugated(b2):
		conj = b2.conjugating_braid(b1)
		toReturn = str(b1) + " and " + str(b2) + " are conjugate and (" + str(conj) + ") * " + str(b1) + " * (" + str(conj) + ")^-1"
		return toReturn
	else:
		return str(b1) + " is not conjugate to " +  str(b2)


## Tests:

# s1=B4([1])
# s2=B4([2])

# print(conjugacy_problem(s1,s2))
# print(conjugacy_problem(s1,x))


def lcm(b1,b2):
	return "lcm("+str(b1)+","+str(b2)") = " str(b1.lcm(b2))


def gcd(b1,b2):
	return "gcd("+str(b1)+","+str(b2)") = " str(b1.gcd(b2))









