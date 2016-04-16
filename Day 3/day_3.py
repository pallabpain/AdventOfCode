directions = open("input.txt").read()

# Solution to Day 3 Part 1
x, y = 0, 0

visited_houses = [[x, y]]

for direction in directions:

	if direction == '<':
		x -= 1
	elif direction == '>':
		x += 1
	elif direction == '^':
		y += 1
	elif direction == 'v':
		y -= 1

	if [x, y] not in visited_houses:
		visited_houses.append([x, y])

print len(visited_houses)

# Solution to Day 3 Part 2
santa = [0, 0]
robot = [0, 0]
visited_houses = [[0, 0]]
mover = 's'

for direction in directions:

	location = santa if mover == 's' else robot
	
	if direction == '<':
		location[0] -= 1
	elif direction == '>':
		location[0] += 1
	elif direction == '^':
		location[1] += 1
	elif direction == 'v':
		location[1] -= 1

	if location not in visited_houses:
		visited_houses.append([location[0], location[1]])

	mover = 'r' if mover == 's' else 's'

print len(visited_houses)