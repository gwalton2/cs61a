from math import factorial
def dorm(n, r):
	r_holder = 3
	prob = 1
	while (r_holder <= r):
		prob *= (n-r_holder)/(n-2)
		r_holder+=1
	print ("brute force:", prob)
	print("our solution:", sol(n, r))


def sol(n, r):
	return factorial(n-3)/(factorial(n-r-1)*((n-2)**(r-2)))