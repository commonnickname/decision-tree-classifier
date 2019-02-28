from itertools import product as product

OrTable = ((	(0,),	(1,)	),
			(	(),		(0,1)	))
		
AndTable = ((	(0,1),	()		),
			(	(0,),	(1,)	))

def bits(num, length):
	return [(num >> i) & 1 for i in range(length - 1, -1, -1)]
	
def bits_to_int(bits):
	out = 0
	for bit in bits: 
		out = (out << 1) | bit
	return out

def bincut(source):
	l = 5

	return bits(source, l)
	
	
	
#generates all x < 2^l, such that num | x == res
def orSolver(num, res, l):
	L = (OrTable[n][r] for n, r in zip(bits(num, l), bits(res, l)))
	for m in product(*L): 
		yield bits_to_int(m)
	
#generates all x < 2^l, such that num & x == res
def andSolver(num, res, l):
	L = (AndTable[n][r] for n, r in zip(bits(num, l), bits(res, l)))
	for m in product(*L): 
		yield bits_to_int(m)
		
		
		
print(bincut(8))



	
