"""
Author: Zachary Richardson
Assignment: frequency.py
Date: 3/22/13
"""

import sys

def frequency(line):
	"""
	splits the lines as long as the len isn't 0.
	it appends the words to a list, candidate, and
	then prints the list
	"""
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
