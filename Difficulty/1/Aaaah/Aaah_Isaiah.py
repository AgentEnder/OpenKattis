import sys;

def aah():
    Marcus_ah = str(sys.stdin.readline())
    Doctor_ah = str(sys.stdin.readline())
    if (len(Marcus_ah) >= len(Doctor_ah)):
        print("Go")
    else:
        print("No")

aah()
