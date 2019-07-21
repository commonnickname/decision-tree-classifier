#reads orderings
def get_orderings(csv_filename):
	import csv
	with open(csv_filename, 'r') as csv_file:
		csv_reader = csv.reader(csv_file)
		RAW_DATA = list(csv_reader)
	csv_file.close()
	DATA = []
	for rd in RAW_DATA:
		DATA.append([int(i) for i in rd])
	return DATA
	
#writes rules
def write_rules(TESTS, RESULTS, filename):
	with open(filename, 'w', newline = '') as nf:
		nf.write(', '.join(TESTS))
		nf.write('\n')
		nf.write(', '.join([str(r) for r in RESULTS]))
	nf.close()	
	return 0

#auto-generates a list of tests
#as the tests are going to be used in meta-programming way, the name of the list variable is required
def test_generator(tuple_list_name, tuple_dimention):
	from itertools import combinations as combinations
	tests = []
	operators = ["==", "!=", "> ", "<=", "< ", ">="]
	test_template = tuple_list_name + "[{}] {} " + tuple_list_name + "[{}]"
	
	#for each operator check all unique pairs 
	for op in operators:
		for first, second in combinations(range(tuple_dimention), 2):
			tests.append(test_template.format(str(first), op, str(second)))
	
	return tests
	
def perform_tests(DATA, TESTS):
	test_results = []

	for t in TESTS:
		#convert the series of booleans into a binary number string
		result_binstring = "".join(["1" if eval(t) else "0" for X in DATA])
		
		#binary number strings -> integer
		result_number = int(result_binstring, 2)
		
		test_results.append(result_number)
		
	return test_results

	

DATA = get_orderings("orderings.csv") 		#read orderings
TESTS = test_generator("X", len(DATA[0])) 	#generate tests
RESULTS = perform_tests(DATA, TESTS)		#get numeric results

for t, r in zip(TESTS, RESULTS):
	print(t + ": " + str(r))

write_rules(TESTS, RESULTS, "atomic_rules.txt")



		
