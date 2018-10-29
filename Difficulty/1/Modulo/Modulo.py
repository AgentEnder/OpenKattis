#Modulo, OpenKattis, https://open.kattis.com/contests/qfs98p/problems/modulo
## Sln by Craigory Coppola
import sys
print(len(set([int(sys.stdin.readline())%42 for x in range(10)])))