"""
Author: Zachary Richardson
Assignment: frequency.py
Date: 3/22/13
"""

import sys

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
	for x in candidatePerfect:
		print(x)

if __name__ == '__main__':
	main()