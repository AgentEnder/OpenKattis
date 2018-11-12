#Tristan Jordan for Calculator on kattis (4.5)
import sys
import string

for i in sys.stdin:
    x = i
    a = round(eval(x),2)
    s = str(a)
    if s.find(".") != -1:
        temp = s.split(".")
        if len(temp[1]) == 1:
            s+="0"
    else:
        s += ".00"
    print(s)
