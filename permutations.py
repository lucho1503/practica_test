from itertools import permutations
def per(nu):
	c = ""
	list_set = list(permutations(range(1, nu)))
	for s in list_set:
		for n in s:
			c += str(n)

	sep = [c[i:i+nu-1] for i in range(o, len(c))]
	return ", ".join(numero for numero in sep)


#per(4)
#per(5)