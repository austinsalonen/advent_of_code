from collections import Counter
from functools import reduce
import math

def load_deltas(input):
	with open(input) as f:
		ns = sorted([int(line) for line in f.readlines()])
		ns = [0, *ns, ns[-1] + 3]
		return [b-a for a,b in zip(ns, ns[1:])]

def differences(ns):
	cs = Counter(ns)
	return cs[1] * cs[3]

def arrangements(ns):
	"""
	prime factors of 19208 lead to the "tribonacci" dict;
	only needed up to trib(4)
	"""
	trib = {0: 1, 1: 1, 2: 2, 3: 4, 4: 7}
	count = 1
	one_seq = 0

	for n in ns:
		if n == 1:
			one_seq += 1
		if n == 3:
			count *= trib[one_seq]
			one_seq = 0

	return count

	# # one-liner...
	# return reduce(lambda c, n: (c[0]*trib[c[1]], 0) if n == 3 else (c[0], c[1]+1), ns, (1,0))[0]

t0 = load_deltas('day10.test0')
t1 = load_deltas('day10.test1')

assert 35 == differences(t0)
assert 220 == differences(t1)

assert 8 == arrangements(t0)
assert 19208 == arrangements(t1)

real = load_deltas('day10.input')
print('part 1 =', differences(real))
print('part 2 =', arrangements(real))