import sys
import re

def hashTable(candidatePerfect):
	table = {}
	for word in candidatePerfect:
		if word in table:
			table[word] += 1
		else:
			table.update({word : 1})
	return table

def printTable(table):
	for key, value in table.items():
		print(key, value)

def wellFormedCandidate(candidate):
	candidate2 = []
	candidatePerfect = []
	candidate2 = [word.lower().rstrip('\'\",.:;!?') for word in candidate]
	for word in candidate2:
		word2 = re.sub("\d+", "", word)
		if len(word2) == 0:
			pass
		else:
			candidatePerfect.append(word2)
	return candidatePerfect

def originalCandidate():
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

main()