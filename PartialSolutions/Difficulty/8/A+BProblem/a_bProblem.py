#A+B Problem, OpenKattis, https://open.katt	is.com/problems/aplusb
#Partial Sln, TOO SLOW, by Craigory Coppola
import sys
ways = set()

num_ints = int(sys.stdin.readline())
ints = [int(x) for x in sys.stdin.readline().split()] #Get ints from stdin
ints.sort() #Sort ints for partitions
count = 0 #Count of ways
''' #SOLUTION 2
int_dict = {}
for num in sorted(ints):
	if num not in int_dict:
		int_dict[num] = 1
	else:
		int_dict[num]+=1

for sum_idx, sum in enumerate(int_dict.keys()):
	for a_idx, a in enumerate(int_dict.keys()):
		if a == sum and int_dict[a] == 1:
			continue
		b = sum - a
		if b in int_dict.keys():
			if b is not a:
				count+=int_dict[b]*int_dict[a]*int_dict[sum]
			elif int_dict[a] > 1:
				count+=(int_dict[b]-1)*int_dict[a]*int_dict[sum]
	
'''
memoise = {} #dict for recurring ints in array, instead of looking up each way

for idx_i in range(len(ints)-1): #Loop through combinations of 2 addends from list, in lexographic order. 
	i = ints[idx_i]
	for idx_k in range(idx_i+1,len(ints)):
		k = ints[idx_k]
		if i+k > ints[-1]: #i+k greater than max value in list, no need to continue checking i+a_k
			break
		if k >= 0:
			if tuple([i,k]) not in memoise.keys():
				arr = enumerate(ints[idx_i:], idx_i)
				memoise[tuple([i,k])] = [s_i for s_i,s in arr if s == i+k]
			ways = [idx for idx in memoise[tuple([i,k])] if idx!=idx_i and idx!=idx_k]
			count+=2*len(ways)
		else:
			if i+k < ints[0]: #Adding negative is less than smallest value in ints, dont enum values
				continue
			if tuple([i,k]) not in memoise.keys():
				arr = enumerate(ints[:idx_i])
				memoise[tuple([i,k])] = [s_i for s_i,s in arr if s == i+k]
			ways = [idx for idx in memoise[tuple([i,k])] if idx!=idx_i and idx!=idx_k]
			count+=2*len(ways) #Mult by 2 due to looping through combin 2 rather than permutes'''
print(count)
