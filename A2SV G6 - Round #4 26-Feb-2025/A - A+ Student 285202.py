# Problem: A - A+ Student - https://codeforces.com/gym/590053/problem/A

from collections import Counter , defaultdict
from cmath import inf
def inp(): return(int(input()))

def arr():return(list(map(int,input().split())))

def st():
    s = input()
    return(list(s[:-1]))

def num(): return(map(int,input().split()))





def solution():
    a , b , c = arr()
    ans = []
    m = max(a ,b, c)
    if a == m and a > b and a > c:
        ans.append(0)
    else:
        ans.append(m + 1 - a)
    if b == m and b > a and b > c:
        ans.append(0)
    else:
        ans.append(m + 1 - b)
    if c == m and c > b and c > a:
        ans.append(0)
    else:
        ans.append(m + 1 - c)
    print(*ans)
    pass










def main():
    t = inp()

    while t:
        solution()
        t -= 1

main()

