import sys
import re

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
	for x in candidatePerfect:
		print(x)

main()