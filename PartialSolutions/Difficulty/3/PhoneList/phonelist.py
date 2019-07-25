#Phone List, OpenKattis, https://open.kattis.com/problems/phonelist
#Partial Sln by Craigory Coppola, TOO SLOW

cases = int(input())
for case in range(cases):
    num_nums = int(input())
    nums = [input().strip() for x in range(num_nums)]
    valid = True
    for num_i in range(0,num_nums-1):
        numi = nums[num_i]
        for num_j in range(num_i+1, num_nums):
            numj = nums[num_j]
            if len(numi) > len(numj):
                if numi[:len(numj)] == numj:
                    valid = False
                    break
            else:
                if numj[:len(numi)] == numi:
                    valid = False
                    break
        else:
            continue
        break 
    if valid:
        print("YES")
    else:
        print("NO")           