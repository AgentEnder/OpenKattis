import sys

def tines():
    L, R = [int(x) for x in sys.stdin.readline().split()]
    if (0<=L<=20 and 0<=R<=20):
        if (L!=0 and R !=0):
            if (L == R):
                print("Even", L+R)
            elif (R<L):
                print("Odd",L*2)
            else:
                print("Odd",R*2)
        elif (L==0 and R!=0):
            print("Odd",R*2)
        elif (L!=0 and R==0):
            print("Odd",L*2)
        else:
            print("Not a Moose")
    else:
        print("Not a Moose")
tines()
