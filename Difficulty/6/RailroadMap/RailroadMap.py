#Railroad Map, OpenKattis, https://open.kattis.com/contests/oeguqx/problems/railroad
#Sln by Craigory Coppola
tests = int(input())
for test_idx in range(tests):
	input() #Throwout blank line
	edges = int(input().split()[1]) #edges in map
	old_map = {}
	for edge in range(edges):
		edge_components = [int(x) for x in input().split()]
		if edge_components[0] not in old_map:
			old_map[edge_components[0]] = []
		if edge_components[1] not in old_map:
			old_map[edge_components[1]] = []
		old_map[edge_components[0]].append([edge_components[1],edge_components[2]])
		old_map[edge_components[1]].append([edge_components[0],edge_components[2]])
	for station in old_map.keys():
		if len(old_map[station]) == 2:
			first_stop = old_map[station][0][0]
			second_stop = old_map[station][1][0]
			time = old_map[station][0][1]+old_map[station][1][1]
			old_map[first_stop].append([second_stop, time])
			for edge in old_map[first_stop]:
				if edge[0] == station:
					old_map[first_stop].remove(edge)
					break
			old_map[second_stop].append([first_stop, time])
			for edge in old_map[second_stop]:
				if edge[0] == station:
					old_map[second_stop].remove(edge)
					break
			old_map[station] = []
	edges = []
	
	for station, railroad_list in {x:old_map[x] for x in old_map.keys() if len(old_map[x]) > 0}.items():
		for rail in railroad_list:
			if [rail[0], station, rail[1]] not in edges:
				edges.append([station,rail[0], rail[1]])
	print(len(edges))
	for edge in edges:
		print(edge[0],edge[1],edge[2])
	if test_idx < tests-1:
		print()
	