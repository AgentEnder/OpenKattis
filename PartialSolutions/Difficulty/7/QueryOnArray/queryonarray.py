#Another Query on Arrays, OpenKattis, https://open.kattis.com/problems/queryonarray

import sys

memoise = {} #i:(i+1)*(i+2)*(i*3)
max_i = -1

def oper_zero(arr,x,y):
	return sum(arr[x:y])%(10**9+7)

def oper_one(arr,x,y):
	global max_i
	i = 0
	while(x+i < y):
		if i > max_i:
			memoise[i] = (i+1)*(i+2)*(i+3)
			max_i = i
		arr[x+i]+=memoise[i]
		i+=1

def oper_two(arr,x,y):
	global max_i
	i = 0
	while(x+i < y):
		if i > max_i:
			memoise[i] = (i+1)*(i+2)*(i+3)
			max_i = i
		arr[x+i]-=memoise[i]
		i+=1
		
lengths = [eval(x) for x in sys.stdin.readline().split()]
array = [0 for i in range(lengths[0])]

for query_idx in range(lengths[1]):
	query = [int(x) for x in sys.stdin.readline().split()]
	if query[0] == 0:
		print(oper_zero(array, query[1]-1,query[2]))
	elif query[0] == 1:
		oper_one(array, query[1]-1, query[2])
	else:
		oper_two(array, query[1]-1, query[2])
	
