def module_masses(path):
	with open(path) as f:
		return [int(line.strip()) for line in f.readlines()]

real_input = module_masses('day01.input')

def fuel_counter_upper(masses):
	return sum(-2 + m//3 for m in masses)

def fuel_required(mass):
	req = mass//3 - 2
	if req <= 0:
		return

	yield req
	for f in fuel_required(req):
		yield f

def include_fuel_mass(masses):
	return sum(f for m in masses for f in fuel_required(m))

assert 2 == sum(fuel_required(14))
assert 966 == sum(fuel_required(1969))

print('part 1 = ', fuel_counter_upper(real_input))
print('part 2 = ', include_fuel_mass(real_input))