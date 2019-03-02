from rule import Rule as Rule
	
def fgenerator(seeds, atoms, S):
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

def bgenerator(goals, atoms, S):
	if not goals: return
	
	from itertools import product as product
	for goal, atom in product(goals, atoms):
		for orSolution in goal.solveOr(atom):
			if orSolution not in S:
				S.add(orSolution)
				yield orSolution
		for andSolution in goal.solveAnd(atom):
			if andSolution not in S:
				S.add(andSolution)
				yield andSolution
	
def test_collisions(seeds, goals, atoms, iterations):
	print(atoms)
	
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
			if frule in bset: 
				print(str(frule) + " matches")
				return frule
			flist.append(frule)
		ffrom, fto = fto, len(flist)
		
		
		if ffrom == fto: 
			print("    no new rules in forward generation found, returning")
			return None
		else:
			print("    found " + str(fto - ffrom) + " new frules")
		
		print("    backward generation: ")
		for brule in bgenerator(blist[bfrom:bto], atoms, bset):
			print("        found " + str(brule))
			if brule in fset: 
				print(brule + " matches")
				return brule
			blist.append(brule)
		bfrom, bto = bto, len(blist)
		if bfrom == bto: 
			print("    no new rules in backward generation found, returning")
			return None
		else:
			print("    found " + str(bto - bfrom) + " new brules")
		
	return None
	
	
	return None
	
'''	
def get_rules(filename):
	from csv import reader as reader
	with open(filename, 'r') as f:
		return [Rule(l, int(n)) for l, n in reader(f)]
	
def get_goals(filename):
	return []

seeds = get_rules("filename")
atoms = get_rules("filename")
goals = get_goals("filename")
'''

seeds = []
atoms = [Rule(8, "con1-8"), Rule(10, "con2-10"), Rule(12, "con3-12"), Rule(3, "ncon3-3"), Rule(7, "ncon1-7"), Rule(5, "ncon2-5")]
goals = [Rule(9)]

Rule.length = 4
Rule.nmask = 2**4 - 1
iterations = 8

print(test_collisions(seeds, goals, atoms, iterations))