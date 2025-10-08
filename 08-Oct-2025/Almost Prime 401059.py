# Problem: Almost Prime - https://codeforces.com/problemset/problem/26/A

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
    bucket = [0] * (n + 1)
    for i in range(2 , n + 1):
        if not bucket[i]:
            j = 2 * i
            while j <= n:
                bucket[j] += 1
                j += i
        i += 1
    ans = 0
    for cnt in bucket:
        if cnt == 2:
            ans += 1
    print(ans)










def main():
    t = 1

    while t:
        solution()
        t -= 1

main()

