from itertools import combinations
import math

def load(path):
	with open(path) as f:
		return [int(line.strip()) for line in f.readlines()]

def preamble(ns, i0, ix, cnt):
	return set([sum(ts) for ts in combinations(ns[i0:ix], cnt)])

def invalid_entry(ns, p_size, cnt):
	for i in range(p_size, len(ns)):
		if ns[i] not in preamble(ns, i-p_size, i, cnt):
			return ns[i]

def weakness(ns, goal):
	for i,n in enumerate(ns):
		s = n
		mn, mx = n, n

		for j in ns[(i+1):]:
			s += j
			mn = min(mn, j)
			mx = max(mx, j)

			if s > goal:
				break

			if s == goal:
				return mx + mn

test = load('day09.test')
assert 127 == invalid_entry(test, 5, 2)
assert 62 == weakness(test, 127)

real = load('day09.input')
p1 = invalid_entry(real, 25, 2)
print('part 1 =', p1)
print('part 2 =', weakness(real, p1))