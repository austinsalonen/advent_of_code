import re
from collections import defaultdict

def parse(line):
	if line.startswith('mask ='):
		return ('mask', line[6:])

	mems = re.split('\[|\]|=| ', line)

	return ('mem', (int(mems[1]), int(mems[-1])))

def load(path):
	with open(path) as f:
		return [parse(l.strip()) for l in f.readlines()]

def masked_value(v, m):
	masked, n = 0, 1
	for c in m[::-1]:
		if c == '1':
			masked |= n

		if c == 'X' and (v & n) == n:
			masked |= n

		n <<= 1

	return masked

def masked_idx(m, idx):
	masked, n = [0], 1

	for c in m[::-1]:
		if c == '1':
			masked = [x | n for x in masked]

		if c == 'X':
			masked = [x | n for x in masked] + [x for x in masked]

		if c == '0':
			masked = [x | (n & idx) for x in masked]

		n <<= 1

	return masked


def version1(cmds):
	memory = defaultdict(int)
	mask = ''

	for c, a in cmds:
		if c == 'mask':
			mask = a
			continue

		idx, val = a

		memory[idx] = masked_value(val, mask)

	return sum(memory.values())

assert set([26,27,58,59]) == set(masked_idx('000000000000000000000000000000X1001X', 42))

def version2(cmds):
	memory = defaultdict(int)
	mask = ''

	for c, a in cmds:
		if c == 'mask':
			mask = a
			continue

		idx, val = a

		for i in masked_idx(mask, idx):
			memory[i] = val

	return sum(memory.values())

t = load('day14.test')
assert 165 == version1(t)
t = load('day14.test1')
assert 208 == version2(t)

real = load('day14.input')
print('part 1 =', version1(real))
print('part 2 =', version2(real))