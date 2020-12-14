# import int_code as IC
from int_code import IntCode, program
from copy import copy
from itertools import permutations

# def tracefunc(frame, event, arg, indent=[0]):
#       if event == "call":
#           indent[0] += 2
#           print("-" * indent[0] + "> call function", frame.f_code.co_name)
#       elif event == "return":
#           print("<" + "-" * indent[0], "exit function", frame.f_code.co_name)
#           indent[0] -= 2
#       return tracefunc

# import sys
# # sys.setprofile(tracefunc)
# sys.settrace(tracefunc)

def amplifiers(prg, xs):
	comps = [IntCode(copy(prg), [xs[i]]) for i in range(5)]

	previous_output = 0
	for x in comps:
		x.add_input(previous_output)
		previous_output = x.run()

	return comps[-1].output


def feedback_loop(prg, xs):
	thrusters = [IntCode(copy(prg), [xs[i]]) for i in range(5)]
	previous_output = 0
	mx = 0
	while all(not t.halted for t in thrusters):
		for t in thrusters:
			t.add_input(previous_output)
			previous_output = t.run()
			mx = max(mx, previous_output) if previous_output else mx

	return mx


def max_thrusters(f, prg, vals):
	return max(f(prg, ps) for ps in permutations(vals))


test0 = amplifiers([3,15,3,16,1002,16,10,16,1,16,15,15,4,15,99,0,0], [4, 3, 2, 1, 0])
assert 43210 == test0, test0
test1 = amplifiers([3,23,3,24,1002,24,10,24,1002,23,-1,23,101,5,23,23,1,24,23,23,4,23,99,0,0], [0,1,2,3,4])
assert 54321 == test1
test2 = amplifiers([3,31,3,32,1002,32,10,32,1001,31,-2,31,1007,31,0,33,1002,33,7,33,1,33,31,31,1,32,31,31,4,31,99,0,0,0],[1,0,4,3,2])
assert 65210 == test2
assert 139629729 == feedback_loop([3,26,1001,26,-4,26,3,27,1002,27,2,27,1,27,26,27,4,27,1001,28,-1,28,1005,28,6,99,0,0,5], [9, 8, 7, 6, 5])

prg = program('day07.input')
print('part 1 =', max_thrusters(amplifiers, prg, [0,1,2,3,4]))
print('part 2 =', max_thrusters(feedback_loop, prg, [5,6,7,8,9]))
