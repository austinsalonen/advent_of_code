test0 = [[('R', 8),('U', 5),('L', 5),('D', 3)], [('U', 7),('R', 6),('D', 4),('L', 4)]]
test1 = [[('R', 75),('D', 30),('R', 83),('U', 83),('L', 12),('D', 49),('R', 71),('U', 7),('L', 72)], [('U', 62),('R', 66),('U', 55),('R', 34),('D', 71),('R', 55),('D', 58),('R', 83)]]

def load(path):
	with open(path) as f:
		for line in f.readlines():
			yield [(x[0], int(x[1:])) for x in line.strip().split(',')]

def points(ds, x, y):
	for direction, distance in ds:
		if direction == 'R':
			for n in range(1, distance+1):
				yield (x+n, y)
			x += distance
		if direction == 'L':
			for n in range(1, distance+1):
				yield (x-n, y)
			x -= distance
		if direction == 'U':
			for n in range(1, distance+1):
				yield (x, y+n)
			y += distance
		if direction == 'D':
			for n in range(1, distance+1):
				yield (x, y-n)
			y -= distance


def closest(x0, x1):
	pts0 = set(points(x0, 0, 0))
	pts1 = set(points(x1, 0, 0))

	return min(abs(x) + abs(y) for x,y in (pts0 & pts1))

def shortest(x0, x1):
	pts0 = list(points(x0, 0, 0))
	pts1 = list(points(x1, 0, 0))

	return min(pts0.index(pt) + pts1.index(pt) + 2 for pt in (set(pts0) & set(pts1)))

assert 6 == closest(*test0)
assert 159 == closest(*test1)
assert 30 == shortest(*test0)

real = list(load('day03.input'))

print('part 1 =', closest(*real))
print('part 2 =', shortest(*real))