from functools import reduce

def grouped(path):
	g = []
	with open(path) as f:
		for line in f.readlines():
			line = line.strip()
			if line == '':
				yield g
				g = []
				continue

			g.append(set(line))

	yield g


def answers(given):
	return sum(len(reduce(set.union, xs)) for xs in given)

def common_yes(given):
	return sum(len(reduce(set.intersection, xs)) for xs in given)

gs = list(grouped('day06.input'))
print('part 1 =', answers(gs))
print('part 2 =', common_yes(gs))
