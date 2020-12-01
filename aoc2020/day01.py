from collections import Counter

inputs = []

with open('day01.input') as f:
	inputs = [int(x) for x in f.readlines()]

def most_common(xs):
	return Counter(xs).most_common(1)[0][0]

def part1(ns):
	return most_common([n * (2020-n) for n in ns])

def part2(ns):
	return most_common([a*b*c for a in ns for b in ns for c in ns if a+b+c == 2020])

print(part1(inputs))
print(part2(inputs))

