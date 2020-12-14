import math 
from functools import reduce

# https://rosettacode.org/wiki/Chinese_remainder_theorem#Python
def chinese_remainder(n, a):
    sum = 0
    prod = reduce(lambda a, b: a*b, n)
    for n_i, a_i in zip(n, a):
        p = prod // n_i
        sum += a_i * mul_inv(p, n_i) * p
    return sum % prod
 
def mul_inv(a, b):
    b0 = b
    x0, x1 = 0, 1
    if b == 1: return 1
    while a > 1:
        q = a // b
        a, b = b, a%b
        x0, x1 = x1 - q * x0, x0
    if x1 < 0: x1 += b0
    return x1
 

def notes(path):
	with open(path) as f:
		ls = [line.strip() for line in f.readlines()]
		return int(ls[0]), ls[1].split(',')

def wait_hash(tx, buses):
	return math.prod(min([(int(b) * (1 + tx // int(b)) - tx, int(b)) for b in buses if b != 'x']))

def earliest(xs):
	ms = [(int(n), (int(n)-inc)) for inc, n in enumerate(xs) if n != 'x']
	ns, mods = list(map(list, zip(*ms)))
	return chinese_remainder(ns, mods)

tx, buses = notes('day13.test')
buses = [int(x) for x in buses if x != 'x']

assert 295 == wait_hash(tx, buses)
assert 3417 == earliest([17,'x',13,19])
assert 754018 == earliest([67,7,59,61])
assert 779210 == earliest([67,'x',7,59,61])
assert 1261476 == earliest([67,7,'x',59,61])
assert 1202161486 == earliest([1789,37,47,1889])
assert 1068781 == earliest([7,13,'x','x',59,'x',31,19])

tx, buses = notes('day13.input')
print('part 1 =', wait_hash(tx, buses))
print('part 2 =', earliest(buses))
