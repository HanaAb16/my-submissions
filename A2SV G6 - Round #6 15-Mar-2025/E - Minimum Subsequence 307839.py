# Problem: E - Minimum Subsequence - https://codeforces.com/gym/594077/problem/E

from collections import Counter , defaultdict
from cmath import inf
def inp(): return(int(input()))

def arr():return(list(map(int,input().split())))

def st():
    s = input()
    return(list(s[:-1]))

def num(): return(map(int,input().split()))





def solution():
    n = inp()
    s = input()
    zeros = []
    ones = []
    ans = []
    gp = 0
    for i in range(n):
        if s[i] == '0':
            if ones:
                ans.append(ans[ones.pop()])
            else:
                gp += 1
                ans.append(gp)
            zeros.append(i)
        else:
            if zeros:
                    ans.append(ans[zeros.pop()])
            else:
                gp += 1
                ans.append(gp)
            ones.append(i)
    print(gp)
    print(*ans)
            












def main():
    t = inp()

    while t:
        solution()
        t -= 1

main()

