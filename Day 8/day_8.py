from re import escape

lines = [line.rstrip('\n') for line in open("input.txt").readlines()]

# Solution for Day 8 Part 1
string_literals = 0
in_memory = 0

for line in lines:
	string_literals += len(line)
	in_memory += len(eval(line))

print "Part 1 Answer =", string_literals - in_memory

# Solution for Day 8 Part 2
string_literals = 0
encoded_literals = 0

encode = lambda x: '"%s"' % escape(x)
for line in lines:
	string_literals += len(line)
	encoded_literals += len(encode(line))

print "Part 2 Answer =", encoded_literals - string_literals 