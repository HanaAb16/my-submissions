# Problem: Experience - https://codeforces.com/edu/course/2/lesson/7/1/practice/contest/289390/problem/C

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
    def __init__(self , n):
        self.size = [1] * (n + 1)
        self.parent = [i for i in range(n + 1)]
        self.exp = [0] * (n + 1)

    def find(self , x):
        if self.parent[x] == x:
            return x
        return self.find(self.parent[x])
    
    def union(self , x , y):
        px = self.find(x)
        py = self.find(y)
        if px != py:
            if self.size[px] < self.size[py]:
                self.parent[px] = py
                self.size[py] += self.size[px]
                self.exp[px] -= self.exp[py]

            elif self.size[px] > self.size[py]:
                self.parent[py] = px
                self.size[px] += self.size[py]
                self.exp[py] -= self.exp[px]

            else:
                self.parent[px] = py
                self.size[py] += self.size[px]
                self.exp[px] -= self.exp[py]
    def get(self , x , y):
        px = self.find(x)
        py = self.find(y)
        if px == py:
            return True
        return False

def solution():
    n , m = arr()
    uni = Union(n)
    for _ in range(m):
        command = input().split()
        if command[0] == 'join':
            uni.union(int(command[1]) , int(command[2]))
        elif command[0] == 'add':
            uni.exp[uni.find(int(command[1]))] += int(command[2])
        else:
            x = int(command[1])
            ans = 0
            while uni.parent[x] != x:
                ans += uni.exp[x]
                x = uni.parent[x]
            ans += uni.exp[x]
            print(ans)
        

            










def main():
    t = 1
    while t:
        solution()
        t -= 1

main()