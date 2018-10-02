#Get to Work, OpenKattis https://open.kattis.com/problems/gettowork
import sys

for test_case in range(int(sys.stdin.readline())): #test case
	first_line = sys.stdin.readline()
	first_line = first_line.split(" ")
	N = int(first_line[0]) #N = num towns
	T = int(first_line[1]) #T = office town
	E = int(sys.stdin.readline()) # num employees
	towns = {town_id+1:[] for town_id in range(N)}
	results = [0 for x in range(N)]
	for employee_id in range(E):
		employee = sys.stdin.readline()
		employee = employee.split(" ")
		towns[int(employee[0])].append(int(employee[1]))
	for town_id,town in towns.items(): #each town is list of cars
		if town_id == T: continue
		town.sort(reverse=True)
		space_needed = len(town)
		space_had = 0
		for passenger in town:
			if passenger > 0:
				space_had+=passenger
		if space_had < space_needed:
			print("Case #{}: IMPOSSIBLE".format(test_case+1))
			results[town_id-1] = -1
			break
		else:
			cars = 0
			for car in town:
				space_needed -= car
				cars+=1
				if space_needed <= 0:
					break
			results[town_id-1] = cars
	if min(results) >= 0:
		results = [str(x) for x in results]
		print("Case #{case_number}: {res}".format(case_number = test_case+1, res=" ".join(results)))
			
		