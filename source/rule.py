class Rule:
	nmask = 1
	length = 1
	
	def __init__(self, number, label=None, ):
		if label == None:
			self.label = '? *'
		else:
			self.label = label
		self.number = number

	def combineOr(self, rule):
		new_label = self.label + " or " + rule.label
		new_number = self.number | rule.number
		return Rule(new_number, new_label)
		
	def combineAnd(self, rule):
		new_label = self.label + " and " + rule.label
		new_number = self.number & rule.number
		return Rule(new_number, new_label)
		
	def solveOr(self, rule):
		from bsolver import orSolver as orSolver
		solutions = []
		for solution in orSolver(rule.number, self.number, Rule.length):
			new_label = '? * ' + rule.label + " or " + self.label[4:]
			solutions.append(Rule(solution, new_label))
		return solutions
		
	def solveAnd(self, rule):
		from bsolver import andSolver as andSolver
		solutions = []
		for solution in andSolver(rule.number, self.number, Rule.length):
			new_labe = '? * ' + rule.label + " and " + self.label[4:]
			solutions.append(Rule(solution, new_label))
		return solutions
		
	def negation(self):
		return self.number ^ Rule.nmask
		
	def __eq__(self, other):
		if not isinstance(other, type(self)): return NotImplemented
		return (self.number == other.number) or (self.negation() == other.number)
	
	def __hash__(self):
		return hash(self.number * self.negation())
		
		
	def __str__(self):
		return self.label + ", " + str(self.number)
		
	def __repr__(self):
		return self.label + " - " + str(self.number)