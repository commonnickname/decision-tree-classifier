from rule import Rule as Rule

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
				
				
Rule.length = 6
Rule.nmask = 2**6 - 1


goals = [Rule(9)]
atoms = [Rule(8, "con1-8"), Rule(10, "con2-10"), Rule(12, "con3-12"), Rule(3, "ncon3-3"), Rule(7, "ncon1-7"), Rule(5, "ncon2-5")]


blist, bset = goals[:], set(goals)
bfrom, bto = 0, len(goals)
for i in range(5):
	print("iteration " + str(i))
	for brule in bgenerator(blist[bfrom:bto], atoms, bset):
		print("        found " + str(brule))
		blist.append(brule)
	bfrom, bto = bto, len(blist)
	
print("="*10)
for r in blist: print(r)
		
		
