from functools import reduce

def pairs(line):
	for kvp in line.split():
		yield kvp.split(':')

def passports(path):
	ppt = {}

	with open(path) as f:
		for line in f.readlines():
			line = line.strip()
			if line == '':
				yield ppt
				ppt = {}

			for k,v in pairs(line):
				ppt[k] = v

		yield ppt

def check_keys(ppt):
	required_fields = set(['byr','iyr','eyr','hgt','hcl','ecl','pid','cid'])
	return (required_fields - set(ppt.keys())) in [set(), set(['cid'])]

def valid_passports(ppts, f):
	return sum(1 for ppt in ppts if f(ppt))

def extra_checks(ppt):
	def check_height(x):
		if x.endswith('cm'):
			return 150 <= int(x[:-2]) <= 193
		if x.endswith('in'):
			return 59 <= int(x[:-2]) <= 76
		return False

	cs = {
		'byr': lambda x: 1920 <= int(x) <= 2002,
		'iyr': lambda x: 2010 <= int(x) <= 2020,
		'eyr': lambda x: 2020 <= int(x) <= 2030,
		'hgt': lambda x: check_height(x),
		'hcl': lambda x: x[0] == '#' and set('0123456789abcdef') >= set(x[1:]) ,
		'ecl': lambda x: x in set(['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']),
		'pid': lambda x: len(x) == 9 and set() == set(x) - set('0123456789'),
		'cid': lambda x: True
	}

	return check_keys(ppt) and all(cs[k](v) for k,v in ppt.items())

real_input = list(passports('day04.input'))
test_input = passports('day04.test')
invalid = passports('day04.invalid')
valid = passports('day04.valid')

assert 2 == valid_passports(test_input, check_keys)
assert 0 == valid_passports(invalid, extra_checks)
assert 4 == valid_passports(valid, extra_checks)

print('part 1 = ', valid_passports(real_input, check_keys))
print('part 2 = ', valid_passports(real_input, extra_checks))
