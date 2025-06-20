# Problem: Circumference of a Tree - https://codeforces.com/gym/102694/problem/A

import sys
from collections import Counter, defaultdict
from cmath import inf
from types import GeneratorType

input = sys.stdin.readline

def bootstrap(f, stack=[]):
    def wrappedfunc(*args, **kwargs):
        if stack:
            return f(*args, **kwargs)
        else:
            to = f(*args, **kwargs)
            while True:
                if isinstance(to, GeneratorType):
                    stack.append(to)
                    to = next(to)
                else:
                    stack.pop()
                    if not stack:
                        break
                    to = stack[-1].send(to)
            return to
    return wrappedfunc

def inp(): return int(input())

def arr(): return list(map(int, input().split()))

def st(): return list(input().strip())

def num(): return map(int, input().split())

def str_matrix(n): return [list(input().strip()) for _ in range(n)]

def int_matrix(n): return [list(map(int, input().split())) for _ in range(n)]

def in_bounds(x, y, n, m): return 0 <= x < n and 0 <= y < m

directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]

class Union:
    def __init__(self, n):
        self.size = [1] * (n + 1)
        self.parent = [i for i in range(n + 1)]

    def find(self, x):
        if self.parent[x] == x:
            return x
        self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        px = self.find(x)
        py = self.find(y)
        if px != py:
            if self.size[px] < self.size[py]:
                self.parent[px] = py
                self.size[py] += self.size[px]
            else:
                self.parent[py] = px
                self.size[px] += self.size[py]

    def get(self, x, y):
        return self.find(x) == self.find(y)






def solution():
    n = inp()
    if n == 1:
        print(0)
        return
    tree = defaultdict(list)

    for _ in range(n - 1):
        u , v = arr()
        tree[u].append(v)
        tree[v].append(u)

    diameter = 0
    visited = [0] * (n + 1)

    @bootstrap
    def dfs(node):
        nonlocal diameter
        visited[node] = 1
        high1 , high2 = 0 , 0 

        for neb in tree[node]:
            if not visited[neb]:
                h = yield dfs(neb)
                if h > high1:
                    high2 = high1
                    high1 = h
                elif h > high2:
                    high2 = h

        diameter = max(diameter , high1 + high2)
        yield high1 + 1
    dfs(1)
    print(diameter * 3)






def main():
    t = 1
    while t:
        solution()
        t -= 1

main()