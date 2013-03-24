import sys
from collections import OrderedDict	

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

def wellFormedCandidate(candidate):
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
	table = {}
	for word in candidatePerfect:
		if word in table:
			table[word] += 1
		else:
			table.update({word : 1})
	return table

def sortTable(table):
	new = OrderedDict(sorted(table.items()))
	new2 = sorted(new.items(), key = lambda kv:kv[1], reverse = True)
	sortedTable = new2
	return sortedTable

def graphicHistogram(sortedTable):
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