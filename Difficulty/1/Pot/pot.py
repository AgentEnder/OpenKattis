line = input()
sum = 0
for i in range(int(line)):
	s = input()
	sum+=int(int(s[:-1])**int(s[-1]))
print(sum)