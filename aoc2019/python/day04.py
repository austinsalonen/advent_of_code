from functools import reduce

def run_length_encode(num):
	def rle(acc, c):
		if acc and acc[-1][0] == c:
			c,n = acc[-1]
			acc[-1] = (c, n+1)
		else:
			acc.append((c,1))

		return acc

	return reduce(rle, str(num), [])

assert [('1', 6)] == run_length_encode(111111)

def never_decrease(x):
	return all(a[0] <= b[0] for a,b in zip(x, x[1:]))

def is_valid(encoded):
	def has_pair(ns):
		return any(n >= 2 for c,n in ns)

	return has_pair(encoded) and never_decrease(encoded)

def not_including_triples(encoded):
	def has_pair(ns):
		return any(n == 2 for c,n in ns)

	return has_pair(encoded) and never_decrease(encoded)

assert is_valid(run_length_encode(111111))
assert not is_valid(run_length_encode(223450))
assert not is_valid(run_length_encode(123789))
assert not not_including_triples(run_length_encode(111111))
assert not_including_triples(run_length_encode(111122))

print('part 1 =', sum(1 for n in range(353096, 843212) if is_valid(run_length_encode(n))))
print('part 2 =', sum(1 for n in range(353096, 843212) if not_including_triples(run_length_encode(n))))