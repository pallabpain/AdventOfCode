words = [word.rstrip('\n') for word in open("input.txt").readlines()]

# Solution for Day 5 Part 1
def has_three_vowels(word):
	vowels = 0
	for letter in word:
		if letter in ('a', 'e', 'i', 'o', 'u'):
			vowels += 1
		if vowels == 3:
			return True
	return False


def a_letter_appears_twice_in_a_row(word):
	prev = ""
	for letter in word:
		if prev == letter:
			return True
		else:
			prev = letter
	return False

def does_not_contain_restricted_srtings(word):
	for string in ('ab', 'cd', 'pq', 'xy'):
		if string in word:
			return False
	return True

def is_word_nice_part_1(word):
	check_1 = has_three_vowels(word)
	check_2 = a_letter_appears_twice_in_a_row(word)
	check_3 = does_not_contain_restricted_srtings(word)
	return check_1 and check_2 and check_3

nice_words = filter(is_word_nice_part_1, words)

print len(nice_words)


# Solution for Day 5 Part 2
def a_letter_repeats_with_exactly_one_letter_in_between(word):
	for letter in word:
		count = word.count(letter)
		if count >= 2:
			first = word.index(letter)
			for x in range(0, count - 1):
				second = word.index(letter, first + 1)
				if (second - first) == 2:
					return True
				else:
					first = second
	return False

def pair_of_two_letters_repeating_without_overlapping(word):
	prev = ""
	for letter in word:
		if prev == "":
			prev = letter
		else:
			if word.count("{0}{1}".format(prev, letter)) >= 2:
				return True
		prev = letter
	return False

def is_word_nice_part_2(word):
	check_1 = pair_of_two_letters_repeating_without_overlapping(word)
	check_2 = a_letter_repeats_with_exactly_one_letter_in_between(word)
	return check_1 and check_2

nice_words_2 = filter(is_word_nice_part_2, new_words)

print nice_words_2

# wretched1 has a beter solution using regex 
# https://github.com/wretched1/adventofcode/blob/master/nice_strings.py
# https://github.com/wretched1/adventofcode/blob/master/nice_strings_p2.py