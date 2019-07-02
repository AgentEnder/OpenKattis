#Variable Arithmetic, OpenKattis, https://open.kattis.com/problems/variablearithmetic
#Sln by Craigory Coppola

import sys

variables = {}

for line in sys.stdin:
    if line.strip() == "0": #Exit condition
        break
    if '=' in line: #Variable definition
        arr = line.split("=")
        variables[arr[0].strip()] = int(arr[1])
    elif '=' not in line: #Sum
        tokens = [x.strip() for x in line.split("+")]
        sum = 0
        addend = ""
        for token in tokens:
            if token.isdigit():
                sum+=int(token)
                continue
            if token in variables.keys():
                sum+=variables[token]
            else:
                if addend != "":
                    addend += " + "
                addend+=token
        if sum is not 0:
            print(sum, end="")
        if addend != "":
            if sum is 0:
                print(addend)
            else: print(" + " + addend)
        else: print()