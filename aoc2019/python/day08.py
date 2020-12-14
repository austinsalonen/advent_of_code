def load(path):
	with open(path) as f:
		return f.read().strip()

def chunks(lst, n):
    """Yield successive n-sized chunks from lst."""
    for i in range(0, len(lst), n):
        yield lst[i:i + n]

def chunked(xs, w, h):
	return list(chunks(list(chunks(xs, w)), h))

def char_count(xs, c):
	return ''.join(xs).count(c)	

def fewest_zeros(xs):
	return sorted(xs, key=lambda x: char_count(x, '0'))[0]

def ones_by_twos(xs):
	return char_count(xs, '1') * char_count(xs, '2')

def merge(a, b):
	ax = list(map(list, a))

	for x in range(0, len(a)):
		for y in range(0, len(a[x])):
			if ax[x][y] != '2': continue

			ax[x][y] = b[x][y]

	return list(''.join(r) for r in ax)

def layer(xs):
	final = xs[0]

	for x in xs:
		final = merge(final, x)

	for r in final:
		print(''.join(['#' if c == '1' else ' ' for c in r]))
		# print(''.join(r))

	return final

print(layer(chunked('0222112222120000', 2, 2)))
assert ['01', '10'] == layer(chunked('0222112222120000', 2, 2))

pixels = load('day08.input')
chunked = chunked(pixels, 25, 6)
print('part 1 =', ones_by_twos(fewest_zeros(chunked)))
print('part 2 =', layer(chunked))