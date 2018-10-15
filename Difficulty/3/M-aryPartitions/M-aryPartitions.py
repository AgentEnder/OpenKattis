#M-ary Partitions, OpenKattis, https://open.kattis.com/problems/marypartitions
#Partial Sln by Craigory Coppola (Partial due to time limit issues.)
import math
import sys

def solve(num, m):
	partitions = [0]
	
	highest_power = int(math.log(num, m))
	powers = [m**i for i in range(highest_power+1)]
	powers.reverse()
	
	####Find constant multipliers for each power where sum(mult*power) is num
	####For ex, powers when num is 9 and m is 3 = [1,3,9]
	####So we need to find {x,y,z|x*1+y*3+z*9 = 9}
	####Each element of this set is a 3-ary partition of 9, and the magnitude is our return value.
	"""
		start is the power idx the for loop should generate guesses for
		powers is our list of powers
		curr_guess tracks current multipliers for each power
		current sum tracks the current sum
	"""
	def helper(start, powers=powers, curr_guess = [], curr_sum = 0):
		if start == len(powers):
			partition_string = ""
			if curr_sum == num:
				for idx, mult in enumerate(curr_guess):
					partition_string += str(mult) + "*" + str( powers[idx]) + "+"
				print("PARTITION FOUND: " + partition_string[:-1])
				partitions[0]+=1
			return
		if powers[start] == 1:
			temp_guess = []+ curr_guess
			temp_guess.append(num-curr_sum)
			helper(start+1, powers, temp_guess, curr_sum = curr_sum+num-curr_sum)
		else:
			for i in range(0, 1+(num-curr_sum)//(powers[start])):
				temp_guess = []+ curr_guess
				temp_guess.append(i)
				if curr_sum+i*powers[start] > num:
					break
				helper(start+1, powers, temp_guess, curr_sum = curr_sum+i*powers[start])
	helper(0, powers, [], 0)
	
	return partitions

test_cases = int(sys.stdin.readline())
for test_case in range(1,test_cases+1):
	line = sys.stdin.readline().split(" ")
	m = int(line[1])
	num = int(line[2])
	print(test_case, solve(num, m)[0])