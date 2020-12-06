from collections import defaultdict

def row(seq):
	return int(''.join('0' if c == 'F' else '1' for c in seq[:-3]), 2)

def seat(seq):
	return int(''.join('0' if c == 'L' else '1' for c in seq[-3:]), 2)

def seat_id(seq):
	return int(''.join('0' if c in ['F', 'L'] else '1' for c in seq), 2)

assert 44 == row('FBFBBFFRLR')
assert 5 == seat('FBFBBFFRLR')
assert 357 == seat_id('FBFBBFFRLR')

def boarding_passes(path):
	with open(path) as f:
		return [line.strip() for line in f.readlines()]

def missing(passes):
	ps = [(row(p), seat(p)) for p in passes]
	seats = defaultdict(set)

	for r,s in ps:
		seats[r].add(s)

	full_row = set([0,1,2,3,4,5,6,7])
	r,s = [(r,s) for r,s in seats.items() if len(s) == 7][0]

	return r * 8 - list(full_row - s)[0]

passes = boarding_passes('day05.input')
print('part 1 =', max(seat_id(p) for p in passes))
print('part 2 =', missing(passes))