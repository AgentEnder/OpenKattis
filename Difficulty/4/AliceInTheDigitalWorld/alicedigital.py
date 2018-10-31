#Alice in the Digital World, OpenKattis, https://open.kattis.com/problems/alicedigital
#Sln by Craigory Coppola
import sys

def find_all_idx(list, item):
	indicies = []
	for idx, t in enumerate(list):
		if t == item:
			indicies.append(idx)
	return indicies

def get_maximal_subsection(list, m, idx):
	left_idx = idx
	right_idx = idx
	while (left_idx > 0):
		if list[left_idx-1] > m:
			left_idx-=1
		else:
			break
	while (right_idx < len(list)-1):
		if list[right_idx+1] > m:
			right_idx+=1
		else:
			break
	return list[left_idx:right_idx+1]
			
		
	
for test_case in range(int(sys.stdin.readline())):
	m = int(sys.stdin.readline().split()[1])
	ints = [int(x) for x in sys.stdin.readline().split()]
	subsections = []
	recording = True
	max_sum = 0
	for m_idx in find_all_idx(ints, m):
		max_sum = max(max_sum, sum(get_maximal_subsection(ints, m, m_idx)))
	print(max_sum)
			
		
