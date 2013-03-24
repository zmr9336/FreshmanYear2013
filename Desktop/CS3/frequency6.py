"""
Author: Zachary Richardson
Assignment: frequency.py
Date: 3/24/13
"""

import fileinput
import sys
from collections import OrderedDict

def originalCandidate():
	"""
	checks if there are one or 2 command line arguments.
	if there is one, it appeds to the list, igonore, normally.
	if there are 2 arguments, if loops through both files and
	only appends the words that are not repeated in the first file
	the list is then returned.
	"""
	ignore = []
	if len(sys.argv[1:]) > 1:
		for line in fileinput.input(sys.argv[1:][0]):
			ignore.append(line)
		candidate = []
		for line in fileinput.input(sys.argv[1:][1]):
			line = line.split()
			if len(line) == '':
				pass
			else:
				for word in line:
					for ig in ignore:
						if word == ig:
							pass
						else:
							candidate.append(word)
		return candidate
	else:
		candidate = []
		for line in fileinput.input(sys.argv[1:]):
			line = line.split()
			if len(line) == '':
				pass
			else:
				for word in line:
					candidate.append(word)
		return candidate

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

def sortTable(table):
	"""
	sorts the table, which is a dictionary based on alphabetical order
	and by the greatest value. It then returns the dictionary.
	"""
	new = OrderedDict(sorted(table.items()))
	new2 = sorted(new.items(), key = lambda kv:kv[1], reverse = True)
	sortedTable = new2
	return sortedTable

def graphicHistogram(sortedTable):
	"""
	prints out the table in a histogram form, (word ***),
	as long as the table has at least one element.
	"""
	if len(sortedTable) < 1:
		pass
	else:
		M = sortedTable[0][1]
		i = 0
		j = 0
		longestWord = 0

		while i < len(sortedTable):
			word = sortedTable[i][0]
			if len(word) > longestWord:
				longestWord = len(word)
			i += 1

		while j < len(sortedTable):
			N = sortedTable[j][1]
			hist = (50 * N) // M
			if len(sortedTable[j][0]) == longestWord:
				print(sortedTable[j][0] +" " + '*' * hist)
			else:
				length = (longestWord - len(sortedTable[j][0])) + 1
				print(sortedTable[j][0] + ' ' * length + '*' * hist)
			j += 1

def main():
	candidate = originalCandidate()
	candidatePerfect = wellFormedCandidate(candidate)
	hist = hashTable(candidatePerfect)
	sortedTable = sortTable(hist)
	graphicHistogram(sortedTable)

if __name__ == '__main__':
	main()