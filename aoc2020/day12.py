def parse(line):
	return line[0], int(line[1:])

def load(path):
	with open(path) as f:
		return [parse(line.strip()) for line in f.readlines()]

def manhattan(pos):
	return sum(map(abs,pos))

def apply(x,y,d,c,n):
	if c == 'R':
		return x,y,(d-n+360) % 360
	if c == 'L':
		return x,y,(d+n+360) % 360
	if c == 'N' or (c == 'F' and d == 90):
		return x+n,y,d
	if c == 'S' or (c == 'F' and d == 270):
		return x-n,y,d
	if c == 'E' or (c == 'F' and d == 0):
		return x,y+n,d
	if c == 'W' or (c == 'F' and d == 180):
		return x,y-n,d

def navigate(ds, x, y, d):
	for c, n in ds:
		x,y,d = apply(x,y,d,c,n)

	return x,y

def waypoint(ds, sx, sy, wx, wy):
	for c, n in ds:
		if c == 'N': wy += n
		elif c == 'S': wy -= n
		elif c == 'E': wx += n
		elif c == 'W': wx -= n
		elif c == 'F':
			sx += (wx*n)
			sy += (wy*n)
		else:
			if (n == 90 and c == 'R') or (n == 270 and c == 'L'):
				wx, wy = wy, -wx
			if n == 180:
				wx, wy = -wx, -wy
			if (n == 270 and c == 'R') or (n == 90 and c == 'L'):
				wx, wy = -wy, wx

	return sx,sy

test = load('day12.test')
assert 25 == manhattan(navigate(test, 0, 0, 0))
assert 286 == manhattan(waypoint(test, 0, 0, 10, 1))

real = load('day12.input')
print('part 1 =', manhattan(navigate(real, 0, 0, 0)))
print('part 2 =', manhattan(waypoint(real, 0, 0, 10, 1)))