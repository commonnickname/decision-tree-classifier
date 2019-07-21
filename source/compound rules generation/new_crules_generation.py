#read in data
def read_data(filename):
	with open(filename, 'r') as file:
		lines = file.readlines()
		lines = [l.strip() for l in lines] 
		LABELS = lines[0].split(', ')
		ATOMS = [int(x) for x in lines[1].split(', ')]
	return LABELS, ATOMS

#save new data
def save_data(filename, DATA):
	with open(filename, 'w', newline = '\n') as nf:
		for d in DATA:
			nf.write(str(d) + "\r\n")
	return None
			
#goes through all pairs of seeds and atoms and tries to combine them, outputs only if the result is not in S
#if the seed list is empty then it tries to just iterate over atoms
def forward_generator(seeds, atoms, S):
	from itertools import product as product
	
	if not seeds:
		for atom in atoms:
			if atom not in S and atom ^ nmask not in S:
				S.add(atom)
				#print("Forward generator: " + str(atom))
				yield atom
	else:
		for (seed, atom) in product(seeds, atoms):
			ruleOR = seed | atom
			if ruleOR not in S and ruleOR ^ nmask not in S:
				S.add(ruleOR)
				#print("Forward generator: " + str(ruleOR))
				yield ruleOR
			ruleAND = seed & atom
			if ruleAND not in S and ruleAND ^ nmask not in S:
				S.add(ruleAND)
				#print("Forward generator: " + str(ruleAND))
				yield ruleAND
		
def stage_generator(ATOMS, iterations):
	from itertools import islice as islice 
	L, S, new_amount = [], set(), 0

	for i in range(iterations):
		print("iteration: " + str(i + 1) + " start")
		
		#possible memory optimization by replacing the list slice with a generator
		L += [X for X in forward_generator(L[len(L) - new_amount:], ATOMS, S)] 
		new_amount = len(L) - new_amount
		
		print("iteration: " + str(i + 1) + " done, new rules: " + str(new_amount) + ", total rules: " + str(len(L)))

	return L
	
	
LABELS, ATOMS = read_data("atomic_rules.txt")

nmask = 2**67 - 1

iterations = 6
LIST = stage_generator(ATOMS, iterations)

save_data("new_coumpound_rules 6i.txt", LIST)
