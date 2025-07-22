# Problem: B - Mihret and Chess - https://codeforces.com/gym/604781/problem/B

from collections import Counter , defaultdict
from cmath import inf
def inp(): return(int(input()))

def arr():return(list(map(int,input().split())))

def st():
    s = input()
    return(list(s[:-1]))

def num(): return(map(int,input().split()))





def solution():
    r1 , c1 , r2 , c2 = arr()
    if r1 == r2 or c1 == c2:
        rook = 1
    else:
        rook = 2
    if abs(r1 - r2) == abs(c1 - c2):
        bishop = 1
    elif (r1 + c1) % 2 == (r2 + c2) % 2:
        bishop = 2
    else:
        bishop = 0
    king = max(abs(r1 - r2) , abs(c1 - c2))
    print(rook , bishop , king)










def main():
    t = 1

    while t:
        solution()
        t -= 1

main()

