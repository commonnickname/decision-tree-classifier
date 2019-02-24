class Rule:
	def __init__(self, label, number):
		self.label = label
		self.number = number
		
	def combineOr(self, rule):
		new_label = self.label + " or " + rule.label
		new_number = self.number | rule.number
		return Rule(new_label, new_number)
		
	def combineAnd(self, rule):
		new_label = self.label + " and " + rule.label
		new_number = self.number & rule.number
		return Rule(new_label, new_number)
		
	def negation(self, nmask):
		return self.number ^ nmask
		
	def __str__(self):
		return self.label + ", " + str(self.number)


def get_atoms(filename):
	from csv import reader as reader
	with open(filename, 'r') as f:
		return [Rule(l, int(n)) for l, n in reader(f)]

def unique_generator(seeds, atoms, S):
	from itertools import product as product
	if not seeds:
		for atom in atoms:
			if atom.number not in S and atom.negation(nmask) not in S:
				S.add(atom.number)
				yield atom
	else:
		for (seed, atom) in product(seeds, atoms):
			ruleOR = seed.combineOr(atom)
			if ruleOR.number not in S and atom.negation(nmask) not in S:
				S.add(ruleOR.number)
				yield ruleOR
			ruleAND = seed.combineAnd(atom)
			if ruleAND.number not in S and atom.negation(nmask) not in S:
				S.add(ruleAND.number)
				yield ruleAND
				
def generate_rules(atoms, iterations):
	S = set()
	L1, L2 = [], []
	L = []
	for _ in range(iterations):
		L2 = [rule for rule in unique_generator(L1, atoms, S)]
		L += L2
		L1, L2 = L2[:], []
		
	return L
	
def store_rules(filename, rules):
	pass
	
	
	
	
atoms = get_atoms('atoms.csv')

search_depth = int(input("Enter search depth: "))

sortings_amount = 67
nmask = 2**sortings_amount - 1
rules = generate_rules(atoms, search_depth)
for rule in rules:
	print(rule)
	
print(len(rules))
	
