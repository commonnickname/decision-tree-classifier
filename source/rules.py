from rule import Rule as Rule

def get_rules(filename):
	from csv import reader as reader
	with open(filename, 'r') as f:
		return [Rule(int(n), l) for l, n in reader(f)]

def forward_generator(seeds, atoms, S):
	if not seeds:
		for atom in atoms:
			if atom not in S:
				S.add(atom)
				yield atom
		return

	from itertools import product as product
	for (seed, atom) in product(seeds, atoms):
		ruleOR = seed.combineOr(atom)
		if ruleOR not in S:
			S.add(ruleOR)
			yield ruleOR
		ruleAND = seed.combineAnd(atom)
		if ruleAND not in S:
			S.add(ruleAND)
			yield ruleAND
				
				
def generate_rules(atoms, iterations):
	L, S = [], set()
	_from, to = 0, 0
	for _ in range(iterations):
		L += [rule for rule in forward_generator(L[_from:to], atoms, S)]
		_from, to = to, len(L)
		print(to - _from)
		
	return L
	
def store_rules(filename, rules):
	with open(filename, 'w', newline = '') as nf:
		for rule in rules:
			nf.write(str(rule) + '\n')

	
	
numof_sortings = 67
Rule.nmask = 2**numof_sortings - 1
search_depth = int(input("Enter search depth: "))

atoms = get_rules('atoms.csv')
rules = generate_rules(atoms, search_depth)

#for rule in rules:
#	print(rule)
	
store_rules("4rules.csv", rules)
print(len(rules))
