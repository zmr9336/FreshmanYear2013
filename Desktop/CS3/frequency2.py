import sys

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

if __name__ == '__main__':
	main()