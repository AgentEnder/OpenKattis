#Happy Happy Prime Prime, OpenKattis, https://open.kattis.com/problems/happyprime/
#Sln by Craigory Coppola
import sys

def check_prime(num):
	if num == 1:
		return False
	for i in range(2, int(num/2)):
		if num%i == 0:
			return False
	return True

def check_happy(num):
	checked_nums = []
	def helper(num):
		digits = []
		if num in checked_nums:
			return False
		else:
			checked_nums.append(num)
		num = str(num)
		for digit in range(len(num)):
			digits.append(int(num[digit]))
		total = sum([x**2 for x in digits])
		if total == 1:
			return True
		else:
			return helper(total)
	return helper(num)

test_cases = int(sys.stdin.readline().replace("\n", ""))

for test_case in range(1, test_cases+1):
	num_to_check = int(sys.stdin.readline().split(" ")[1])
	if check_prime(num_to_check):
		if check_happy(num_to_check):
			print(test_case, num_to_check, "YES")
			continue
	print(test_case, num_to_check, "NO")
	
