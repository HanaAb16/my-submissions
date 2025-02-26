# Problem: B - Jo's Adventure - https://codeforces.com/gym/590053/problem/B

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
    nums = arr()
    prefix = [0] * n
    suffix = [0] * n
    for i in range(1 , n):
        if nums[i] < nums[i - 1]:
            prefix[i] = nums[i - 1] - nums[i]
    for i in range(1 , n):
        prefix[i] += prefix[i - 1]
    for i in range(n - 2 , -1 , -1):
        
        if nums[i] < nums[i + 1]:
            suffix[i] = nums[i + 1] - nums[i]
    for i in range(n - 2 , -1 , -1):
        suffix[i] += suffix[i + 1]
    
    for _ in range(m):
        l , r = arr()
        if l <= r:
            print(prefix[r - 1] - prefix[l - 1])
        else:
            print(abs(suffix[l - 1] - suffix[r - 1]))

    pass










def main():
    t = 1

    while t:
        solution()
        t -= 1

main()

