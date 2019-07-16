#ABC, OpenKattis, https://open.kattis.com/problems/abc
#Sln by Craigory Coppola

nums = sorted([int(x) for x in input().split()])
idxs = [ord(c)-65 for c in input()]
print(" ".join([str(nums[x]) for x in idxs]))