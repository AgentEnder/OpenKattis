#Poker Hand, OpenKattis, https://open.kattis.com/problems/pokerhand
#Sln by MSU ICPC TEAM FA 2018

lib = {}
in_stream = input().split()
for pair in in_stream:
    if pair[0] not in lib:
        lib[pair[0]] = 0
    lib[pair[0]]+=1
print(max(lib.values()))