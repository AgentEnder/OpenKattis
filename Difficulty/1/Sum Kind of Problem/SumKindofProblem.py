#Sum Kind of Problem, OpenKattis, https://open.kattis.com/problems/sumkindofproblem
#Sln by Craigory Coppola
import sys

test_cases = int(sys.stdin.readline())
for test_case in range(test_cases):
	line = sys.stdin.readline().split(" ")
	case_id = int(line[0])
	n = int(line[1])
	pos_sum = int(n*(n+1)/2)
	even_sum = int(pos_sum*2)
	odd_sum = int(even_sum-n)
	
	print("{} {} {} {}".format(case_id, pos_sum, odd_sum, even_sum))