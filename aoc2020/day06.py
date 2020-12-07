def answers(path):
	groups = []
	group = set()
	with open(path) as f:
		for line in f.readlines():
			ans = line.strip()

			if ans == '':
				groups.append(group)
				group = set()
				continue

			group = group | set(ans)


	groups.append(group)
	return groups

def common_yes(path):
	groups = []
	group = set('abcdefghijklmnopqrstuvwxyz')
	with open(path) as f:
		for line in f.readlines():
			ans = line.strip()

			if ans == '':
				groups.append(group)
				group = set('abcdefghijklmnopqrstuvwxyz')
				continue

			group = group & set(ans)


	groups.append(group)
	return groups

print('part 1 =', sum(len(g) for g in answers('day06.input')))
print('part 2 =', sum(len(g) for g in common_yes('day06.input')))