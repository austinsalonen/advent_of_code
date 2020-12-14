from copy import deepcopy

def layout(path):
	with open(path) as f:
		return [(line.strip()) for line in f.readlines()]

def occupied(layout):
	return sum(1 for row in layout for c in row if c == '#')

def neighbors(g, r, c):
	rmx, cmx = len(g), len(g[r])

	ns = [(x,y) for x in range(r-1, r+2) for y in range(c-1, c+2) if x >= 0 and y >= 0 and x < rmx and y < cmx and (x,y) != (r,c)]

	return sum(1 for (x,y) in ns if g[x][y] == '#')

def first_visible(g, r, c):
	rmx, cmx = len(g), len(g[r])

	def inc(n): return n+1
	def dec(n): return n-1
	def nop(n): return n

	def find_seat(dx, dy):
		x, y = dx(r), dy(c)
		while True:
			if x < 0 or x >= rmx: return None
			if y < 0 or y >= cmx: return None

			if g[x][y] != '.': return (x,y)

			x, y = dx(x), dy(y)

	f = find_seat
	ns = [p for p in [f(dec, inc), f(dec, nop), f(dec, dec), f(nop, inc), f(nop, dec), f(inc, inc), f(inc, nop), f(inc, dec)] if p != None]

	return sum(1 for (x,y) in ns if g[x][y] == '#')

def apply_rule(a,b, rule, seats):
	for r in range(0, len(b)):
		for c in range(0, len(b[r])):
			if b[r][c] == '.':
				a[r][c] = '.'

			if b[r][c] == 'L' and rule(b, r, c) == 0:
				a[r][c] = '#'

			if b[r][c] == '#' and rule(b, r, c) >= seats:
				a[r][c] = 'L'


def stable(layout, rule, seats):
	a, b = deepcopy(layout), layout

	while True:
		apply_rule(a, b, rule, seats)

		if a == b:
			return a

		b = deepcopy(a)

test = layout('day11.test')

assert 37 == occupied(stable(test, neighbors, 4))
assert 26 == occupied(stable(test, first_visible, 5))

real = layout('day11.input')
print('part 1 =', occupied(stable(real, neighbors, 4)))
print('part 2 =', occupied(stable(real, first_visible, 5)))