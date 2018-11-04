#Goat Rope, OpenKattis, https://open.kattis.com/problems/goatrope
#Sln by MSU ICPC TEAM FA 2018
import math
in_stream = [int(x) for x in input().split()]
goat = in_stream[:2]
bottom_left = in_stream[2:4]
top_right = in_stream[4:]

x = 0
y = 0
if goat[0] < bottom_left[0]:
    x = bottom_left[0]
elif goat[0] < top_right[0]:
    x = goat[0]
else:
    x = top_right[0]
if goat[1] < bottom_left[1]:
    y = bottom_left[1]
elif goat[1] < top_right[1]:
    y = goat[1]
else:
    y = top_right[1]

print(math.sqrt((x-goat[0])**2+(y-goat[1])**2))