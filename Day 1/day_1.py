directions = open("input.txt").read()

# Solution for Part 1
floor = 0
for direction in directions:
	floor += 1 if direction == '(' else -1
print floor

# Solution for Part 2
floor = 0
for index, direction in enumerate(directions):
	floor += 1 if direction == '(' else -1
	if floor == -1:
		print index + 1
		break
