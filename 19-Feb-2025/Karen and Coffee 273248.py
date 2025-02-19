# Problem: Karen and Coffee - https://codeforces.com/contest/816/problem/B

from collections import Counter , defaultdict
from cmath import inf
def arr(): return list(map(int , (x for x in input().split())))
n , k , q = arr()
recipe = []
ques = []
for _ in range(n):
    left , right = arr()
    recipe.append([left , right])
for _ in range(q):
    l , r = arr()
    ques.append([l , r])
big = [0] * 200003
for i in range(n):
    big[recipe[i][0]] += 1
    big[recipe[i][1] + 1] -= 1
for i in range(1 , len(big)):
    big[i] += big[i - 1]
for i in range(len(big)):
    if big[i] >= k:
        big[i] = 1
    else:
        big[i] = 0
for i in range(1 , len(big)):
    big[i] += big[i - 1]
for i in range(q):
    print(big[ques[i][1]] - big[ques[i][0] - 1])

