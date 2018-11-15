#Compound Words, OpenKattis, https://open.kattis.com/problems/compoundwords
#Sln by Craigory Coppola
import sys
words = []
for line in sys.stdin:
	words += line.split()
words.sort()
compounds = set()
for prefix_idx in range(len(words)):
	for postfix_idx in range(len(words)):
		if prefix_idx == postfix_idx:
			continue
		else:
			compounds.add(words[prefix_idx]+words[postfix_idx])
for word in sorted(compounds):
	print(word)