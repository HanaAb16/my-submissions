# Problem: E - Strange Mirroring - https://codeforces.com/gym/596141/problem/E

from collections import Counter , defaultdict
from cmath import inf
def inp(): return(int(input()))

def arr():return(list(map(int,input().split())))

def st():
    s = input()
    return(list(s[:-1]))

def num(): return(map(int,input().split()))



def find_char(level, k, i, s):
    if level == 1:  
        return s[i]

    half_length = 2 ** (level - 2)

    if k > half_length:
        return find_char(level - 1, k - half_length, i, s).swapcase()

    return find_char(level - 1, k, i, s)
def solution():
    s = input()
    q = inp()
    queries = arr()
    n = len(s)  
    results = []
    for k in queries:
        k -= 1  
        level = k // len(s) + 1  
        index = k % len(s)  
        results.append(find_char(61, level, index, s))  

    print(*results)  









def main():
    t = inp()

    while t:
        solution()
        t -= 1

main()

