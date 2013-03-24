"""
Author: Zachary Richardson
Assignment: frequency.py
Date: 3/23/13
"""

import sys

def hashTable(candidatePerfect):
	"""
	creates a dictionary with each word from candidatePerfect
	as a key and its frequency as a value. Then, the dictionary
	is returned.
	"""
	table = {}
	for word in candidatePerfect:
		if word in table:
			table[word] += 1
		else:
			table.update({word : 1})
	return table

def printTable(table):
	"""
	loops throuhg every key and value and prints the key and then
	a spaces and then the value.
	"""
	for key, value in table.items():
		print(key, value)

def wellFormedCandidate(candidate):
	"""
	strips the lines of any trailing punctuation or numbers.
	appends the words to a new list, candidatePerfect.
	then candidatePerfect is returned.
	"""
	candidate2 = []
	candidatePerfect = []
	candidate2 = [word.lower().rstrip('\'\",.:;!?') for word in candidate]
	for word in candidate2:
		if len(word) == 0:
			pass
		elif word.isalpha():
			candidatePerfect.append(word)
	return candidatePerfect

def originalCandidate():
	"""
	splits the lines as long as the len isn't 0.
	it appends the words to a list, candidate, and
	then returns the list
	"""
	candidate = []
	for line in sys.stdin:
		line = line.split()
		if len(line) == '':
			pass
		else:
			for word in line:
				candidate.append(word)
	return candidate

def main():
	candidate = originalCandidate()
	candidatePerfect = wellFormedCandidate(candidate)
	hist = hashTable(candidatePerfect)
	printTable(hist)

if __name__ == '__main__':
	main()