# Problem: Minimum Integer - https://codeforces.com/problemset/problem/1101/A

from collections import Counter , defaultdict
from cmath import inf
def inp(): return(int(input()))

def arr():return(list(map(int,input().split())))

def st():
    s = input()
    return(list(s[:-1]))

def num(): return(map(int,input().split()))





def solution():
    q = inp()
    for _ in range(q):
        l , r , d = arr()
        if l > d:
            print(d)
        else:
            print(((r // d) + 1) * d)









def main():
    t = 1

    while t:
        solution()
        t -= 1

main()

