from binsolver import bits_to_int as bits_to_int

def get_orderings(csv_filename):
	from csv import reader as reader
	with open(csv_filename, 'r') as f:
		RAW_DATA = list(reader(f))
	return [[int(i) for i in rd] for rd in RAW_DATA]
	
def save_atoms(filename, labels, rules):
	with open(filename, 'w', newline='') as nf:
		for label, rule in zip(labels, rules):
			nf.write(label + ", " + str(rule) + '\n')

def get_rule(orderings, rule):
	bits = [eval(rule) for x in orderings]
	return bits_to_int(bits)
	
LABELS = [  
		"m1 == m2", "m1 == m3", "m1 == m4", "m2 == m3", "m2 == m4", "m3 == m4",
		"m1 != m2", "m1 != m3", "m1 != m4", "m2 != m3", "m2 != m4", "m3 != m4",
		"m1 >  m2", "m1 >  m3", "m1 >  m4", "m2 >  m3", "m2 >  m4", "m3 >  m4",
		"m1 <= m2", "m1 <= m3", "m1 <= m4", "m2 <= m3", "m2 <= m4", "m3 <= m4",
		"m1 <  m2", "m1 <  m3", "m1 <  m4", "m2 <  m3", "m2 <  m4", "m3 <  m4",
		"m1 >= m2", "m1 >= m3", "m1 >= m4", "m2 >= m3", "m2 >= m4", "m3 >= m4"	]
		
RULES = [  	
		'x[0] == x[1]', 'x[0] == x[2]', 'x[0] == x[3]', 'x[1] == x[2]', 'x[1] == x[3]', 'x[2] == x[3]',
		'x[0] != x[1]', 'x[0] != x[2]', 'x[0] != x[3]', 'x[1] != x[2]', 'x[1] != x[3]', 'x[2] != x[3]',
		'x[0] >  x[1]', 'x[0] >  x[2]', 'x[0] >  x[3]', 'x[1] >  x[2]', 'x[1] >  x[3]', 'x[2] >  x[3]',
		'x[0] <= x[1]', 'x[0] <= x[2]', 'x[0] <= x[3]', 'x[1] <= x[2]', 'x[1] <= x[3]', 'x[2] <= x[3]',
		'x[0] <  x[1]', 'x[0] <  x[2]', 'x[0] <  x[3]', 'x[1] <  x[2]', 'x[1] <  x[3]', 'x[2] <  x[3]',
		'x[0] >= x[1]', 'x[0] >= x[2]', 'x[0] >= x[3]', 'x[1] >= x[2]', 'x[1] >= x[3]', 'x[2] >= x[3]'	]
		
orderings = get_orderings("orderings.csv")

NRULES = [get_rule(orderings, r) for r in RULES]
	
save_atoms("atoms.csv", LABELS, NRULES)