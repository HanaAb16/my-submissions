# Problem: B - Distribute - https://codeforces.com/gym/606404/problem/B

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
    nums = arr()
    pair = {}
    for i  in range(n):
        pair[i] = nums[i]
    pair = dict(sorted(pair.items() , key= lambda num:num[1]))
    ind = list(pair.keys())
    l , r = 0 , n - 1
    while l < r:
        print(ind[l] + 1 , ind[r] + 1)
        l += 1
        r -= 1












def main():
    t = 1

    while t:
        solution()
        t -= 1

main()

