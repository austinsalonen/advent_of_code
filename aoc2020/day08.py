from copy import copy

def parse(line):
	[cmd, arg] = line.split()
	return (cmd, int(arg))

def load(path):
	with open(path) as f:
		return [parse(line.strip()) for line in f.readlines()]

def accumulator_before_loop(cmds, on_loop, on_eof):
	visited = set()
	acc, pos = 0, 0

	while True:
		if pos in visited:
			return on_loop(acc)

		if pos >= len(cmds):
			return on_eof(acc)

		cmd, n = cmds[pos]
		visited.add(pos)

		if cmd == 'nop':
			pos += 1

		if cmd == 'acc':
			pos += 1
			acc += n

		if cmd == 'jmp':
			pos += n


def copy_flip(cmds, i):
	cs = copy(cmds)
	(c,n) = cs[i]

	cs[i] = ('jmp', n) if c == 'nop' else ('nop', n)

	return cs

def terminating(cmds):
	copies = [copy_flip(cmds, i) for i,c in enumerate(cmds) if c[0] == 'nop' or c[0] == 'jmp']
	return max([accumulator_before_loop(c, lambda x: -10000, lambda x: x) for c in copies])

test = load('day08.test')

assert 5 == accumulator_before_loop(test, lambda x: x, lambda x: None)
assert 8 == terminating(test)

real = load('day08.input')
print('part 1 =', accumulator_before_loop(real, lambda x: x, lambda x: None))
print('part 2 =', terminating(real))