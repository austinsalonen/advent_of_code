import networkx as nx

def child(c):
	if c.startswith('no other'): return [None, 0]
	[count, a, b, rest] = c.strip().split(' ')
	return f'{a} {b}', count

def edges(line):
	[parent, children] = line.split(' bags contain ')

	return [(parent, *child(c)) for c in children.split(',')]

def input(path):
	with open(path) as f:
		return [rule for line in f.readlines() for rule in edges(line.strip())]

def parents_graph(bags):
	g = nx.DiGraph()

	for (a,b,_) in bags:
		if b == None: continue
		g.add_edge(b,a)

	return g	

def at_least_one(g, child):
	for n in nx.neighbors(g, child):
		yield n

		for m in at_least_one(g, n):
			yield m

def contents_graph(bags):
	g = nx.DiGraph()

	for (a,b,c) in bags:
		g.add_edge(a,(b,int(c)))

	return g

def total_bags(g, child):
	for (c0, count) in nx.neighbors(g, child):
		yield 0 if c0 == None else count + sum(b*count for b in total_bags(g, c0))

def total_bag_count(g, child):
	return sum(n for n in total_bags(g, child))

test = input('day07.test')
g = parents_graph(test)
assert 4 == sum(1 for _ in set(at_least_one(g, 'shiny gold')))
g = contents_graph(test)
assert 32 == total_bag_count(g, 'shiny gold')

test1 = input('day07.test1')
g = contents_graph(test1)
assert 126 == total_bag_count(g, 'shiny gold')

real = input('day07.input')
g = parents_graph(real)
print('part 1 =', sum(1 for _ in set(at_least_one(g, 'shiny gold'))))

contents = contents_graph(real)
print('part 2 =', total_bag_count(contents, 'shiny gold'))