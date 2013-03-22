import sys
import re
from collections import OrderedDict

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
	for x, y in sorted(new.items(), key = lambda kv:kv[1], reverse = True):
		print("%s %s" % (x,y))			

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
	sortTable(hist)

main()