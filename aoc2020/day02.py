import re
from collections import Counter

def parse(line):
	[rng, c, pwd] = [w for w in re.split(' |:|\n', line) if w != '']
	[mn, mx] = rng.split('-')
	return (int(mn), int(mx), c, pwd)

def input(path):
	with open(path) as f:
		return [parse(line) for line in f.readlines()]

def min_max_chars(pwds):
	return sum([1 for mn, mx, c, pwd in pwds if mn <= Counter(pwd)[c] <= mx])

def char_in_exactly_one_of_the_positions(pwds):
	return sum([1 for p0, p1, c, pwd in pwds if (pwd[p0-1] == c) ^ (pwd[p1-1] == c)])

test_input = input('day02.test')
real_input = input('day02.input')

assert 2 == min_max_chars(test_input)
assert 1 == char_in_exactly_one_of_the_positions(test_input)

print('part 1 = ', min_max_chars(real_input))
print('part 2 = ', char_in_exactly_one_of_the_positions(real_input))

