
def program(path):
	with open(path) as f:
		return [int(n) for l in f.readlines() for n in l.strip().split(',')]

def run(prg, input=None, output=None):
	i = 0
	while True:
		# addition

		if prg[i] == 1:
			prg[prg[i+3]] = prg[prg[i+1]] + prg[prg[i+2]]
			i += 4
			continue

		if prg[i] ==   101:
			prg[prg[i+3]] = prg[i+1] + prg[prg[i+2]]
			i += 4
			continue

		if prg[i] ==  1001:
			prg[prg[i+3]] = prg[prg[i+1]] + prg[i+2]
			i += 4
			continue

		if prg[i] ==  1101:
			prg[prg[i+3]] = prg[i+1] + prg[i+2]
			i += 4
			continue

		if prg[i] == 10001:
			prg[i+3] = prg[prg[i+1]] + prg[prg[i+2]]
			i += 4
			continue

		if prg[i] == 10101:
			prg[i+3] = prg[i+1] + prg[prg[i+2]]
			i += 4
			continue

		if prg[i] == 11001:
			prg[i+3] = prg[prg[i+1]] + prg[i+2]
			i += 4
			continue

		if prg[i] == 11101:
			prg[i+3] = prg[i+1] + prg[i+2]
			i += 4
			continue

		# multiplication
		if prg[i] == 2:
			prg[prg[i+3]] = prg[prg[i+1]] * prg[prg[i+2]]
			i += 4
			continue

		if prg[i] ==   102:
			prg[prg[i+3]] = prg[i+1] * prg[prg[i+2]]
			i += 4
			continue

		if prg[i] ==  1002:
			prg[prg[i+3]] = prg[prg[i+1]] * prg[i+2]
			i += 4
			continue

		if prg[i] ==  1102:
			prg[prg[i+3]] = prg[i+1] * prg[i+2]
			i += 4
			continue

		if prg[i] == 10002:
			prg[i+3] = prg[prg[i+1]] * prg[prg[i+2]]
			i += 4
			continue

		if prg[i] == 10102:
			prg[i+3] = prg[i+1] * prg[prg[i+2]]
			i += 4
			continue

		if prg[i] == 11002:
			prg[i+3] = prg[prg[i+1]] * prg[i+2]
			i += 4
			continue

		if prg[i] == 11102:
			prg[i+3] = prg[i+1] * prg[i+2]
			i += 4
			continue

		# input
		if prg[i] == 3:
			prg[prg[i+1]] = input()
			i += 2
			continue

		# output
		if prg[i] == 4:
			output(prg[prg[i+1]])
			i += 2
			continue

		if prg[i] == 104:
			output(prg[i+1])
			i += 2
			continue

		# Opcode 5 is jump-if-true: if the first parameter is non-zero, 
		# it sets the instruction pointer to the value from the second 
		# parameter. Otherwise, it does nothing.
		if prg[i] ==    5:
			if prg[prg[i+1]] != 0:
				i = prg[prg[i+2]]
			else:
				i += 3
			continue

		if prg[i] ==  105:
			if prg[i+1] != 0:
				i = prg[prg[i+2]]
			else:
				i += 3
			continue

		if prg[i] == 1005:
			if prg[prg[i+1]] != 0:
				i = prg[i+2]
			else:
				i += 3
			continue

		if prg[i] == 1105:
			if prg[i+1] != 0:
				i = prg[i+2]
			else:
				i += 3
			continue
	
		# Opcode 6 is jump-if-false: if the first parameter is zero, 
		# it sets the instruction pointer to the value from the second 
		# parameter. Otherwise, it does nothing.
		if prg[i] ==    6:
			if prg[prg[i+1]] == 0:
				i = prg[prg[i+2]]
			else:
				i += 3
			continue

		if prg[i] ==  106:
			if prg[i+1] == 0:
				i = prg[prg[i+2]]
			else:
				i += 3
			continue

		if prg[i] == 1006:
			if prg[prg[i+1]] == 0:
				i = prg[i+2]
			else:
				i += 3
			continue

		if prg[i] == 1106:
			if prg[i+1] == 0:
				i = prg[i+2]
			else:
				i += 3
			continue

		# Opcode 7 is less than: if the first parameter 
		# is less than the second parameter, it stores 1 
		# in the position given by the third parameter. 
		# Otherwise, it stores 0.

		if prg[i] ==     7:
			if prg[prg[i+1]] < prg[prg[i+2]]:
				prg[prg[i+3]] = 1
			else:
				prg[prg[i+3]] = 0
			i+= 4
			continue

		if prg[i] ==   107:
			if prg[i+1] < prg[prg[i+2]]:
				prg[prg[i+3]] = 1
			else:
				prg[prg[i+3]] = 0
			i+= 4
			continue

		if prg[i] ==  1007:
			if prg[prg[i+1]] < prg[i+2]:
				prg[prg[i+3]] = 1
			else:
				prg[prg[i+3]] = 0
			i+= 4
			continue

		if prg[i] ==  1107:
			if prg[i+1] < prg[i+2]:
				prg[prg[i+3]] = 1
			else:
				prg[prg[i+3]] = 0
			i+= 4
			continue

		if prg[i] == 10007:
			if prg[prg[i+1]] < prg[prg[i+2]]:
				prg[i+3] = 1
			else:
				prg[i+3] = 0
			i+= 4
			continue

		if prg[i] == 10107:
			if prg[i+1] < prg[prg[i+2]]:
				prg[i+3] = 1
			else:
				prg[i+3] = 0
			i+= 4
			continue

		if prg[i] == 11007:
			if prg[prg[i+1]] < prg[i+2]:
				prg[i+3] = 1
			else:
				prg[i+3] = 0
			i+= 4
			continue

		if prg[i] == 11107:
			if prg[i+1] < prg[i+2]:
				prg[i+3] = 1
			else:
				prg[i+3] = 0
			i+= 4
			continue

		# Opcode 8 is equals: if the first parameter is 
		# equal to the second parameter, it stores 1 in 
		# the position given by the third parameter. 
		# Otherwise, it stores 0.

		if prg[i] ==     8:
			if prg[prg[i+1]] == prg[prg[i+2]]:
				prg[prg[i+3]] = 1
			else:
				prg[prg[i+3]] = 0
			i+= 4
			continue

		if prg[i] ==   108:
			if prg[i+1] == prg[prg[i+2]]:
				prg[prg[i+3]] = 1
			else:
				prg[prg[i+3]] = 0
			i+= 4
			continue

		if prg[i] ==  1008:
			if prg[prg[i+1]] == prg[i+2]:
				prg[prg[i+3]] = 1
			else:
				prg[prg[i+3]] = 0
			i+= 4
			continue

		if prg[i] ==  1108:
			if prg[i+1] == prg[i+2]:
				prg[prg[i+3]] = 1
			else:
				prg[prg[i+3]] = 0
			i+= 4
			continue

		if prg[i] == 10008:
			if prg[prg[i+1]] == prg[prg[i+2]]:
				prg[i+3] = 1
			else:
				prg[i+3] = 0
			i+= 4
			continue

		if prg[i] == 10108:
			if prg[i+1] == prg[prg[i+2]]:
				prg[i+3] = 1
			else:
				prg[i+3] = 0
			i+= 4
			continue

		if prg[i] == 11008:
			if prg[prg[i+1]] == prg[i+2]:
				prg[i+3] = 1
			else:
				prg[i+3] = 0
			i+= 4
			continue

		if prg[i] == 11108:
			if prg[i+1] == prg[i+2]:
				prg[i+3] = 1
			else:
				prg[i+3] = 0
			i+= 4
			continue

		# EOP
		if prg[i] == 99:
			break;

		print(f'unexpected command: {prg[i]}')
		break

