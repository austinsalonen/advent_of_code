import networkx as nx

def edges(path):
	with open(path) as f:
		for edge in f.readlines():
			yield edge.strip().split(')')

def graph(path):
	G = nx.Graph()

	for pr in edges(path):
		G.add_edge(*pr)

	return G

def minimal_orbital_transfers(g, you='YOU', santa='SAN'):
	return len(nx.shortest_path(g, you, santa)) - 3 

def orbit_count(orbits):
	return sum(len(nx.shortest_path(orbits, n, 'COM')) - 1 for n in orbits.nodes())

test = graph('day06.test')

assert 54 == orbit_count(test)

orbits = graph('day06.input')

print('part 1 =', orbit_count(orbits))
print('part 2 =', minimal_orbital_transfers(orbits))

