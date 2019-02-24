from rule import Rule as Rule

def get_atoms(filename):
	from csv import reader as reader
	with open(filename, 'r') as f:
		return [Rule(l, int(n)) for l, n in reader(f)]

def unique_generator(seeds, atoms, S):
	from itertools import product as product
	if not seeds:
		for atom in atoms:
			if atom not in S:
				S.add(atom)
				yield atom
	else:
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
	S = set()
	L1, L2 = [], []
	L = []
	for _ in range(iterations):
		L2 = [rule for rule in unique_generator(L1, atoms, S)]
		L += L2
		print(len(L2))
		L1, L2 = L2[:], []
		
	return L
	
def store_rules(filename, rules):
	pass
	
	
	
	
	
numof_sortings = 67
Rule.nmask = 2**numof_sortings - 1
search_depth = int(input("Enter search depth: "))

atoms = get_atoms('atoms.csv')
rules = generate_rules(atoms, search_depth)

for rule in rules:
	print(rule)
	
print(len(rules))
