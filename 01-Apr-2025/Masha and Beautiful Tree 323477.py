# Problem: Masha and Beautiful Tree - https://codeforces.com/problemset/problem/1741/D

from collections import Counter , defaultdict
from cmath import inf
def inp(): return(int(input()))

def arr():return(list(map(int,input().split())))

def st():
    s = input()
    return(list(s[:-1]))

def num(): return(map(int,input().split()))





def solution():
    m = inp()
    nums = arr()
    count = 0
    def merge(left_half , right_half):
        nonlocal count
        ans = []
        if left_half[0] > right_half[0]:
            ans.extend(right_half)
            ans.extend(left_half)
            count += 1
        else:
            ans.extend(left_half)
            ans.extend(right_half)
        return ans

    def merge_sort(left , right ,  arr):
        if left == right:
            return [nums[left]]
        mid = (left + right) // 2
        left_half = merge_sort(left , mid , nums)
        right_half = merge_sort(mid + 1 , right , nums)
        return merge(left_half , right_half)
    result = merge_sort(0 , m - 1 , nums)
    
    if result == sorted(result):
        print(count)
    else:
        print(-1)










def main():
    t = inp()

    while t:
        solution()
        t -= 1

main()

