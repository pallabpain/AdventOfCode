# Creates a dictionary of the following format {result: operation}
instructions = {instruction[1].strip(): instruction[0].strip().split(' ') 
				for instruction in [line.strip('\n').split('->') 
					for line in open("input.txt").readlines()]}

signals = {}

def get_signal(wire):
	try:
		return int(wire)
	except Exception:
		pass

	if wire not in signals:
		operation = instructions[wire]
		if len(operation) == 1:
			signal = get_signal(operation[0])
		else:
			operator = operation[-2]
			if operator == "AND":
				signal = get_signal(operation[0]) & get_signal(operation[-1])
			elif operator == "OR":
				signal = get_signal(operation[0]) | get_signal(operation[-1])
			elif operator == "LSHIFT":
				signal = get_signal(operation[0]) << get_signal(operation[-1])
			elif operator == "RSHIFT":
				signal = get_signal(operation[0]) >> get_signal(operation[-1])
			elif operator == "NOT":
				signal = ~get_signal(operation[1])

		signals[wire] = signal

	return signals[wire]

a = get_signal('a')
print "Part 1 Answer", a
signals = {}
signals['b'] = a
a = get_signal('a')
print "Part 2 Answer", a
