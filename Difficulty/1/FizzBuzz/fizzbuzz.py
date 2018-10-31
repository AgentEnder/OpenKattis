#FizzBuzz, OpenKattis, https://open.kattis.com/problems/fizzbuzz
#Sln by Craigory Coppola
X,Y,N = [int(x) for x in input().split()]
for i in range(1,N+1):
	if i%X == 0 or i%Y == 0:
		if i%X == 0:
			print("Fizz", end="")
		if i%Y == 0:
			print("Buzz", end="")
		print()
	else:
		print(i)