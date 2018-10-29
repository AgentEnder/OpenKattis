#A Classy Problem, OpenKattis, https://open.kattis.com/problems/classy
#Sln by Craigory
import sys

class_to_int = {"lower":"0","middle":"1","upper":"2"}

for test_case in range(int(sys.stdin.readline())):
	num_people = int(sys.stdin.readline())
	people = {}
	class_max = 0
	for person_idx in range(num_people):
		line = sys.stdin.readline().replace("\n","").replace(" class","")
		line = line.split(":")
		name = line[0]
		classes = [class_to_int[x.replace(" ","")] for x in line[1].split("-")[:]]
		if len(classes)>class_max:
			class_max = len(classes)
		people[name]=classes
	people_by_class = {}
	for person in people:
		p_class = people[person]
		while len(p_class) < class_max:
			p_class.insert(0,"1")
		sum = int("".join(reversed(p_class)))
		if sum not in people_by_class:
			people_by_class[sum] = []
		people_by_class[sum].append(person)
	for class_level in sorted(people_by_class.keys(), reverse=True):
		for person in sorted(people_by_class[class_level]):
			print(person)
	print("="*30)