from math import log2 as log2

def read_rules(filename):
	with open(filename, 'r') as file:
		rules = [int(l) for l in file.readlines()]	
	return rules
	
def read_numbers(filename):
	from ast import literal_eval as literal_eval
	with open(filename, 'r') as file:
		line = file.readline().strip()
	return literal_eval(line)
	
def is_single_category(categories):
	amount = 0
	for c in categories:
		amount += c > 0
	return amount == 1
	
def get_nonzero_category(categories):
	cat_labels = [0, 1, 2, 3]
	for i in range(len(categories)):
		if categories[i] != 0: 
			return cat_labels[i]
	return None
	
def countSetBits(n): 
	count = 0
	while (n): 
		count += n & 1
		n >>= 1
	return count 
	
def entropy(categories):
	bits = [countSetBits(c) for c in categories]
	total = sum(bits)
	L = [b/total * log2(b/total) if b != 0 else 0 for b in bits]
	return -sum(L)

def split(categories, rule):
	nmask = 2**67 - 1
	categoriesT = [rule & c for c in categories]
	categoriesF = [(nmask ^ rule) & c for c in categories]
	return categoriesT, categoriesF
	
def number_of_instances(categories):
	bits = [countSetBits(c) for c in categories]
	return sum(bits)
	
	
def information_gain(categories, rule):
	#heavy time optimization here!
	prior_entropy = entropy(categories)
	categoriesT, categoriesF = split(categories, rule)
	total_instances = number_of_instances(categories) 
	trueFactor = entropy(categoriesT) * number_of_instances(categoriesT) / total_instances
	falseFactor = entropy(categoriesF) * number_of_instances(categoriesF) / total_instances
	return prior_entropy - trueFactor - falseFactor
	


	
def classify(categories, offset):
	#check base cases
	if is_single_category(categories):
		print(offset + str(get_nonzero_category(categories)))
		return

	global RULES
	
	
	

	best_index, best_gain = None, 0
	for i, R in enumerate(RULES):
		current_gain = information_gain(categories, R)
		if current_gain > best_gain:
			best_index, best_gain = i, current_gain

		
	categoriesT, categoriesF = split(categories, RULES[best_index])
	print(offset + str(RULES[best_index]) + ":")
	classify(categoriesT, offset + "    ")
	print(offset + "else:")
	classify(categoriesF, offset + "    ")
	
	return
	
	
	
RULES = read_rules("new_coumpound_rules 4i.txt")
categories = read_numbers("NW number.txt")


classify(categories, "")
	
	
	
	
	
	
	
