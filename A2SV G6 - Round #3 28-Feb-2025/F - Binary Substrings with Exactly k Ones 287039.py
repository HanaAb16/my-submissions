# Problem: F - Binary Substrings with Exactly k Ones - https://codeforces.com/gym/588468/problem/F

from collections import Counter , defaultdict
from cmath import inf
def arr(): return list(map(int , (x for x in input().split())))
k = int(input())
s = list(map(int , input().strip()))
def atmost (k , s):
    l = 0
    window = 0
    count = 0
    for r in range(len(s)):
        window += s[r]
        while window > k:
            window -= s[l]
            l += 1
        count += r - l + 1
    return count
if k == 0:
    print(atmost(k , s))
else:
    print(atmost(k , s) - atmost(k - 1 , s))
