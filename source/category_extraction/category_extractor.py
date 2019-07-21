#reads orderings
def read_sortings(filename):
	from ast import literal_eval as literal_eval
	with open(filename, 'r') as file:
		lines = [line.strip() for line in file.readlines()] 

	return [literal_eval("[" + line + "]") for line in lines]
	
def write_sorting(filename, sorting):
	with open(filename, 'w', newline = '') as nf:
		nf.write(str(sorting))
	nf.close()
	
	
	return None
	
def extract_sample_sorting(sortings):
	return [s[0] for s in sortings]
	
def extract_position_sorting(single_sorting, position):
	return [s[position] for s in single_sorting]
	
	
	
DATA = read_sortings("compact_sortings.csv")
SAMPLE_SORTING = extract_sample_sorting(DATA)
SORTING = extract_position_sorting(SAMPLE_SORTING, 1)

write_sorting("NW.txt", SORTING)