from itertools import product, compress
from math import log2, floor

OrTable = ((	(0,),	(1,)	),
			(	(),		(0,1)	))
		
AndTable = ((	(0,1),	()		),
			(	(0,),	(1,)	))


def intlen(num):
	if num == 0: return 1
	return floor(log2(num)) + 1
	
def bits(num, length=0):
	if length == 0: length = intlen(num)
	return [(num >> i) & 1 for i in range(length - 1, -1, -1)]
	
def bits_to_int(bits):
	out = 0
	for bit in bits: 
		out = (out << 1) | bit
	return out
	
#returns a number constructed from bits of source, specified by mask
def bitmask(source, mask):
	sbits = bits(source)
	mbits = bits(mask)
	lendiff = abs(len(mbits) - len(sbits))
	a = (lendiff if len(sbits) < len(mbits) else 0)
	b = (lendiff if len(sbits) > len(mbits) else 0)
	sbits = [0] * a + sbits[b:]

	return bits_to_int(compress(sbits, mbits))

	
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

