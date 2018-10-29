#Association for Computing Machinery, OpenKattis, https://open.kattis.com/problems/acm2
#Sln by Craigory Coppola.

import sys
firstIdx = int(sys.stdin.readline().split()[1])

upperTimeBound = 300

time = 0
penaltyTime = 0
solved = 0

times = [int(x) for x in sys.stdin.readline().split()] #Get list of integers on input line 2
if times[firstIdx] <= 300: #Can finish at least one problem
	time = times[firstIdx] #Do first problem
	penaltyTime = time #Add penal time
	del times[firstIdx] #Remove completed problem
	solved += 1 #increment solved
	times.sort() #Sort for optimal strategy
	while True:
		sys.stderr.write(str(times)+"\n")
		submitTime = time+times[0] #Time next problem would be solved in
		if submitTime <= upperTimeBound:
			time = submitTime #Increment time
			penaltyTime+=submitTime #Add penal time
			del times[0] #Remove completed problem
			solved+=1 #Increment Solved Count
			if len(times) < 1: #Solved all problems
				break
		else: #Can't solve more problems
			break

print(solved, penaltyTime)
		
