def read_categories(filename):
	from ast import literal_eval as literal_eval
	with open(filename, 'r') as file:
		line = file.readline()
		
	return literal_eval(line)
	
def categories_to_numbers(categories, category_labels):
	cat_numbers = []
	for label in category_labels:
		
		number_binstring = "".join(["1" if c == label else "0" for c in categories])
		number = int(number_binstring, 2)
		
		cat_numbers.append(number)
	return cat_numbers

def get_binstr(n, min_bits = 0):
    return format(n, 'b').zfill(min_bits)
	
def write_numbers(filename, numbers):
	with open(filename, 'w') as file:
		file.write(str(numbers))
	return None
	
categories = read_categories("NW.txt")
cat_numbers = categories_to_numbers(categories, [0, 1, 2, 3])
write_numbers("NW number.txt", cat_numbers)