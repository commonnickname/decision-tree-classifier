def negate(number):
	return number ^ nmask

def fgenerator(seeds, atoms, S):
	if not seeds:
		for atom in atoms:
			if atom not in S and negate(atom) not in S: 
				S.add(atom)
				yield atom
		return
	from itertools import product as product
	for seed, atom in product(seeds, atoms):
		ruleOR = seed | atom
		if ruleOR not in S and negate(ruleOR) not in S:
			S.add(ruleOR)
			yield ruleOR
		ruleAND = seed & atom
		if ruleAND not in S and negate(ruleAND) not in S:
			S.add(ruleAND)
			yield ruleAND
	
def bgenerator(goals, atoms, S):
	if not goals: return
	
	from itertools import product as product
	from bsolver import orSolver, andSolver
	for goal, atom in product(goals, atoms):
		for ruleOR in orSolver(atom, goal, length):
			if ruleOR not in S and negate(ruleOR) not in S:
				S.add(ruleOR)
				yield ruleOR
		for ruleAND in andSolver(atom, goal, length):
			if ruleAND not in S and negate(ruleAND) not in S:
				S.add(ruleAND)
				yield ruleAND
	

	
def collisions(seeds, goals, atoms, iterations):
	
	flist, fset = seeds[:], set(seeds)
	ffrom, fto = 0, len(seeds)
	
	blist, bset = goals[:], set(goals)
	bfrom, bto = 0, len(goals)
	
	for i in range(iterations//2):
		print("iteration: " + str(i))
		print("flist: " + str(flist))
		print("blist: " + str(blist))
		
		print("    forward generation: ")
		for frule in fgenerator(flist[ffrom:fto], atoms, fset):
			print("        found " + str(frule))
			if frule in bset or negate(frule) in bset: 
				print("found match")
				if frule in bset:
					print(str(frule) + " matches directly")
				else:
					print("negation of " + str(frule) + " = " + str(negate(frule)) + " matches blist")
				return frule
			flist.append(frule)
		ffrom, fto = fto, len(flist)
		
		
		if ffrom == fto: 
			print("    no new rules in forward generation found, returning")
			return None
		else:
			print("    new frules: " + str(flist))
		
		print("    backward generation: ")
		for brule in bgenerator(blist[bfrom:bto], atoms, bset):
			print("        found " + str(brule))
			if brule in fset or negate(brule) in fset: 
				print("found match")
				if brule in fset:
					print(str(brule) + " matches directly")
				else:
					print("negation of " + str(brule) + " = " + str(negate(brule)) + " matches flist")
				return brule
			blist.append(brule)
		bfrom, bto = bto, len(blist)
		if bfrom == bto: 
			print("    no new rules in backward generation found, returning")
			return None
		else:
			print("    new brules: " + str(blist))
		
	return None
	

length = 5	
nmask = 2**length - 1

seeds = []
atoms = [8, 10, 12, 3, 7, 5]
goals = [9]


print(collisions(seeds, goals, atoms, 8))
