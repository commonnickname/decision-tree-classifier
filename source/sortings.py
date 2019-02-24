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

def extractor(sortings, index):
	
	from itertools import product as product
	L = []
	for sorting in sortings:
		L.append(list(set([s[index] for s in sorting])))
	s = 1
	for l in L:
		s *= len(l)
	'''
	for l in product(*L):
		#print(l)
		s *= len(l)
	'''

	return s
	
def save_sortings(filename, sortings):
	with open(filename, 'w', newline = '') as nf:
		for sorting in sortings:
			nf.write(', '.join(str(s) for s in sorting) + '\n')
	
	return 0
	
	
orderings = get_orderings('orderings.csv')
sortings = [getSortings(x) for x in orderings]

save_sortings('sortings.csv', sortings)

for s in sortings:
	print(s)
	
print(extractor(sortings,0))
print(extractor(sortings,1))
print(extractor(sortings,2))
print(extractor(sortings,3))

