import sys

def frequency(line):
	candidate = []
	if len(line) == '':
		pass
	else:
		for word in line:
			candidate.append(word)
	for x in candidate:
		print(x)

def main():
	for line in sys.stdin:
		line = line.split()
		frequency(line)

if __name__ == '__main__':
	main()
