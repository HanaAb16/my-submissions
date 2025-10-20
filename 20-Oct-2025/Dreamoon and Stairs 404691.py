# Problem: Dreamoon and Stairs - https://codeforces.com/problemset/problem/476/A

from collections import Counter , defaultdict
from cmath import inf 
import math
def inp(): return(int(input()))

def arr():return(list(map(int,input().split())))

def st():
    s = input()
    return(list(s[:-1]))

def num(): return(map(int,input().split()))





def solution():
    n , m = arr()
    if n < m:
        print(-1)
    else:
        temp = math.ceil(n / 2)
        if temp % m == 0:
            print(temp)
        else:
            print(math.ceil(temp / m) * m)











def main():
    t = 1

    while t:
        solution()
        t -= 1

main()

