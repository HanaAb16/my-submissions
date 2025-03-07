# Problem: Array Splitting - https://codeforces.com/problemset/problem/1197/C

from collections import Counter , defaultdict
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
    diff = []
    ans = 0
    for i in range(1 , n):
        diff.append(nums[i] - nums[i - 1])
    diff.sort(reverse= True)
    for i in range(k - 1 , n - 1):
        ans += diff[i]
    print(ans)










def main():
    t = 1

    while t:
        solution()
        t -= 1

main()

