# Problem: D - Meklit's Chat Screen - https://codeforces.com/gym/594077/problem/D

from collections import Counter , defaultdict, deque
from cmath import inf
def inp(): return(int(input()))

def arr():return(list(map(int,input().split())))

def st():
    s = input()
    return(list(s[:-1]))

def num(): return(map(int,input().split()))





def solution():
    n , k = arr()
    nums = arr()
    dq = deque()
    s = set()
    for i in range(n):
        if nums[i] not in s:
            if len(dq) == k:
                s.remove(dq.pop())
            dq.appendleft(nums[i])
            s.add(nums[i])
    print(len(dq))
    print(*dq)










def main():
    t = 1

    while t:
        solution()
        t -= 1

main()

