#generates ways to sort orderings (compacted)

def get_orderings(filename):
	import csv
	orderings = []
	with open(filename, 'r') as csv_file:
		csv_reader = csv.reader(csv_file)
		orderings = list(csv_reader)
	
	iorderings = []
	for ordering in orderings:
		io = []
		for o in ordering:
			io.append(int(o))
		iorderings.append(io)
	return iorderings

def pfunction(source, indices):
	return [source[i] for i in indices]

def getSortings(ordering):
	from itertools import permutations as permutations
	
	pseed = [i for i in range(len(ordering))]
	S = []
	sorted_ordering = sorted(ordering)
	if (ordering == sorted_ordering): return None
	for p in permutations(pseed):
		if pfunction(ordering, p) == sorted_ordering:
			S.append(p)
	return S

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

#save_sortings('compact_sortings2.csv', sortings)

for s in sortings:
	print(s)
	
print(extractor(sortings,0))
print(extractor(sortings,1))
print(extractor(sortings,2))
print(extractor(sortings,3))

