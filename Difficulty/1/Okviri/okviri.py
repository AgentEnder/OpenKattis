#Okviri, OpenKattis, https://open.kattis.com/problems/okviri
#Sln by Craigory Coppola

_in = input()
w = len(_in)*4+1
out = [['.' for i in range(w)] for i in range(5)]
    
#Draw peter pan windows
for i,c in enumerate(_in):
    out[2][i*4+2] = c
    out[2][i*4] = '#'
    out[2][i*4+4] = '#'
    out[0][i*4+2] = '#'
    out[4][i*4+2] = '#'
    out[1][i*4+1] = '#'
    out[1][i*4+3] = '#'
    out[3][i*4+1] = '#'
    out[3][i*4+3] = '#'
    
#Draw wendy windows
for i,c in enumerate(_in):
    if not (i+1)%3 == 0:
        continue
    out[2][i*4] = '*'
    out[2][i*4+4] = '*'
    out[0][i*4+2] = '*'
    out[4][i*4+2] = '*'
    out[1][i*4+1] = '*'
    out[1][i*4+3] = '*'
    out[3][i*4+1] = '*'
    out[3][i*4+3] = '*'

print("\n".join(["".join(x) for x in out]))