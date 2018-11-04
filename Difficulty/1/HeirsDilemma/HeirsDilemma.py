#Heirs Dilemma, OpenKattis, https://open.kattis.com/problems/heirsdilemma
#Sln by MSU FA 2018 ICPC TEAM
count = 0
def solve(min, max):
    def solve_helper(min, max, curr = [], digits = set([1,2,3,4,5,6,7,8,9])):
        global count
        if len(curr) == 6:
            num = int("".join([str(i) for i in curr]))
            if num > max or num < min:
                return
            for digit in curr:
                if num%digit!=0:
                    break
            else:
                count+=1
            return
        for digit in digits:
            if digit in curr:
                continue
            else:
                solve_helper(min,max,curr+[digit],set([i for i in digits if i!=digit]))
    solve_helper(min, max, [], set([1,2,3,4,5,6,7,8,9]))
    return count

in_stream = [int(x) for x in input().split()]
solve(min(in_stream), max(in_stream))
print(count)