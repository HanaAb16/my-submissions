# Problem: D - Minimize the Distance - https://codeforces.com/gym/590053/problem/D

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
    nums.sort()
    print(nums[(n - 1) // 2]) 
    pass










def main():
    t = 1

    while t:
        solution()
        t -= 1

main()

