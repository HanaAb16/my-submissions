# Problem: Array Elimination - https://codeforces.com/contest/1601/problem/A

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
    a = arr()
    bit_cnt = [0] * 30
    for num in a:
        for bit in range(30):
            if num & (1 << bit):
                bit_cnt[bit] += 1
    ans = []
    for i in range(1 , n + 1):
        for cnt in bit_cnt:
            if cnt % i != 0:
                break
        else:
            ans.append(i)
    print(*ans)










def main():
    t = inp()

    while t:
        solution()
        t -= 1

main()

