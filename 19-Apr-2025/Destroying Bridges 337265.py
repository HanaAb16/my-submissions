# Problem: Destroying Bridges - https://codeforces.com/problemset/problem/1944/A

from collections import Counter , defaultdict
from cmath import inf
def inp(): return(int(input()))

def arr():return(list(map(int,input().split())))

def st():
    s = input()
    return(list(s[:-1]))

def num(): return(map(int,input().split()))





def solution():
    n , k = arr()
    if k >= n - 1:
        print(1)
    else:
        print(n)










def main():
    t = inp()

    while t:
        solution()
        t -= 1

main()

