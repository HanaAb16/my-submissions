# Problem: B - Fix the Forecast! - https://codeforces.com/gym/591928/problem/B

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
    a = arr()
    b = arr()
    sra = []
    for i , val in enumerate(a):
        sra.append((val , i))
    sra.sort()
    srb = sorted(b)
    result = [0] * n
       
    for i in range(n):
        result[sra[i][1]] = srb[i]
    print(*result)
    
    pass










def main():
    t = inp()

    while t:
        solution()
        t -= 1

main()

