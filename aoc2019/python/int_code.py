import functools

@functools.lru_cache(maxsize=1)
def program(path):
	with open(path) as f:
		return [int(n) for l in f.readlines() for n in l.strip().split(',')]

# def run(prg, input=None, output=None, on_halt=None):
# 	i = 0
# 	while True:
# 		# addition

# 		if prg[i] == 1:
# 			prg[prg[i+3]] = prg[prg[i+1]] + prg[prg[i+2]]
# 			i += 4
# 			continue

# 		if prg[i] ==   101:
# 			prg[prg[i+3]] = prg[i+1] + prg[prg[i+2]]
# 			i += 4
# 			continue

# 		if prg[i] ==  1001:
# 			prg[prg[i+3]] = prg[prg[i+1]] + prg[i+2]
# 			i += 4
# 			continue

# 		if prg[i] ==  1101:
# 			prg[prg[i+3]] = prg[i+1] + prg[i+2]
# 			i += 4
# 			continue

# 		if prg[i] == 10001:
# 			prg[i+3] = prg[prg[i+1]] + prg[prg[i+2]]
# 			i += 4
# 			continue

# 		if prg[i] == 10101:
# 			prg[i+3] = prg[i+1] + prg[prg[i+2]]
# 			i += 4
# 			continue

# 		if prg[i] == 11001:
# 			prg[i+3] = prg[prg[i+1]] + prg[i+2]
# 			i += 4
# 			continue

# 		if prg[i] == 11101:
# 			prg[i+3] = prg[i+1] + prg[i+2]
# 			i += 4
# 			continue

# 		# multiplication
# 		if prg[i] == 2:
# 			prg[prg[i+3]] = prg[prg[i+1]] * prg[prg[i+2]]
# 			i += 4
# 			continue

# 		if prg[i] ==   102:
# 			prg[prg[i+3]] = prg[i+1] * prg[prg[i+2]]
# 			i += 4
# 			continue

# 		if prg[i] ==  1002:
# 			prg[prg[i+3]] = prg[prg[i+1]] * prg[i+2]
# 			i += 4
# 			continue

# 		if prg[i] ==  1102:
# 			prg[prg[i+3]] = prg[i+1] * prg[i+2]
# 			i += 4
# 			continue

# 		if prg[i] == 10002:
# 			prg[i+3] = prg[prg[i+1]] * prg[prg[i+2]]
# 			i += 4
# 			continue

# 		if prg[i] == 10102:
# 			prg[i+3] = prg[i+1] * prg[prg[i+2]]
# 			i += 4
# 			continue

# 		if prg[i] == 11002:
# 			prg[i+3] = prg[prg[i+1]] * prg[i+2]
# 			i += 4
# 			continue

# 		if prg[i] == 11102:
# 			prg[i+3] = prg[i+1] * prg[i+2]
# 			i += 4
# 			continue

# 		# input
# 		if prg[i] == 3:
# 			prg[prg[i+1]] = input()
# 			i += 2
# 			continue

# 		# output
# 		if prg[i] == 4:
# 			output(prg[prg[i+1]])
# 			i += 2
# 			continue

# 		if prg[i] == 104:
# 			output(prg[i+1])
# 			i += 2
# 			continue

# 		# Opcode 5 is jump-if-true: if the first parameter is non-zero, 
# 		# it sets the instruction pointer to the value from the second 
# 		# parameter. Otherwise, it does nothing.
# 		if prg[i] ==    5:
# 			if prg[prg[i+1]] != 0:
# 				i = prg[prg[i+2]]
# 			else:
# 				i += 3
# 			continue

# 		if prg[i] ==  105:
# 			if prg[i+1] != 0:
# 				i = prg[prg[i+2]]
# 			else:
# 				i += 3
# 			continue

# 		if prg[i] == 1005:
# 			if prg[prg[i+1]] != 0:
# 				i = prg[i+2]
# 			else:
# 				i += 3
# 			continue

# 		if prg[i] == 1105:
# 			if prg[i+1] != 0:
# 				i = prg[i+2]
# 			else:
# 				i += 3
# 			continue
	
# 		# Opcode 6 is jump-if-false: if the first parameter is zero, 
# 		# it sets the instruction pointer to the value from the second 
# 		# parameter. Otherwise, it does nothing.
# 		if prg[i] ==    6:
# 			if prg[prg[i+1]] == 0:
# 				i = prg[prg[i+2]]
# 			else:
# 				i += 3
# 			continue

