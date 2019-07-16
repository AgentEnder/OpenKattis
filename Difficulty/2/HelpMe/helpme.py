#Help me With the Game, OpenKattis, https://open.kattis.com/contests/problems/helpme
#Sln by Craigory Coppola

import sys

white = []
black = []

int2chr = 'abcdefgh'
pieceOrder = {i:idx for idx, i in enumerate('KQRBNP')}

row = 9
for line in sys.stdin:
    if line == "+---+---+---+---+---+---+---+---+\n":
        row-=1
        continue
    col = 0
    for element in line.split("|")[1:-1]:
        if element == "":
            continue
        piece = element[1]
        if piece == '.' or piece == ':':
            col+=1
            continue
        if piece.upper() == piece: #White piece
            white.append(piece + str(int2chr[col]) + str(row))
        else:
            black.append(piece.upper() + str(int2chr[col]) + str(row))
        col+=1

white.sort(key=lambda x:(pieceOrder[x[0]], x[2],x[1]))
black.sort(key=lambda x:(pieceOrder[x[0]],-int(x[2]),x[1]))

for i,x in enumerate(white):
    if x[0] == 'P':
        white[i]=x[1:]
for i,x in enumerate(black):
    if x[0] == 'P':
        black[i]=x[1:]

print("White: " + ",".join(white))
print("Black: " + ",".join(black))