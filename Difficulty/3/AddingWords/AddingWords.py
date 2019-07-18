#Adding Words, OpenKattis, Sln by Craigory Coppola
#https://open.kattis.com/problems/addingwords

import sys

w2i = {}
i2w = {}
for line in sys.stdin:
    _in = line.split()
    _inBU = [x for x in _in]
    if _in[0] == "def":
        if _in[1] in w2i.keys():
            val = w2i[_in[1]]
            del i2w[val]
        w2i[_in[1]] = int(_in[2])
        i2w[int(_in[2])] = _in[1]
    elif _in[0] == "clear":
        w2i.clear()
        i2w.clear()
    else:
        tokens = _in[1:-1]
        for i in range(len(tokens)):
            if tokens[i] in w2i.keys():
                tokens[i] = str(w2i[tokens[i]])
            else:
                if tokens[i] is "+" or tokens[i] is "-":
                    continue
                break
        else:
            sum = eval("".join(tokens))
            if sum not in i2w.keys():
                print(" ".join(_inBU[1:]) + " unknown")
            else:
                print(" ".join(_inBU[1:]) + " " + i2w[sum])
            continue
        print(" ".join(_inBU[1:]) + " unknown")
                        
