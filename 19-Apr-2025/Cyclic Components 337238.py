# Problem: Cyclic Components - https://codeforces.com/problemset/problem/977/E

from collections import Counter , defaultdict
from cmath import inf
from types import GeneratorType
def inp(): return(int(input()))

def arr():return(list(map(int,input().split())))

def st():
    s = input()
    return(list(s[:-1]))

def num(): return(map(int,input().split()))

def bootstrap(f, stack=[]):
    def wrappedfunc(*args, **kwargs):
        if stack:
            return f(*args, **kwargs)
        else:
            to = f(*args, **kwargs)
            while True:
                if type(to) is GeneratorType:
                    stack.append(to)
                    to = next(to)
                else:
                    stack.pop()
                    if not stack:
                        break
                    to = stack[-1].send(to)
            return to
    return wrappedfunc




def solution():
    n , m = arr()
    graph = defaultdict(list)
    for _ in range(m):
        v , u = arr()
        graph[v].append(u)
        graph[u].append(v)
    visited = [0] * (n + 1)
    @ bootstrap
    def dfs(node):
        is_cyclic = True
        if len(graph[node]) != 2:
            is_cyclic = False
        for neb in graph[node]:
            if not visited[neb]:
                visited[neb] = 1
                returned = yield dfs(neb)
                if not returned:
                    is_cyclic = False
        yield is_cyclic
    ans = 0
    for i in range(1 , n + 1):
        if not visited[i]:
            visited[i] = 1
            if dfs(i):
                ans += 1
    print(ans)










def main():
    t = 1

    while t:
        solution()
        t -= 1

main()

