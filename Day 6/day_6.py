instructions = [item.strip('\n') for item in open("input.txt").readlines()]

def get_coordinates(instruction):
	coordinates = instruction.split(" through ")
	coordinates = [[int(j) for j in i.split(',')] for i in coordinates]
	return coordinates

# Solution for Day 6 Part 1
grid = [[False for j in range(0, 1000)] for i in range(0, 1000)]

def perform_operation_part_1(instruction):	
	operation = ""	
	if "turn on" in instruction:
		operation = "turn on "
	elif "turn off" in instruction:
		operation = "turn off "
	elif "toggle" in instruction:
		operation = "toggle "
		
	coordinates = get_coordinates(instruction.replace(operation, ""))
	
	start = coordinates[0]
	end = coordinates[1]

	for x in range(start[0], end[0] + 1):
		for y in range(start[1], end[1] + 1):
			if operation == "turn on ":
				grid[x][y] = True
			elif operation == "turn off ":
				grid[x][y] = False
			elif operation == "toggle ":
				grid[x][y] = not grid[x][y]

for instruction in instructions:
	perform_operation_part_1(instruction)

lights_on = 0
for x in range(0, 1000):
	for y in range(0, 1000):
		if grid[x][y]:
			lights_on += 1

print lights_on

# Solution for Day 6 Part 2
grid = [[0 for j in range(0, 1000)] for i in range(0, 1000)]

def perform_operation_part_2(instruction):	
	operation = ""	
	if "turn on" in instruction:
		operation = "turn on "
	elif "turn off" in instruction:
		operation = "turn off "
	elif "toggle" in instruction:
		operation = "toggle "
		
	coordinates = get_coordinates(instruction.replace(operation, ""))
	
	start = coordinates[0]
	end = coordinates[1]

	for x in range(start[0], end[0] + 1):
		for y in range(start[1], end[1] + 1):
			if operation == "turn on ":
				grid[x][y] += 1
			elif operation == "turn off ":
				grid[x][y] -= 1 if grid[x][y] > 0 else 0
			elif operation == "toggle ":
				grid[x][y] += 2

for instruction in instructions:
	perform_operation_part_2(instruction)

sum_of_brightness = 0

for row in grid:
	sum_of_brightness += sum(row)

print  sum_of_brightness