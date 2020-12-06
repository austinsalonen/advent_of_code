from int_code import run, program
from copy import copy

buffer = []
prg = [3,0,4,0,99]
run(prg, input=lambda: 1, output=buffer.append)

assert [1] == buffer


prg = program('day05.input')

output = []
run(copy(prg), input=lambda: 1, output=output.append)

print('part 1 =', output[-1])

output = []
run(copy(prg), input=lambda: 5, output=output.append)

print('part 2 =', output[-1])