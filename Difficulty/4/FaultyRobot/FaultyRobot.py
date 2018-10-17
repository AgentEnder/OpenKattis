#FaultyRobot, OpenKattis, https://open.kattis.com/problems/faultyrobot
## Sln by Craigory Coppola (Partial due to wrong answer on test case 4)

import sys

line = sys.stdin.readline().replace("\n","").split() #Get initial input 
forced_graph = {i:[] for i in range(1, int(line[0])+1)} #initialize adjacency matrix for forced edges
buggy_graph = {i:[] for i in range(1, int(line[0])+1)} #initialize adjacency matrix for buggy edges
bug_jumps_allowed = 1 #Number of times robot might make a buggy move

#Parse Adj. Matrices
for edge in range(int(line[1])):
	edge_pair = [int(x) for x in sys.stdin.readline().split()] #Formated like: [edge, connection]
	if edge_pair[0] > 0: #Edge should be buggy
		buggy_graph[edge_pair[0]].append(edge_pair[1]) #Add to buggy matrix
	else:
		forced_graph[-1*edge_pair[0]].append(edge_pair[1]) #Add to forced matrix

stops = set() #Only record unique values

#Recursive Depth First Traversal, modified for problem specifics.
def traversal(start, seen = [], bug_count = 0, prev_buggy = False):
	
	#Loop Detection
	if start in seen: #Loop Found
		return #Dont loop
	elif not prev_buggy:
		seen.append(start) #Add to seen_nodes
	
	if bug_count < bug_jumps_allowed:	#Can still make a buggy move
		for node in buggy_graph[start]: #Check each buggy move
			traversal(node, seen, bug_count+1, True) #Increment bug count
	
	if len(forced_graph[start]) > 0: #There is a forced move, can't stop
		for node in forced_graph[start]: #Check each forced move (should only ever be one)
			traversal(node, seen) #Recursive call for forced move
	else: #No forced edges, must stop
		stops.add(start) #Add to set if not in set
		
	

traversal(1) #Start Traversal Algorithm
#print("num_stops = {0}, stops = {1}".format(len(stops), stops)) #DEBUGGING PRINT
print(len(stops)) #ACTUAL PRINT