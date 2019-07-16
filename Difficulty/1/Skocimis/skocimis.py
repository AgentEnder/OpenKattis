# Skocimis, OpenKattis, https://open.kattis.com/contests/xsyd56/problems/skocimis
# Sln by CraigoryCoppola

positions = sorted([int(x) for x in input().split()])
spaces = [positions[1]-positions[0],positions[2]-positions[1]]
moves = 0
while spaces[0] > 1 or spaces[1] > 1:
    if spaces[0] > spaces[1]: #Move the right most one.
        positions.pop()
        positions.insert(1, positions[0]+1)
    else:
        positions.insert(2, positions[2]-1)
        positions.pop(0)
    moves+=1
    spaces = [positions[1]-positions[0],positions[2]-positions[1]]
print(moves)