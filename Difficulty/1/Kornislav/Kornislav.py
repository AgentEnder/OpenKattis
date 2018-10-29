#Kornislav, OpenKattis, https://open.kattis.com/problems/kornislav
#Sln by Craigory Coppola
import sys

nums = sorted([int(x) for x in sys.stdin.readline().split()])

print(nums[0]*nums[2])