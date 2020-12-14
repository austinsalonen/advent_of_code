from int_code import program, IntCode
from copy import copy

prg = program('day05.input')

c = IntCode(prg, [1])
print('part 1 =', c.run())

c = IntCode(prg, [5])
print('part 2 =', c.run())

# part 1 = 6069343
# part 2 = 3188550
# [Finished in 0.6s]