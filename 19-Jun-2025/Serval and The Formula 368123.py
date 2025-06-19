# Problem: Serval and The Formula - https://codeforces.com/problemset/problem/2085/C

from collections import Counter , defaultdict
from cmath import inf
def inp(): return(int(input()))

def arr():return(list(map(int,input().split())))

def st():
    s = input()
    return(list(s[:-1]))

def num(): return(map(int,input().split()))





def solution():
    x , y = arr()
    maxi = max(x , y)
    i = 1
    while i <= maxi:
        i *= 2
    k = i - maxi
    if (x + k) + (y + k) != (x + k) ^ (y + k):
        print(-1)
    else:
        print(k)
    
    
    









def main():
    t = inp()

    while t:
        solution()
        t -= 1

main()

