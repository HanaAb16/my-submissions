# Problem:  Network Topology - https://codeforces.com/problemset/problem/292/B

from collections import Counter , defaultdict
from cmath import inf
def inp(): return(int(input()))

def arr():return(list(map(int,input().split())))

def st():
    s = input()
    return(list(s[:-1]))

def num(): return(map(int,input().split()))





def solution():
    n , m = arr()
    graph = defaultdict(list)
    for _ in range(m):
        x , y = arr()
        graph[x].append(y)
        graph[y].append(x)
    degree = defaultdict(int)
    for i in range(1 , n + 1):
        degree[2 * len(graph[i])] += 1
    if degree[2] == 2 and degree[4] == n - 2:
        print("bus topology")
    elif degree[4] == n:
        print("ring topology")
    elif degree[2 * (n - 1)] == 1 and degree[2] == n - 1:
        print("star topology")
    else:
        print('unknown topology')












def main():
    t = 1

    while t:
        solution()
        t -= 1

main()

