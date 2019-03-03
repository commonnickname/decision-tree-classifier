from rule import Rule as Rule
	
def setget(set_, rule):
	for x in set_:
		if x == rule:
			return x
	return None
	
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
	print("ATOMS:")
	print(atoms)
	print("GOALS:")
	print(goals)
	
	
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
			#print("        found " + str(frule))
			if frule in bset: 
				print(str(frule) + " matches " + str(setget(bset, frule)))
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
			#print("        found " + str(brule))
			if brule in fset: 
				print(str(frule) + " matches " + str(setget(fset, brule)))
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
	

def get_rules(filename):
	
	from csv import reader as reader
	with open(filename, 'r') as f:
		return [Rule(int(n), l) for l, n in reader(f)]
	
def get_goals(filename):
	a = [1,1,2,2,2,3,3,1,1,2,3,2,2,2,3,3,2,3,2,2,2,3,0,0,3,0,0,0,0,3,0,0,0,0,3,0,0,0,0,0,0,0,0,2,3,2,2,2,3,3,3,1,1,1,1,1,1,3,2,3,2,2,3,1,1,3,2]
	L = []
	from itertools import combinations as combinations
	for n1, n2 in combinations(list(range(4)), 2):
		b = ''.join(['0' if x in [n1, n2] else '1' for x in a])
		L.append(Rule(int(b, 2)))

	return L


seeds = []
atoms = get_rules("atoms.csv")
goals = get_goals("filename")

Rule.length = 67
Rule.nmask = 2**67 - 1
iterations = 8



print(test_collisions(seeds, goals, atoms, iterations))