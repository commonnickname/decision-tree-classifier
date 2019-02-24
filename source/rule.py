class Rule:
	nmask = 1
	
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
		
	def negation(self):
		return self.number ^ Rule.nmask
		
	def __eq__(self, other):
		if not isinstance(other, type(self)): return NotImplemented
		return (self.number == other.number) or (self.number ^ Rule.nmask == other.number)
	
	def __hash__(self):
		return hash(self.number * self.negation())
		
		
	def __str__(self):
		return self.label + ", " + str(self.number)