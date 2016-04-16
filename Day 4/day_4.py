# I'm using brute-force technique to arrive at the result,
# but there may be a more optimal solution available

from hashlib import md5

puzzle_input = 'ckczppom'

# Solution to Day 4 Part 1
success = False
count = 0

while not success:
	output = md5('{0}{1}'.format(puzzle_input, count)).hexdigest()
	if output.startswith(5 * '0'):
		break
	else:
		count += 1

print count

# Solution to Day 4 Part 2
success = False
count = 0

while not success:
	output = md5('{0}{1}'.format(puzzle_input, count)).hexdigest()
	if output.startswith(6 * '0'):
		break
	else:
		count += 1

print count