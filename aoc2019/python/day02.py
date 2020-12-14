from int_code import program, IntCode
from copy import copy

def run(p1, p2):
	p = program('day02.input')
	p = [p[0]] + [p1, p2] + p[3:]
	c = IntCode(p)
	c.run()
	return c.get(0)

print('part 1 =', run(12, 2))

def search_for(desired, path):
	for n in range(0,100):
		for v in range(0,100):
			if run(n, v) == desired:
				return n*100 + v

print('part 2 =', search_for(19690720, 'day02.input') )

# part 1 = 2894520
# part 2 = 9342
# [Finished in 1.2s]