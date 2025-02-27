# Problem: C - Binary Flip - https://codeforces.com/gym/590053/problem/C

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
    a = input()
    b = input()
    cnt = Counter(a)
    i = n - 1
    swap = 0
    while i >= 0:
        if swap % 2 == 0:
            if a[i] != b[i]:
                if cnt['0'] == cnt['1']:
                    swap += 1
                else:
                    print('NO')
                    return
        else:
            if a[i] == b[i]:
                if cnt['0'] == cnt['1']:
                    swap += 1
                else:
                    print('NO')
                    return
        cnt[a[i]] -= 1
        i -= 1
    print('YES')

    pass










def main():
    t = inp()

    while t:
        solution()
        t -= 1

main()

