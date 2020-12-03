import math

def input(path):
	with open(path) as f:
		return [line.strip() for line in f.readlines()]

def trees_in_path(trees, right, down):
	x, tree_count = 0, 0

	for idx, line in enumerate(trees):
		if idx % down != 0: continue

		if line[x % len(line)] == '#': tree_count += 1

		x += right

	return tree_count


def many_slopes(slopes, trees):
	return math.prod([trees_in_path(trees, rt, dn) for rt, dn in slopes])

test_input = input('day03.test')
real_input = input('day03.input')
slopes = [(1,1), (3,1), (5,1), (7,1), (1,2)]

assert 7 == trees_in_path(test_input, 3, 1)
assert 5 == trees_in_path(test_input, 10, 1)

assert 336 == many_slopes(slopes, test_input)

print('part 1 = ', trees_in_path(real_input, 3, 1))
print('part 2 = ', many_slopes(slopes, real_input))