thing = [1, 2, 3, 4, 5, 6, 7, 6, 5, 4]
this = [2, -2, 2, -2, -2, -2, 2, -2, 2, 2]
def auto(shift):
	result = 0
	newthing = thing[-shift:] + thing[0:len(thing) - shift] 
	for i in range(0, len(thing)):
		result += this[i]*newthing[i]
	return result