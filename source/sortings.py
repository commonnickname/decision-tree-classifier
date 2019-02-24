#generates ways to sort orderings (compacted)

def get_orderings(filename):
	from csv import reader as reader
	with open(filename, 'r') as f:
		return [[int(x) for x in order] for order in reader(f)]

def indexed(source, indices):
	return [source[i] for i in indices]

def getSortings(ordering):
	sorted_o = sorted(ordering)
	if ordering == sorted_o: return None
	
	from itertools import permutations as permutations
	perm = (p for p in permutations(range(len(ordering))))
	
	return [p for p in perm if indexed(ordering, p) == sorted_o]
	
def position_sortings(sortings, index):
	L = [list(set([s[index] for s in sorting])) for sorting in sortings]
	return L
	
def save_sortings(filename, sortings):
	with open(filename, 'w', newline = '') as nf:
		for sorting in sortings:
			nf.write(', '.join(str(s) for s in sorting) + '\n')

	
	
orderings = get_orderings('orderings.csv')
sortings = [getSortings(x) for x in orderings]

#save_sortings('sortings.csv', sortings)

for s in sortings:
	print(s)
	
for i in range(4):
	print("index: " + str(i))
	for ps in position_sortings(sortings, i):
		print(ps)