# 		if prg[i] ==  106:
# 			if prg[i+1] == 0:
# 				i = prg[prg[i+2]]
# 			else:
# 				i += 3
# 			continue

# 		if prg[i] == 1006:
# 			if prg[prg[i+1]] == 0:
# 				i = prg[i+2]
# 			else:
# 				i += 3
# 			continue

# 		if prg[i] == 1106:
# 			if prg[i+1] == 0:
# 				i = prg[i+2]
# 			else:
# 				i += 3
# 			continue

# 		# Opcode 7 is less than: if the first parameter 
# 		# is less than the second parameter, it stores 1 
# 		# in the position given by the third parameter. 
# 		# Otherwise, it stores 0.

# 		if prg[i] ==     7:
# 			if prg[prg[i+1]] < prg[prg[i+2]]:
# 				prg[prg[i+3]] = 1
# 			else:
# 				prg[prg[i+3]] = 0
# 			i+= 4
# 			continue

# 		if prg[i] ==   107:
# 			if prg[i+1] < prg[prg[i+2]]:
# 				prg[prg[i+3]] = 1
# 			else:
# 				prg[prg[i+3]] = 0
# 			i+= 4
# 			continue

# 		if prg[i] ==  1007:
# 			if prg[prg[i+1]] < prg[i+2]:
# 				prg[prg[i+3]] = 1
# 			else:
# 				prg[prg[i+3]] = 0
# 			i+= 4
# 			continue

# 		if prg[i] ==  1107:
# 			if prg[i+1] < prg[i+2]:
# 				prg[prg[i+3]] = 1
# 			else:
# 				prg[prg[i+3]] = 0
# 			i+= 4
# 			continue

# 		if prg[i] == 10007:
# 			if prg[prg[i+1]] < prg[prg[i+2]]:
# 				prg[i+3] = 1
# 			else:
# 				prg[i+3] = 0
# 			i+= 4
# 			continue

# 		if prg[i] == 10107:
# 			if prg[i+1] < prg[prg[i+2]]:
# 				prg[i+3] = 1
# 			else:
# 				prg[i+3] = 0
# 			i+= 4
# 			continue

# 		if prg[i] == 11007:
# 			if prg[prg[i+1]] < prg[i+2]:
# 				prg[i+3] = 1
# 			else:
# 				prg[i+3] = 0
# 			i+= 4
# 			continue

# 		if prg[i] == 11107:
# 			if prg[i+1] < prg[i+2]:
# 				prg[i+3] = 1
# 			else:
# 				prg[i+3] = 0
# 			i+= 4
# 			continue

# 		# Opcode 8 is equals: if the first parameter is 
# 		# equal to the second parameter, it stores 1 in 
# 		# the position given by the third parameter. 
# 		# Otherwise, it stores 0.

# 		if prg[i] ==     8:
# 			if prg[prg[i+1]] == prg[prg[i+2]]:
# 				prg[prg[i+3]] = 1
# 			else:
# 				prg[prg[i+3]] = 0
# 			i+= 4
# 			continue

# 		if prg[i] ==   108:
# 			if prg[i+1] == prg[prg[i+2]]:
# 				prg[prg[i+3]] = 1
# 			else:
# 				prg[prg[i+3]] = 0
# 			i+= 4
# 			continue

# 		if prg[i] ==  1008:
# 			if prg[prg[i+1]] == prg[i+2]:
# 				prg[prg[i+3]] = 1
# 			else:
# 				prg[prg[i+3]] = 0
# 			i+= 4
# 			continue

# 		if prg[i] ==  1108:
# 			if prg[i+1] == prg[i+2]:
# 				prg[prg[i+3]] = 1
# 			else:
# 				prg[prg[i+3]] = 0
# 			i+= 4
# 			continue

# 		if prg[i] == 10008:
# 			if prg[prg[i+1]] == prg[prg[i+2]]:
# 				prg[i+3] = 1
# 			else:
# 				prg[i+3] = 0
# 			i+= 4
# 			continue

# 		if prg[i] == 10108:
# 			if prg[i+1] == prg[prg[i+2]]:
# 				prg[i+3] = 1
# 			else:
# 				prg[i+3] = 0
# 			i+= 4
# 			continue

# 		if prg[i] == 11008:
# 			if prg[prg[i+1]] == prg[i+2]:
# 				prg[i+3] = 1
# 			else:
# 				prg[i+3] = 0
# 			i+= 4
# 			continue

