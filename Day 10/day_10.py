def get_sequence(sequence):
    prev_char, char_count, new_sequence = None, 0, ""
    for char in sequence:
        if prev_char != char and prev_char is not None:
            new_sequence += "{0}{1}".format(char_count, prev_char)
            char_count = 0
        char_count += 1
        prev_char = char
    new_sequence += "{0}{1}".format(char_count, prev_char)
    return new_sequence

sequence = "3113322113"

for i in range(40):
    sequence = get_sequence(sequence)

print "Part 1 Answer =", len(sequence)

sequence = "3113322113"

for i in range(50):
    sequence = get_sequence(sequence)

print "Part 2 Answer =", len(sequence)
