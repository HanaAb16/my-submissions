# Problem: Odd Subarrays - https://codeforces.com/problemset/problem/1686/B

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
    p = arr()
    cur_max = p[0]
    ans = 0
    for i in range(n):
        if p[i] < cur_max:
            ans += 1
            cur_max = 0
        else:
            cur_max = p[i]
    print(ans)
    pass










def main():
    t = inp()

    while t:
        solution()
        t -= 1

main()

