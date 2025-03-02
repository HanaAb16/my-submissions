# Problem: D - Bernabas and the Harmonious Melody - https://codeforces.com/gym/588468/problem/D

from collections import Counter , defaultdict
from cmath import inf
def arr(): return list(map(int , (x for x in input().split())))
def solve():
    t = int(input())
    for _ in range(t):
        n = int(input())
        s = input()
        s_set = set(s)
        min_rem = inf
        for ch in s_set:
            l , r = 0 , n - 1
            removed = 0
            while l < r:
                if s[l] == s[r]:
                    l += 1
                    r -= 1
                else:
                    if s[l] == ch:
                        l += 1
                        removed += 1
                    elif s[r] == ch:
                        r -= 1
                        removed += 1
                    else:
                        break
            else:
                min_rem = min(min_rem , removed)

        print(-1 if min_rem == inf else min_rem)
solve()