# 		if prg[i] == 11108:
# 			if prg[i+1] == prg[i+2]:
# 				prg[i+3] = 1
# 			else:
# 				prg[i+3] = 0
# 			i+= 4
# 			continue

# 		# EOP
# 		if prg[i] == 99:
# 			if on_halt: on_halt()
# 			break;

# 		print(f'unexpected command: {prg[i]}')
# 		on_crash()
# 		break


# class Computer():
# 	def from_file(program_file, on_initialization=None):
# 		return Computer(program(program_file), on_initialization)

# 	def __init__(self, prg, on_initialization):
# 		self.program = prg
# 		if on_initialization: on_initialization(self.program)
# 		self.halted = False
# 		self.inputs = []
# 		self.outputs = []

# 	def run(self):
# 		self.halted = False
# 		def on_halt():
# 			self.halted = True
# 		run(self.program, lambda: self.inputs.pop(0), self.outputs.append, on_halt)
# 		return self.program[0]

# 	def input(self, n):
# 		self.inputs = [n] + self.inputs

class Instruction():
    code, argument_num = 0, 0
    def execute(self, comp, args):
        pass
    def update_counter(self, comp):
        return comp.pc + self.argument_num + 1

class Add(Instruction):
    code, argument_num = 1, 3
    def execute(self, comp, args):
        comp.set(args[2].address, args[0].value + args[1].value)
        return self.update_counter(comp)

class Multiply(Instruction):
    code, argument_num = 2, 3
    def execute(self, comp, args):
        comp.set(args[2].address, args[0].value * args[1].value)
        return self.update_counter(comp)

class Input(Instruction):
    code, argument_num = 3, 1
    def execute(self, comp, args):
        comp.set(args[0].address, comp.next_input())
        return self.update_counter(comp)

class Output(Instruction):
    code, argument_num = 4, 1
    def execute(self, comp, args):
        comp.output = args[0].value
        return self.update_counter(comp)

class JumpIfTrue(Instruction):
    code, argument_num = 5, 2
    def execute(self, comp, args):
        return args[1].value if args[0].value != 0 else self.update_counter(comp)

class JumpIfFalse(Instruction):
    code, argument_num = 6, 2
    def execute(self, comp, args):
        return args[1].value if args[0].value == 0 else self.update_counter(comp)

class LessThan(Instruction):
    code, argument_num = 7, 3
    def execute(self, comp, args):
        comp.set(args[2].address, int(args[0].value < args[1].value))
        return self.update_counter(comp)

class Equals(Instruction):
    code, argument_num = 8, 3
    def execute(self, comp, args):
        comp.set(args[2].address, int(args[0].value == args[1].value))
        return self.update_counter(comp)

class Halt(Instruction):
    code, argument_num = 99, 0
    def execute(self, comp, args):
        comp.halted = True
        return None

class Argument:
    def __init__(self, address, value):
        self.address = address
        self.value = value

    def __repr__(self):
        return f'Arg: address={self.address}; value={self.value}'

class IntCode():
    def __init__(self, prg, inputs=[]):
        self.program = prg[:]
        self.halted = False
        self.pc = 0
        self.inputs = inputs[::-1]
        self.output = None

    def run(self):
        self.output = None
        while not self.halted and self.output is None:
            inst = self._instruction(self.program[self.pc] % 100) 
            args = self._arguments(inst.argument_num)
            self.pc = inst().execute(self, args)
        return self.output

    def get(self, pos):
        return self.program[pos]

    def set(self, pos, value):
        self.program[pos] = value

    def _instruction(self, code):
        return next(cls for cls in Instruction.__subclasses__() if cls.code == code)

    def _arguments(self, argument_num):
        modes = str(self.program[self.pc]).zfill(5)[:3][::-1]
        args = []
        for i in range(argument_num):
            address = self.program[self.pc + i + 1]
            args.append(Argument(address, self.program[address] if modes[i] == '0' else address))
        return args

    def next_input(self):
        return self.inputs.pop()

    def add_input(self, n):
        self.inputs = [n] + self.inputs

test = IntCode([1,9,10,3,2,3,11,0,99,30,40,50])
assert None == test.run()
assert 3500 == test.get(0)

test = IntCode([3,0,4,0,99], [5])
assert 5 == test.run()
assert 5 == test.output

test = IntCode([3,9,8,9,10,9,4,9,99,-1,8], [8])
assert 1 == test.run()
test = IntCode([3,9,8,9,10,9,4,9,99,-1,8], [7])
assert 0 == test.run()