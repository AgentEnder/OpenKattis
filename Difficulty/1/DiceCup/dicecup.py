#Dice Cup, OpenKattis, https://open.kattis.com/problems/dicecup
#Sln by Craigory Coppola

x, y = [int(x) for x in input().split()]
die_x = [i +1 for i in range(x)]
die_y = [i +1 for i in range(y)]
sums = {}
combin = float(x*y)

for i in die_x:
	for j in die_y:
		if i+j not in sums.keys():
			sums[i+j] = 0
		sums[i+j]+=1
sums = [(sum, count/combin) for sum, count in sums.items()]
sums.sort(reverse = True, key = lambda i: i[1])
last = -1
for i in sums:
	if last != -1 and last != i[1]:
		break
	print(i[0])
	last = i[1]