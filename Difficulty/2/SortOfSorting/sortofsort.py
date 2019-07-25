#Sort of Sorting, OpenKattis, https://open.kattis.com/problems/sortofsorting
#Sln by Craigory Coppola

line = input()
while line is not "0":
    num_names = int(line)
    names = [input() for x in range(num_names)]
    names.sort(key=lambda n: n[:2])
    [print(x) for x in names]
    print()
    line = input()
