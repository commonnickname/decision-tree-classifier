#generates unique orderings of length n

def combinations(n, k=0):
    if n > 1:
        for res in combinations(n-1, k):
            yield [k] + res
        for res in combinations(n-1, k+1):
            yield [k] + res
    else:
        yield [k]
		
		
from itertools import permutations as permutations

def all_combinations(n):
	X = (x for combs in combinations(n) for x in set(permutations(combs)))
	return sorted(X)
	
def save_orderings(orderings, filename):
	with open(filename, 'w', newline = '') as nf:
		for ordering in orderings:
			if list(ordering) != sorted(ordering):
				nf.write(','.join((str(x) for x in ordering)) + '\n' )
	
	return 0
	
n = int(input("Enter N: "))
Arrays = list(all_combinations(n))	

for l in Arrays: print(l)

print("Number of unique orderings: " + str(len(Arrays)))

save_orderings(Arrays, "orderings.csv")

