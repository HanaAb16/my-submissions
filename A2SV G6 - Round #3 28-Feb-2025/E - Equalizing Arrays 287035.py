# Problem: E - Equalizing Arrays - https://codeforces.com/gym/588468/problem/E

from collections import Counter , defaultdict
from cmath import inf
def arr(): return list(map(int , (x for x in input().split())))
n = int(input())
a = arr()
m = int(input())
b = arr()
length = 0
i , j , asum , bsum  = 0 , 0 , 0 , 0
if sum(a) != sum(b):
    print(-1)
else:
    asum += a[i]
    bsum += b[j]
    while i < len(a):
       

        if asum < bsum:
            i += 1
            asum += a[i]
        elif asum > bsum:
            j += 1
            bsum += b[j]
        else:
            length += 1
            i += 1
            j += 1
            if i < len(a) and j < len(b):
                asum += a[i]
                bsum += b[j]
        
    print(length)